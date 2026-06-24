from FRONT.InterfazPantalla import jefe_Derrotado,mostrar_Stats
from FRONT.InterfazMapa import imprimir_Cofre_Batalla, imprimir_Cofre_Curacion,imprimir_Cofre_Daño,imprimir_Cofre_SubirNivel,imprimir_Camino,imprimir_Donde_Avanzar
from FRONT.InterfazVarios import limpiar_Pantalla,imprimir_Pausas

def avanzar(senda):
    eleccion = ""
    imprimir_Pausas()
    limpiar_Pantalla()
    imprimir_Camino(senda.get_caminoHistorico(),senda.get_siguiente0().caracter,senda.get_siguiente1().caracter)
    eleccion = imprimir_Donde_Avanzar(eleccion,senda.get_siguiente0().nombre,senda.get_siguiente1().nombre)              

    if eleccion == "0":
        return senda.get_siguiente0()
    elif eleccion == "1":
        return   senda.get_siguiente1()


