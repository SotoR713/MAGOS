from BACK.Clases.Magos import Mago
from Configuracion import statsPorNivelJugador,maximoCriticoJugador,bonificacionCriticoJugador, maximaevasionJugador
from CONTROLADOR.Repartir import calculo_Repartir_Stats

class Jugador(Mago):

    def subir_Nivel(self):
        self._nivel += 1
        self.repartir_Stats()

    def repartir_Stats(self):
        
        puntos = statsPorNivelJugador

        calculo_Repartir_Stats(self)


    def calcular_Critico(self,rival,aleato,daño):
        difVel = self.get_velocidad() - rival.get_velocidad()
        if difVel <= 0:
            porcentajeDaño = 0
        else:
            porcentajeDaño = (difVel*100)//rival.get_velocidad()
        
        if porcentajeDaño > maximoCriticoJugador:
            porcentajeDaño= maximoCriticoJugador
        elif porcentajeDaño < 0:
            porcentajeDaño = 0     

        activacion = aleato
        activacion = activacion % 100

        if activacion <= porcentajeDaño:
            daño += (daño*bonificacionCriticoJugador)//100

        return daño
    
    def evasion(self, rival,aleato):
        difVel = self.get_velocidad() - rival.get_velocidad()
        if difVel <= 0:
            porcentajeEva = 0
        else:
            porcentajeEva = (difVel*100)//rival.get_velocidad()
        
        if porcentajeEva > maximaevasionJugador:
            porcentajeEva= maximaevasionJugador
        elif porcentajeEva < 0:
            porcentajeEva = 0     

        activacion = aleato
        activacion = activacion % 100

        if activacion <= porcentajeEva:
            esquivar =0
        else:
            esquivar=1
        return esquivar
   