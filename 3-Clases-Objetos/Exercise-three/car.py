class Vehiculo():
    
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        
    def __str__(self):
        return "color {}, {} ruedas, {} puertas".format( self.color, self.ruedas, self.puertas )
        
        
class Coche(Vehiculo):
    
    def __init__(self, color, ruedas,puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)  # utilizamos super() sin self en lugar de Vehiculo
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)
    
c= Coche('blue', 150, 5, 1200)
print(c)