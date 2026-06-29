from BACK.Clases.Generadores import Generadores
from BACK.Clases.Eventos import BRival,BJefe,Cofre,Curacion
from BACK.Funciones.Calculadoras import raiz_digital
from Configuracion import posicionesJefe,siguienteRival,siguienteCofre,porcentajeCuracionCofre,porcentajeCuracionEvento,umbralBatalla,umbralCuracion,umbralSubir,porcentajeDañoCofre


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


    def registrar_Avance(self, eleccion):
        self._camino.append(eleccion)
        self._posicion += 1
        self._caminoHistorico = ""
        for i in self._historial:
            self._caminoHistorico += i

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

    def agregar_Historial(self, simbolo):
        self._historial.append(simbolo)

    def marcar_Rival(self):
        largo = len(self._historial) - 1
        if self._historial[largo] == "[":
            self._historial[largo] = "→[⚔]"
        else:
            self._historial.append("→⚔")