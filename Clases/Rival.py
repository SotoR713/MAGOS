from Clases.Magos import Mago
from Clases.Elementos import Agua,Fuego,Planta,Tierra,Neutral
from Configuracion import *

class Rival(Mago):

    def repartir_Stats(self):

        puntos = statsPorNivelRival * (self._nivel - (2*(self._nivel//10)))

        while puntos > 4:
            self._hpMax += 1
            self._fuerza += 1
            self._armadura += 1
            self._velocidad += 1
            puntos -= 4
        while puntos > 0:
            self._velocidad +=1
            puntos -= 1
        self._hpActual = self._hpMax

    def calcular_Critico(self,rival,aleato,daño):

        porcentajeDaño = porcentajeDañoCriticoRival   

        activacion = aleato %100

        if activacion <= porcentajeDaño:
            daño += (daño*bonificacionCriticoRival)//100
        return daño
    
    def evasion(self, rival,aleato):

        porcentajeEva = evasionRival   

        activacion = aleato %100

        if activacion <= porcentajeEva:
            esquivar=0
        else: 
            esquivar=1
        
        return esquivar
    

listaRivales = [
    Rival("00","Sortilego",Agua,24,24,3,4,4,0),
    Rival("01","Debugorio",Agua,24,24,3,4,4,0),
    Rival("02","Hexomante",Fuego,18,18,8,4,5,0),
    Rival("03","Algoritus",Planta,22,22,4,6,3,0),
    Rival("04","Binarcano",Tierra,26,26,3,5,1,0),
    Rival("05","Stackomante",Neutral,20,20,5,5,5,0),
    Rival("06","Recursio",Agua,17,17,6,3,9,0),
    Rival("07","Kernelius",Fuego,15,15,10,4,6,0),
    Rival("08","Overflorius",Planta,19,19,4,8,4,0),
    Rival("09","Crashelio",Tierra,21,21,5,7,2,0),
    Rival("10","Punterius",Agua,30,30,1,2,2,0),
    Rival("11","Hexagoro",Fuego,16,16,11,3,5,0),
    Rival("12","Alquimia",Planta,18,18,6,5,6,0),
    Rival("13","Oraclon",Tierra,23,23,4,7,1,0),
    Rival("14","Trucanor",Agua,20,20,7,2,6,0),
    Rival("15","Nigrombo",Fuego,17,17,9,5,4,0),
    Rival("16","Musgorio",Planta,25,25,3,6,1,0),
    Rival("17","Pedrurio",Tierra,28,28,2,5,0,0),
    Rival("18","Cubistar",Agua,14,14,7,4,10,0),
    Rival("19","Esotron",Fuego,20,20,6,4,5,0)
]