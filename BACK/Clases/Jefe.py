from BACK.Clases.Magos import Mago
from BACK.Clases.Elementos import Agua,Fuego,Planta,Tierra,Neutral
from Configuracion import statsPorNivelJefe, porcentajeDañoCriticoJefe,bonificacionCriticoJefe,evasionJefe

class Jefe(Mago):

    def repartir_Stats(self):
            
        puntos = statsPorNivelJefe * self._nivel

        while puntos > statsPorNivelJefe:
            self._hpMax += 1
            self._fuerza += 1
            self._armadura += 1
            self._velocidad += 1
            puntos -= statsPorNivelJefe
        while puntos > 0:
            self._hpMax += 1
            self._velocidad +=1
            puntos -= 2
        self._hpActual = self._hpMax
   
    def calcular_Critico(self,rival,aleato,daño):
        porcentajeDaño = porcentajeDañoCriticoJefe
      
        activacion = aleato % 100

        if activacion <= porcentajeDaño:
            daño += (daño*bonificacionCriticoJefe)//100
        return daño
        
    def evasion(self, rival,aleato):
        
        porcentajeEva = evasionJefe   

        activacion = aleato %100

        if activacion <= porcentajeEva:
            esquivar=0
        else: 
            esquivar=1
        return esquivar

listaJefes =[
    Jefe("0","Nullizador",Neutral,28,28,2,4,1,0),
    Jefe("1","Hexecutor",Fuego,16,16,10,4,5,0),
    Jefe("2","Daemonus",Fuego,19,19,7,4,5,0),
    Jefe("3","ElProfeCaguamo",Tierra,22,22,6,6,1,0),
    Jefe("4","Bytemaster",Agua,18,18,5,3,9,0),
    Jefe("5","Compilator",Planta,24,24,4,5,2,0),
    Jefe("6","Piri",Neutral,25,25,7,2,1,0),
    Jefe("7","Fatalerror",Neutral,20,20,8,3,4,0),
    Jefe("8","CeszarW",Fuego,17,17,7,5,6,0),
    Jefe("9","CarluxSanguis",Neutral,26,26,6,2,1,0),
]