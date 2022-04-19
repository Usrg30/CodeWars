# Paseo

"""
Ejercicio para validar si una paseo por un mapa, vuelve al punto de origen al finalizar
"""


def is_valid_walk(walk):
    ejex = 0
    ejey = 0
    count = len(walk)
    if count == 10:
        for x in walk:
            if x == 'n':
                ejex += 1
            if x == 's':
                ejex -= 1
            if x == 'w':
                ejey += 1
            if x == 'e':
                ejey -= 1
            else:
                pass
        if ejex == 0 and ejey == 0:
            return True
        else:
            return False
    else:
        return False


print(is_valid_walk(['n', 's', 'e', 'e', 'w', 's', 'e', 'w', 'n', 's']))


# Refactorización con el metodo count:
"""
Comparamos los norte y sur con este y oeste, para saber si son iguales, lo que significa que vuelve al origen.
"""


def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
