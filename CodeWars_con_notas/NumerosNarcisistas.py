# Los numeros Narcisistas

"""
Ejercicio sobre saber si un numero es narcisista
(si se eleva cada digito a la potencia del numero de digitos y se suman es el numero),
importante los operadores matematicos y los comparativos de bits ** es potencia en python ^ compara bits.
"""


def narcissistic(value):
    valor = 0
    x = [int(a) for a in str(value)]
    digits_number = len(x)
    for i in x:
        valor += i**digits_number
    return valor == value


print(narcissistic(371))
