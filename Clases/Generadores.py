class Generadores:
    def __init__ (self,dado):
        self._dado = dado
        
    def aleatorio(self):
        self._dado = (self._dado * 120295 + 713) % (240214)
        return self._dado
    