from BACK.Clases.Magos import Mago
from Configuracion import statsPorNivelJugador,maximoCriticoJugador,bonificacionCriticoJugador, maximaevasionJugador
from FRONT.Interfaz import imprimir_Mensaje_OpcionNoValida

class Jugador(Mago):

    def subir_Nivel(self):
        self._nivel += 1
        self.repartir_Stats()

    def repartir_Stats(self):
        puntos = statsPorNivelJugador
        while puntos > 0:
            esValor = False
            while esValor == False:
                eleccion = input(f"tienes {puntos} puntos a repartir \n selecciona a que le quieres asignar el siguiente punto\n1-HP\n2-Fuerza\n3-Armadura\n4-Velocidad:\n")
                esValor = eleccion.isdigit()
            eleccion = int(eleccion)

            if eleccion == 1:
                self._hpMax += 1
                puntos -= 1
            elif eleccion == 2:
                self._fuerza += 1
                puntos -= 1
            elif eleccion == 3:
                self._armadura += 1
                puntos -= 1
            elif eleccion == 4:
                self._velocidad += 1
                puntos -= 1
            else:
                imprimir_Mensaje_OpcionNoValida()


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
   