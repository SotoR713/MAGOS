import nt

from BACK.Clases.Elementos import Agua,Fuego,Planta,Tierra,Neutral
from BACK.Clases.ValoracionCaracter import listaCaracteres
from BACK.Clases.Jugador import Jugador
from Configuracion import vidaJugador,fuerzaJugador,armaduraJugador,velocidadJugador
from FRONT.InterfazVarios import imprimir_Mensaje_OpcionNoValida, limpiar_Pantalla

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

    mostrar_Stats(player1)
    print(f"Semilla: {idJugador}")
    return player1


def jefe_Derrotado():
    print(r"    __ _____ _____ _____    _____ _____ _____ _____ _____ ____  _____ ")
    print(r" __|  |   __|   __|   __|  |  |  |   __|   | |     |     |    \|     |")
    print(r"|  |  |   __|   __|   __|  |  |  |   __| | | |   --|-   -|  |  |  |  |")
    print(r"|_____|_____|__|  |_____|   \___/|_____|_|___|_____|_____|____/|_____|")





def mostrar_Stats(mago):
        print("")
        print("╔══════════════╗")
        print("║",mago.get_nombre()," de ",mago.get_elemento().get_nombre())
        print("════════════════")
        print("║","Nivel: ",mago.get_nivel())
        print("║","HP: ",mago.get_hpActual(),"/",mago.get_hpMax())
        print("║","Fuerza: ",mago.get_fuerza())
        print("║","Armadura: ",mago.get_armadura())
        print("║","Velocidad: ",mago.get_velocidad())
        print("╚══════════════╝")
        print("")



def imprimir_Repartir_Stats(puntos):
    valido=False

    while valido == False:
            print(f"tienes {puntos} puntos a repartir")
            print("selecciona a que le quieres asignar el siguiente punto:")
            print("1-HP")
            print("2-Fuerza")
            print("3-Armadura")
            print("4-Velocidad")
            eleccion=input()
            if  eleccion.isdigit():
                eleccion = int(eleccion)
                if eleccion <=4 and eleccion>0:
                    valido=True
                else:
                    imprimir_Mensaje_OpcionNoValida()
            else:
                imprimir_Mensaje_OpcionNoValida()
    return eleccion

def finalizar_juego(mapa1):
    print("senda: ",mapa1._caminoHistorico)
    print("Has llegado hasta la posicion:",mapa1.get_posicion())
    print("")
    titulo_Final()
    print("")
    input("presion ENTER para reiniciar")
    limpiar_Pantalla()