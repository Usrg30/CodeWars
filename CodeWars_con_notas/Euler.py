# Detecta los multiplos de 3 o 5 y los suma todos.

"""
El parametro a indicar el el numero final, iterando por todos y sumando los multiplos de 3 y 5.
"""

def solution(number):
    sum = 0
    for i in range(1, number):
        if i%3 == 0 or i%5 == 0:
            sum += i
        else:
            pass
    return sum

print(solution(10))


# Mejor codigo:

"""
sum() suma un iterable, por lo que se le pasa una lista comprimida creada con las condiciones
"""
def solution(number):
    return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])

