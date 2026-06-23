class Elementos:
    def __init__ (self,nombre,fortaleza,debilidad):
        self._nombre = nombre
        self._fortaleza = fortaleza
        self._debilidad = debilidad
    
    def get_nombre(self):
        return self._nombre
    def get_fortaleza(self):
        return self._fortaleza
    def get_debilidad(self):
        return self._debilidad

    
Agua = Elementos("Agua","Fuego","Tierra")
Fuego = Elementos("Fuego","Planta","Agua")
Planta = Elementos("Planta","Tierra","Fuego")
Tierra = Elementos("Tierra","Agua","Planta")
Neutral = Elementos("Neutral","","")

