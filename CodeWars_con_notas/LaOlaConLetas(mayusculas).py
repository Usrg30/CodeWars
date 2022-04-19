# Problema de la ola

"""
Forma poco practica.
"""

def wave(people):
    x = people
    r = len(x)
    y = ''
    v = 0
    list = []
    for j in range(0, r):
        if x[j] == ' ':
            v += 1
            pass
        else:
            for i in range(0, r):
                if x[i] == ' ':
                    y += ' '
                elif i == v:
                    y += (x[i].upper())
                else:
                    y += (x[i])
            v += 1
            list.append(y)
            y = ''

    return list


print(wave('pa aw'))
"""
el problema es la anidación de bucles y la iteración de las letras
tambien el hecho de omitir los espacios, mediante un control de flujo entre bucles
importante atención al control mediante contador de v
"""

# Mejor Codigo

def wave(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]

