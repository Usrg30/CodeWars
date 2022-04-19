# Crea los posibles Anagramas de una palabra, sin repetir palabras.

def anagrams(palabra, palabras):
    lista = []
    x = palabra
    for y in palabras:
        if len(x) != len(y):
            pass
        elif sorted(x) == sorted(y):
            lista.append(y)
        else:
            pass
    return lista

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))

"""
Anagramas, en este caso comprabamos la longitud de las palabras lo primero,
lo segundo ordenamos las palabras, si son anagramas el algoritmo de ordenación debe ser el mismo.
se usa comparador logico y se concluye.
"""

# Refactorización de codigo:
def anagrams(palabra, palabras):
    return filter(lambda x: sorted(palabra) == sorted(x), palabras)