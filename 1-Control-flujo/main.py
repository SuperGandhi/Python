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

for numero in range(2,7):
    print(numero)
    
listillo = len(lista)
print('The list have' ,listillo , 'items')