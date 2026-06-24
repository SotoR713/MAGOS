from BACK.Clases.Rival import Rival, listaRivales
from BACK.Clases.Jefe import listaJefes, Jefe
from BACK.Funciones.Calculadoras import crear_Elemento



def crear_Rival(numeroDado,valorPosicion_Actual):
    nivelCrear = numeroDado * valorPosicion_Actual
    nivelCrear = nivelCrear %20

    nivelar = nivelCrear % 10
    if nivelar > 7:
        valorNivel=valorPosicion_Actual-1
    elif nivelar > 4:
        valorNivel=valorPosicion_Actual-2
    else:
        valorNivel=valorPosicion_Actual

    valorPosicion_Actual=valorNivel

    if valorNivel<0:
        valorPosicion_Actual = 0

    elementoAsignar = crear_Elemento(numeroDado)

    valores_Rival = listaRivales[nivelCrear]
    rival_Actual = Rival(valores_Rival.get_ID(),valores_Rival.get_nombre(),elementoAsignar,valores_Rival.get_hpActual(),valores_Rival.get_hpMax(),valores_Rival.get_fuerza(),valores_Rival.get_armadura(),valores_Rival.get_velocidad(),valorPosicion_Actual)
    rival_Actual.repartir_Stats()
    return rival_Actual
   

def crear_Jefe(numeroDado,valorPosicion_Actual):
    nivelCrear = numeroDado
    nivelCrear = nivelCrear % 10

    elementoAsignar = crear_Elemento(numeroDado)

    valores_Jefe = listaJefes[nivelCrear]
    jefe_Actual = Jefe(valores_Jefe.get_ID(),valores_Jefe.get_nombre(),elementoAsignar,valores_Jefe.get_hpActual(),valores_Jefe.get_hpMax(),valores_Jefe.get_fuerza(),valores_Jefe.get_armadura(),valores_Jefe.get_velocidad(),valorPosicion_Actual)
    jefe_Actual.repartir_Stats()
    return jefe_Actual


