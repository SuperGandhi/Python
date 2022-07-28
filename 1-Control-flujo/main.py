# Test de veracidad
"""
Operadores condicionales
    > Mayor
    >= Mayor igual
    == Igual
    < Menor
    <= Menor Igual
    
"""
a = 5
b = 5
c = 10

"""
    AND
    T T = T
    T F = F
    F T = F 
    F F = F

"""

result = (a > 5 and c > 7)
#          false and true = false
print(result)

"""
    OR
    T T = T
    T F = T
    F T = T 
    F F = F

"""
result = a < 5 or c <7
print(result)


"""
    XOR o exclusivo
    T T = F
    T F = T
    F T = T 
    F F = F

"""

result = a < 5 ^ c < 7;
print(result)


a = 10
b = 20
c = 30

# a > b
# a < b and b < a or a > b and b > a
# SOlo se ejecutun las condiciones cuando son verdaderas
# if a >= 10 and c >= 30:
#     print('Diez es mayor igual y treinta es mayor igual')
# elif b >= 20:
#     print("A es mayor o igual que 6")
# else:
#     print('NO SE CUMPLE NINGUNA CONDICIÓN')
# print('F')

contador = 0
"""
        What's is the difference between break 
        and continue:
        Continue jump of the next iteration 
"""
while contador <= 10:
        print('Contador vale: ', contador)
        contador += 1
        continue

print('END WHILE')

lista = [1,2,3,4,5,6,7]
tupla = (1,2,3,4,5,6,7)

# for current_value in tupla:
#     print(current_value)

# for numero in range(2,7):
#     print(numero)
    
# listillo = len(lista)
# print('The list have' ,listillo , 'items')

# lista = ['hi', 'bye', 'message']

# if 'message' not in 'lista':
#     print('Yes I find the word')

lista = [4,5,6,1,10,12,3]
list_alphabet = ['A','b','Z','y','S','q','W','r']
print(lista)

list_order = sorted(lista)
list_order = sorted(lista, reverse=True)
list_alphabet = sorted(list_alphabet)
print(list_order)
print(list_alphabet)

# la palabra reservada math actua como un "switch" está se encuentra
# disponible a partir de la versión 3.10 de python 

# value = 10

# math value:
#         case 1:
#             print('Value is one')
#         case 2:
#             print('Value is two')
#         case 3:
#             print('Value is three')
#         case 4:
#             print('Value is four')
#         case 5:
#             print('Value is five')
            
list = ['hi', 'bye', 'message']

for word in lista:
    # para dejar declarada una función o bucle, esto también para que no nos tire un error al tener 
    # un espacio en blanco o vacio
    pass 
    # las variables solo se pueden usar dentro de un bucle y su hijo 
    temporal = False
    if word == "message":
        print('Find the word message')
        break

print(list)