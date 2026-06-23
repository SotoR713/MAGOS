from Configuracion import dañoMinimo,dañoFuerteElemental

class Mago:
    def __init__ (self,ID,nombre,elemento,hpActual,hpMax,fuerza,armadura,velocidad,nivel):
        self._ID = ID
        self._nombre = nombre
        self._elemento = elemento
        self._hpActual = hpActual
        self._hpMax = hpMax
        self._fuerza = fuerza
        self._armadura = armadura
        self._velocidad = velocidad
        self._nivel = nivel

    def get_ID(self):
        return self._ID
    def get_nombre(self):
        return self._nombre
    def get_elemento(self):
        return self._elemento
    def get_hpActual(self):
        return self._hpActual
    def get_hpMax(self):
        return self._hpMax
    def get_fuerza(self):
        return self._fuerza
    def get_armadura(self):
        return self._armadura
    def get_velocidad(self):
        return self._velocidad
    def get_nivel(self):
        return self._nivel
    


    def repartir_Stats(self):
        raise NotImplementedError("funcion repartir no declarada")
    
    def calcular_Critico(self,rival):
        raise NotImplementedError("funcion critico no declarada")
    
    def evasion(self,rival):
        raise NotImplementedError("funcion evasion no declarada")
    
    def mostrar_Stats(self):
        print(f"{self.get_nombre()} de {self.get_elemento().get_nombre()}:\nHP: {self.get_hpActual()}/{self.get_hpMax()}\nFuerza: {self.get_fuerza()}\nArmadura: {self.get_armadura()}\nVelocidad: {self.get_velocidad()}\nNivel: {self.get_nivel()}\n")

    def calcular_Daño(self,objetivo):
        daño = self.get_fuerza() - objetivo.get_armadura()
        if daño < dañoMinimo:
            daño=dañoMinimo
        if objetivo.get_elemento().get_nombre() == self.get_elemento().get_fortaleza():
            daño += (daño*dañoFuerteElemental)//100
        elif objetivo.get_elemento().get_nombre() == self.get_elemento().get_debilidad():
            daño = (daño*dañoFuerteElemental)//100
        if daño < dañoMinimo:
           daño=dañoMinimo
        return daño
        
    def recibir_Daño(self,daño):
        self._hpActual -= daño
        if self._hpActual < 0:
            self._hpActual = 0

    def curar(self,cantidadCurar):
        self._hpActual += cantidadCurar
        if self._hpActual > self._hpMax:
            self._hpActual = self._hpMax
        return cantidadCurar,