# Permutación de letras

"""
Permutar las letras de una palabra en sus posibles variaciones sin repetir.
"""

from itertools import permutations as perm
# permutacion ya imlementa la solucion en una funcion en la libreria etertools


def permutations(string):
    lista = [''.join(i) for i in perm(string)]  # compresion de lista de permutaciones.
    lista = set(lista)  # elimina los elementos repetidos en listas en caso de letras repetidas
    return lista


print(sorted(permutations('abba')))
