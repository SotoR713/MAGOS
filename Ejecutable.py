from BACK.Clases.Mapa import Mapa
from FRONT.InterfazPantalla import finalizar_juego, titulo_Final, titulo_Inicio, nombrar_Jugador
from FRONT.InterfazVarios import limpiar_Pantalla
from CONTROLADOR.ReccorrerMapa import avanzar, resolver_Evento

bucle_Juego=0
while bucle_Juego ==0:
    titulo_Inicio()     
    
    mapa1 = Mapa(nombrar_Jugador())
    while mapa1.get_jugador().get_hpActual() >0:
        evento = avanzar(mapa1)       
        resolver_Evento(mapa1,evento)
        mapa1.generar_Siguientes()
    finalizar_juego(mapa1.get_caminoHistorico(),mapa1.get_posicion())
   