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