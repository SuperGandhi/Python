
# clase base
class Juguete:
    """
        cuando  una propiedad o funcion empiezan con guion bajo no se debe manipular 
        fuera de la clase(convención)
    """
    # variable de clase
    _encendido = False
    
    def enciende(self):
        # variable shadowing dos variables del mismo nombres que no están relacioandas
        self._encendido = True

    
    def apaga(self):
        self._encendido = False
        
    def isEncendido(self):
        return self._encendido

        """
            Herencia:
            Consiste en que una clase hereda 
            las propiedades y métodos de otra clase 
            
            También existen las herencias múltiples
            pero se considera una mala práctica hay que
            evitarla en la medida de lo posible
            
        """

class Dino(Juguete):
    color = None
    name = None
    
    def _init_(self, name):
        self.color = "Green"
        self.name = name
        print("Estoy en el constructor", name)
    
    def verEscamas(self):
        pass

p = Dino()
print(p.color)
print(p.name)



