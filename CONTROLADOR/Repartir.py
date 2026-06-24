from FRONT.InterfazPantalla import imprimir_Repartir_Stats

def calculo_Repartir_Stats(jugador):
        while puntos > 0:
            esValor = False
          
            eleccion =  imprimir_Repartir_Stats(esValor,puntos)

            if eleccion == 1:
                jugador._hpMax += 1
                puntos -= 1
            elif eleccion == 2:
                jugador._fuerza += 1
                puntos -= 1
            elif eleccion == 3:
                jugador._armadura += 1
                puntos -= 1
            elif eleccion == 4:
                jugador._velocidad += 1
                puntos -= 1
