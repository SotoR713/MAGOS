from BACK.Clases.Mapa import Mapa
from FRONT.InterfazPantalla import titulo_Final, titulo_Inicio, nombrar_Jugador
from FRONT.InterfazVarios import limpiar_Pantalla

bucle_Juego=0
while bucle_Juego ==0:
    titulo_Inicio()     
    
    mapa1 = Mapa(nombrar_Jugador())
    while mapa1.get_jugador().get_hpActual() >0:
        print(f"Posición: {mapa1.get_posicion()}")
        mapa1.resolver_Evento(mapa1.avanzar())
        mapa1.generar_Siguientes()
    print("senda: ",mapa1._caminoHistorico)
    print("Has llegado hasta la posicion:",mapa1.get_posicion())
    print("")
    titulo_Final()
    print("")
    input("presion ENTER para reiniciar")
    limpiar_Pantalla()