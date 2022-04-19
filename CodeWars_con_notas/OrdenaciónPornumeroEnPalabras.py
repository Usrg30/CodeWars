# Ordenación por Numeros en Palabras

"""
Ordena las palabras segun el numero que figure en la misma.
"""


def order(sentence):
    lista = sentence.split()
    orden = ''
    for j in range(1, 10):
        for i in lista:
            if str(j) in i:
                orden += i + ' '
    return orden[0:-1]


print(order("todo2s som1os l4a p3ces e5n l6a mar7"))
