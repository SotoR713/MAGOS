from BACK.Clases.Magos import Mago
from Configuracion import maximoCriticoJugador,bonificacionCriticoJugador, maximaevasionJugador

class Jugador(Mago):

    def subir_Nivel(self):
        self._nivel += 1

    def repartir_Stats(self,eleccion):
    
        if eleccion == 1:
            self._hpMax +=1
        elif eleccion == 2:
            self._fuerza +=1
        elif eleccion == 3:
            self._armadura +=1
        elif eleccion == 4:
            self._velocidad +=1    


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
   