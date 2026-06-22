from Clases.Elementos import Agua,Fuego,Planta,Tierra,Neutral
from Clases.ValoracionCaracter import listaCaracteres
from Clases.Jugador import Jugador
from Configuracion import *

def titulo_Inicio():

    print("███╗   ███╗ █████╗  ██████╗  ██████╗ ███████╗")
    print("████╗ ████║██╔══██╗██╔════╝ ██╔═══██╗██╔════╝")
    print("██╔████╔██║███████║██║  ███╗██║   ██║███████╗")
    print("██║╚██╔╝██║██╔══██║██║   ██║██║   ██║╚════██║")
    print("██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝███████║")
    print("╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝")
    print("Maestros Arcanos Guiados por la Onceava Senda")
    print("")
    print("        --Tu nombre define tu senda-")
    print("     -La senda recuerda tus decisiones-")
    print("")

    

def titulo_Final():
    print(            " ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ ")
    print(            "██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗")
    print(            "██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝")
    print(            "██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
    print(            "╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║")
    print(            " ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")


def nombrar_Jugador():
    nombre_Usuario = input("Ingrese el nombre del usuario ")
    idJugador = "0"
    
    for i in nombre_Usuario:
        for j in listaCaracteres:
            if i.lower() == j.letra:
                idJugador += str(j.valor)
    idJugador=int(idJugador)            
    if idJugador < 1:
        idJugador = 713
    
    elemento_Jugador = "error"
    while elemento_Jugador == "error":
        esValor = False
        while esValor == False:
            elemento_Jugador = input("selecciona un elemento de la lista: \n1-Agua\n2-Fuego\n3-Planta\n4-Tierra\n5-Neutral\n:")
            esValor=elemento_Jugador.isdigit()
        elemento_Jugador=int(elemento_Jugador)
        if elemento_Jugador == 1:
            elemento_Jugador = Agua
        elif elemento_Jugador == 2:
            elemento_Jugador = Fuego
        elif elemento_Jugador == 3:
            elemento_Jugador = Planta
        elif elemento_Jugador == 4:
            elemento_Jugador = Tierra
        elif elemento_Jugador == 5:
            elemento_Jugador = Neutral
        else:
            print("Elemento no existe")
            elemento_Jugador = "error"

    player1 = Jugador(idJugador,nombre_Usuario,elemento_Jugador,vidaJugador,vidaJugador,fuerzaJugador,armaduraJugador,velocidadJugador,0)

    player1.mostrar_Stats()
    print(f"Semilla: {idJugador}")
    return player1