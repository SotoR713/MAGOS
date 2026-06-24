from FRONT.InterfazPantalla import imprimir_Repartir_Stats
from Configuracion import statsPorNivelJugador

def calculo_Repartir_Stats(jugador):
        
    puntos = statsPorNivelJugador
    while puntos > 0:
        
        eleccion =  imprimir_Repartir_Stats(puntos)
        
        jugador.repartir_Stats(eleccion)

        puntos -= 1
            


