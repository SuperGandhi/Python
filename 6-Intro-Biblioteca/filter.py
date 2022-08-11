
"""
    Filter aplica una función a todos los elementos
    de una lista que devuelve true o false, si devuelve
    true filter guarda el valor caso contrario no devuelve
    el valor
"""
number = [1,2,4,5,6,7,8,9,10]

def main(x):
    if x % 2 == 0:
        return True
    return False



result = filter(lambda x: x % 2 == 0, number)
print(list(result))


def main_characters(x):
    if str(x).startswith('pep'):
        return True
    return False



result = filter(lambda x: str(x).startswith('pep'), ['pep', 'pedro', 'pablo'])
print(list(result))