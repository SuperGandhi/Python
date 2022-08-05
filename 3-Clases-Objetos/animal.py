from abc import ABC, abstractmethod

"""
    La clase abstracta define un conjunto
    de funciones comunes a otras clases
    
"""
class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass
    
