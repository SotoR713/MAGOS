from Clases.Magos import Mago

class Jugador(Mago):

    def subir_Nivel(self):
        self._nivel += 1
        self.repartir_Stats()
        self.mostrar_Stats()

    def repartir_Stats(self):
        puntos = 4
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
                print("Estadistica no existe")


    def calcular_Critico(self,rival,aleato,daño):
        difVel = self._velocidad - rival._velocidad
        if difVel <= 0:
            porcentajeDaño = 0
        else:
            porcentajeDaño = (difVel*100)//rival._velocidad
        
        if porcentajeDaño > 30:
            porcentajeDaño= 30
        elif porcentajeDaño < 0:
            porcentajeDaño = 0     

        activacion = aleato
        activacion = activacion % 100

        if activacion <= porcentajeDaño:
            daño += (daño*50)//100

        return daño
    
    def evasion(self, rival,aleato):
        difVel = self._velocidad - rival._velocidad
        if difVel <= 0:
            porcentajeEva = 0
        else:
            porcentajeEva = (difVel*100)//rival._velocidad
        
        if porcentajeEva > 20:
            porcentajeEva= 20
        elif porcentajeEva < 0:
            porcentajeEva = 0     

        activacion = aleato
        activacion = activacion % 100

        if activacion <= porcentajeEva:
            esquivar =0
        else:
            esquivar=1
        return esquivar
   