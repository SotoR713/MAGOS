from BACK.Clases.Generadores import Generadores
from BACK.Clases.Eventos import BRival,BJefe,Cofre,Curacion
from BACK.Funciones.Calculadoras import raiz_digital
from BACK.Funciones.Fabrica import crear_Rival,crear_Jefe
from Configuracion import posicionesJefe,siguienteRival,siguienteCofre,porcentajeCuracionCofre,porcentajeCuracionEvento,umbralBatalla,umbralCuracion,umbralSubir,porcentajeDañoCofre
from CONTROLADOR.Combate import enfrentamiento,calculo_Repartir_Stats
from CONTROLADOR.ReccorrerMapa import avanzar
from FRONT.InterfazPantalla import jefe_Derrotado,mostrar_Stats
from FRONT.InterfazMapa import imprimir_Cofre_Batalla, imprimir_Cofre_Curacion,imprimir_Cofre_Daño,imprimir_Cofre_SubirNivel,imprimir_Camino,imprimir_Donde_Avanzar
from FRONT.InterfazVarios import limpiar_Pantalla,imprimir_Pausas


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
    def get_caminoHistorico(self):
        return self._caminoHistorico
        
    def camino(self):
        imprimir_Pausas()
        limpiar_Pantalla()
        
        self.get_caminoHistorico()=""
        for i in self._historial():
            self._caminoHistorico() += i

        self._camino.append(avanzar(self))
        self._posicion += 1   


    def validar_vs_Jefe(self):
        if (len(self._camino)) % posicionesJefe == 0:
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
        if v1 <= siguienteRival:
            self._siguiente1= BRival
        elif v1 <= siguienteCofre:
            self._siguiente1= Cofre
        else:
            self._siguiente1= Curacion
        v2 = (self.get_generador().aleatorio() )
        v2=raiz_digital(v2)
        if v2 <= siguienteRival:
            self._siguiente0= BRival
        elif v2 <= siguienteCofre:
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
            jefe_Derrotado()
        elif evento == Curacion:
            self.get_jugador().curar(self.get_jugador().get_hpMax()*porcentajeCuracionEvento//100)
            self._historial.append("→♥") 
        elif evento == Cofre:
            v1 = (self.get_generador().aleatorio() * self.get_generador().aleatorio() )// 713
            v1 = raiz_digital(v1)

            if v1 <= umbralSubir:
                self.get_jugador().subir_Nivel() 
                calculo_Repartir_Stats(self.get_jugador())               
                mostrar_Stats(self.get_jugador())
                imprimir_Cofre_SubirNivel()
                self._historial.append("→[↑]")
            elif v1 <= umbralCuracion:
                vidaCurar=self.get_jugador().get_hpMax()*porcentajeCuracionCofre//100
                self.get_jugador().curar(vidaCurar)
                imprimir_Cofre_Curacion(vidaCurar)
                self._historial.append("→[♥]")
            elif v1 <= umbralBatalla:
                self._historial.append("[")
                self.resolver_Evento(BRival)
                imprimir_Cofre_Batalla()
            else:
                vidaDaño=self.get_jugador().get_hpMax()*porcentajeDañoCofre//100
                self.get_jugador().recibir_Daño(vidaDaño)
                imprimir_Cofre_Daño(vidaDaño)
                self._historial.append("→[↓]")