from Clases.Elementos import Agua,Fuego,Planta,Tierra,Neutral

def raiz_digital(numero):
    while numero >= 10:
        suma = 0
        for i in str(numero):
            suma += int(i)
        numero = suma
    return numero



def crear_Elemento(numeroDado):
    asignacionElemento = (numeroDado % 10) // 2
    if asignacionElemento == 0:
        elementoAsignar = Agua
    elif asignacionElemento == 1:
        elementoAsignar = Fuego
    elif asignacionElemento == 2:
        elementoAsignar = Planta
    elif asignacionElemento == 3:
        elementoAsignar = Tierra
    else:
        elementoAsignar = Neutral
    return elementoAsignar

