# Elimina las marcas de las palabras

"""
Si la frase comienza con un elemento designado como marker, se omitira de la solución.
"""


def solution(string, markers):
    if string == '':
        return ''
    else:
        x = string.split('\n')
        y = []
        print(x)
        for i in x:  # cada elemento de la lista
            parrafo = ''
            for j in i:  # cada palabra de la lista
                if j in markers:
                    break
                else:
                    parrafo += j
            try:
                if parrafo == '':
                    y.append(parrafo)
                while parrafo[-1] == ' ':
                    parrafo = parrafo[:-1]
                else:
                    pass
                y.append(parrafo)
            except:
                pass

        return '\n'.join(y)


sol = (solution('apples lemons lemons\nwatermelons oranges pears avocados\n@ avocados watermelons # strawberries\n! bananas ,', ['@', '!']))
print(sol)

# Mejor Solución:


def solution(string, markers):
    parts = string.split('\n')  # lista que a posterior se modificara con for
    for s in markers:  # v.split(s)[0] recorta la string por (lo que hay entre parentesis) y 0 indica que permanece lo anterior [1] seria lo posterior.
        parts = [v.split(s)[0].rstrip() for v in parts]  # compresion de listas con rstrip() borra los espacios
    return '\n'.join(parts)  # union con join de la lista en string
