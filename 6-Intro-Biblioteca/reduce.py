from functools import reduce
"""
    Ejecutar de forma recursiva una función
    sobre la lista hasta que la lista se quede
    con un único elemento
"""

# def sum(a,b):
#     return a + b


res = reduce(lambda a,b: a + b, [1,2,3,4,5,6,7,8,9,10])
print(res)