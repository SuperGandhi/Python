# Sorted se usa para ordenar listas

list = ['g', 'r', 'q', 'z']
order = sorted(list, reverse=True, key= lambda x: str(x).startswith('z'))
print(order)