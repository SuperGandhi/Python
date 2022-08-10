# number = 321
# text = "hi"
# floatt = 1.2


# def sum(a,b):
#     return a + b
# txt = f'El numero es {sum(number,number)} y el texto es {text.upper()} y el float es {floatt}'
# print(txt)


class Juguete:
    nombre= ''
    precio= 0.0
            
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
    
    # def __str__(self):
    #     return f'My name is {self.name} and the price is {self.price}'
    
    
        
j1 = Juguete('Potato',19.5)
print(j1)

