
# si una condición es cierta me devuelve true
list_a =  [1 == 1 , 2 == 1, 3 == 1]
res =  any(list_a)
print(res)

# con all todas deben ser ciertas
list_b =  [1 == 2 , 5 == 1, 6 == 1]
res =  all(list_b)
print(res)