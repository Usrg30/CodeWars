# Convierte un binario en entero.


def binary_array_to_number(arr):
    binario = ''
    for i in arr:
        binario += str(i)
    return int(binario, 2)  # el segundo argumento de int es la base, para binario 2 octal 8 ect

print(binary_array_to_number([1, 1, 0, 1]))