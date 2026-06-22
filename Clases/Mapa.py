from Clases.Generadores import Generadores
from Clases.Eventos import *
from Funciones.Calculadoras import *
from Funciones.Fabrica import *
from Funciones.Combate import *

class Mapa:
    def __init__ (self,jugador):
        self._jugador = jugador
        self._generador = Generadores((jugador.get_ID()))
        self._posicion = 0
        self._camino = []
        self._historial =["█"]
        self._siguiente0 = BRival
        self._siguiente1 = BRival
        self._caminoHistorico = "█"

    def get_jugador(self):
        return self._jugador
    def get_generador(self):
        return self._generador
    def get_posicion(self):
        return self._posicion
    def get_camino(self):
        return self._camino
    def get_siguiente0(self):
        return self._siguiente0
    def get_siguiente1(self):
        return self._siguiente1
    
        
    def avanzar(self):
        eleccion = ""
        self._caminoHistorico=""
        for i in self._historial:
            self._caminoHistorico += i
        print(f" {" " * len(self._caminoHistorico)}{self.get_siguiente0().caracter}")
        print(self._caminoHistorico)
        print(f" {" " * len(self._caminoHistorico)}{self.get_siguiente1().caracter}")
        while eleccion != "0" and eleccion !="1":
            eleccion = input(f"seleccione a donde avanzar:\n0-{self.get_siguiente0().nombre}\n1-{self.get_siguiente1().nombre}\n")
                    
        self._camino.append(eleccion)
        self._posicion += 1   

        if eleccion == "0":
            return self.get_siguiente0()
        elif eleccion == "1":
            return   self.get_siguiente1()

    def validar_vs_Jefe(self):
        if (len(self._camino)) % 10 == 0:
            return True
        else:
            return False

    def generar_Siguientes(self):
        if self.validar_vs_Jefe() == True:
            self._siguiente0 = BJefe
            self._siguiente1 = BJefe
        else:
            self.generar_siguiente_no_Jefe()
        return self._siguiente0,self._siguiente1

    def  generar_siguiente_no_Jefe(self):
        v1 = (self.get_generador().aleatorio())
        v1=raiz_digital(v1)
        if v1 <= 6:
            self._siguiente1= BRival
        elif v1 <= 8:
            self._siguiente1= Cofre
        else:
            self._siguiente1= Curacion
        v2 = (self.get_generador().aleatorio() )
        v2=raiz_digital(v2)
        if v2 <= 6:
            self._siguiente0= BRival
        elif v2 <= 8:
            self._siguiente0= Cofre
        else:
            self._siguiente0= Curacion
        return self._siguiente0,self._siguiente1

    def resolver_Evento(self, evento):
        if evento == BRival:
            Brival = crear_Rival(self.get_generador().aleatorio(), len(self.get_camino()))
            enfrentamiento(self.get_jugador(), Brival,self.get_generador())
            largo=len(self._historial)-1
            if self._historial[largo] == "[":
                self._historial[largo]="→[⚔]"
            else:    
                self._historial.append("→⚔")
        elif evento == BJefe:
            bjefe = crear_Jefe(self.get_generador().aleatorio(), len(self.get_camino()))
            enfrentamiento(self.get_jugador(), bjefe,self.get_generador())
            self._historial.append( "→☠")
        elif evento == Curacion:
            self.get_jugador().curar(self.get_jugador().get_hpMax()*3//10)
            self._historial.append("→♥")
        elif evento == Cofre:
            v1 = (self.get_generador().aleatorio() * self.get_generador().aleatorio() )// 713
            v1 = raiz_digital(v1)

            if v1 <= 4:
                self.get_jugador().subir_Nivel()
                print("Subiste Nivel")
                self._historial.append("→[↑]")
            elif v1 <= 7:
                vidaCurar=self.get_jugador()._hpMax*3//10
                self.get_jugador().curar(vidaCurar)
                print(f"Recuperaste {vidaCurar} de vida")
                self._historial.append("→[♥]")
            elif v1 <= 8:
                self._historial.append("[")
                self.resolver_Evento(BRival)
                print("BATALLA")
            else:
                vidaDaño=self.get_jugador()._hpMax*1//10
                self.get_jugador().recibir_Daño(vidaDaño)
                print(f"Has perdido {vidaDaño}")
                self._historial.append("→[↓]")