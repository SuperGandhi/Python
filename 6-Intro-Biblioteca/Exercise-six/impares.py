def pares_impares(lista):
    '''Función que recibe una lista de números enteros y devuelve dos listas ordenadas con los números impares y pares de la lista dada.

    Parámetros:
        - lista: Es una lista de números enteros.
    Devuelve: Dos listas ordenadas con los números impares y pares de la lista dada.
    '''

    # Definimos dos listas vacías para guardar los números pares e impares.
    pares = []
    impares = []
    # Bucle para recorrer la lista de números.
    for i in lista:
        # Condicional para ver si el número es par o impar.
        if i%2 == 0:
            # Si el resto de la división entera por 2 es 0, el número es par y se añade a la lista de pares. 
            pares.append(i)
        else:
            # Si el resto de la división entera por 2 no es 0, el número es impar y se añade a la lista de impares.
            impares.append(i)
    # Ordenamos las listas.
    pares.sort()
    impares.sort()
    # Devolvemos las listas de pares e impares.
    return pares, impares

# Ejemplo
lista = [3, 8, 2, 7, 5, 4, 6, 1, 9]
pares, impares = pares_impares(lista)
print('Pares: ', pares)
print('Impares: ', impares)