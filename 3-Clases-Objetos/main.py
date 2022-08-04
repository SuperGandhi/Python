class Car:
    """
        cuando  una propiedad o funcion empiezan con guion bajo no se debe manipular 
        fuera de la clase(convención)
    """
    _encendido = False
    
    def enciende(self):
        # variable shadowing dos variables del mismo nombres que no están relacioandas
        self._encendido = True
        pass
    
    def apaga(self):
        self._encendido = False
        
    def isEncendido(self):
        return self._encendido

a1 = Car()
a1.apaga()
print(a._encendido)

d2 = Car()
d2.encendido()
