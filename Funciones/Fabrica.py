from Clases.Elementos import *
from Clases.Rival import *
from Clases.Jefe import *
from Clases.ValoracionCaracter import *
from Clases.Jugador import *




def crear_Rival(numeroDado,valorPosicion_Actual):
    v1 = numeroDado * valorPosicion_Actual
    v1 = v1 %20

    nivelar = v1 % 10
    if nivelar > 7:
        valorNivel=valorPosicion_Actual-1
    elif nivelar > 4:
        valorNivel=valorPosicion_Actual-2
    else:
        valorNivel=valorPosicion_Actual

    valorPosicion_Actual=valorNivel

    if valorNivel<0:
        valorPosicion_Actual = 0

    asignacionElemento = (numeroDado % 10) // 2
    if asignacionElemento == 0:
        v2 = Agua
    elif asignacionElemento == 1:
        v2 = Fuego
    elif asignacionElemento == 2:
        v2 = Planta
    elif asignacionElemento == 3:
        v2 = Tierra
    else:
        v2 = Neutral

    valores_Rival = listaRivales[v1]
    rival_Actual = Rival(valores_Rival.get_ID(),valores_Rival.get_nombre(),v2,valores_Rival.get_hpActual(),valores_Rival.get_hpMax(),valores_Rival.get_fuerza(),valores_Rival.get_armadura(),valores_Rival.get_velocidad(),valorPosicion_Actual)
    rival_Actual.repartir_Stats()
    return rival_Actual
   

def crear_Jefe(numeroDado,valorPosicion_Actual):
    v1 = numeroDado
    v1 = v1 % 10

    asignacionElemento = (numeroDado % 10) // 2
    if asignacionElemento == 0:
        v2 = Agua
    elif asignacionElemento == 1:
        v2 = Fuego
    elif asignacionElemento == 2:
        v2 = Planta
    elif asignacionElemento == 3:
        v2 = Tierra
    else:
        v2 = Neutral


    valores_Jefe = listaJefes[v1]
    jefe_Actual = Jefe(valores_Jefe.get_ID(),valores_Jefe.get_nombre(),v2,valores_Jefe.get_hpActual(),valores_Jefe.get_hpMax(),valores_Jefe.get_fuerza(),valores_Jefe.get_armadura(),valores_Jefe.get_velocidad(),valorPosicion_Actual)
    jefe_Actual.repartir_Stats()
    return jefe_Actual


