# Texto a Numero

"""
Indica el numero en el alfabeto de cada letra en el texto que se pasa como parametro.
"""


def alphabet_position(text):
    alfabeto = ['@', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    texto = text.lower()
    lista = ''
    for i in texto:
        try:
            lista += (str(alfabeto.index(i))) + ' '
        except:
            continue

    return lista[0:-1]


print(alphabet_position('alejandro'))
