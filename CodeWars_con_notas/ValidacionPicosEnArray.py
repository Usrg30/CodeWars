# VAlidación de Picos en Array

"""
Funcion para determinar si es un pico o el inicio de una meseta
mucho cuidado con los comparativos, se descarta el inicio y el fin con el len()
luego si es menor que el anterio se descarta como pico, si es mayor se comprueba si tambien es mayor
que el sigiente y se suma al dicionario. si es igual, hay que verificar si es una meseta
recorriendo con un for el resto del array para determinar si es meseta de pico o no.
"""


def pick_peaks(array):
    len_array = len(array)
    pos = []
    peaks = []
    solution = {'pos': pos, 'peaks': peaks}

    for i in range(len_array):
        if i == 0 or i == len_array:
            continue
        try:
            if array[i] > array[i+1]:
                if array[i] > array[i-1]:
                    peaks.append(array[i])
                    pos.append(i)
                elif array[i] < array[i-1]:
                    continue
            elif array[i] < array[i-1]:
                continue
            elif array[i] == array[i-1]:
                continue
            else:
                for j in range(len_array):
                    if array[i] > array[i+j]:
                        peaks.append(array[i])
                        pos.append(i)
                        break
                    elif array[i] < array[i+j]:
                        break
                    else:
                        continue
        except:
            continue
    return solution


print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]))

# Refactorizar:
