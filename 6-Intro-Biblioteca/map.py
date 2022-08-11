"""
    Aplica una función a todos los elementos
    iterables
"""
# def cuadrado(x):
#     return x * x


result = map(lambda x: x*x, [1,2,3,4,5,6,7,8,9])
print(list(result))