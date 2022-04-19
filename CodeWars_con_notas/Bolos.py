# Marcador del juego de los bolos.

def bowling_score(rolls):
    lecturaultimajugada = rolls.split(' ')
    contadorUltimajugada = len(lecturaultimajugada[-1])
    x = ''.join(lecturaultimajugada)
    lista = [i for i in x]
    contador = 0
    ultimaTirada = len(lista) - contadorUltimajugada
    for j, x in enumerate(lista):
        if j == ultimaTirada:
            # Aqui se hacen las condiciones de la ultima tirada, ya que varian las normas un poco
            if lista[j] == 'X':
                contador += 10
                if lista[j+1] == 'X':
                    contador += 10
                    if lista[j+2] == 'X':
                        contador += 10
                    else:
                        contador += int(lista[j+2])
                elif lista[j+2] == '/':
                    contador += 10 - int(lista[j+1])
                    contador += int(lista[j+1])
                else:
                    contador += int(lista[j+1])
                    contador += int(lista[j+2])
                break

            else:
                contador += int(lista[j])
                try:
                    if lista[j+2] == '/':
                        contador += 10 - int(lista[j+1])
                        contador += int(lista[j+1])
                    elif lista[j+1] == 'X':
                        contador += 10
                        if lista[j+2] == 'X':
                            contador += 10
                        else:
                            contador += int(lista[j+2])
                    else:
                        if lista[j+1] == '/':
                            contador += 10 - int(lista[j])
                            if lista[j+2] == 'X':
                                contador += 10
                            else:
                                contador += int(lista[j+2])
                        else:
                            contador += int(lista[j+1])
                except IndexError:
                    contador += int(lista[j+1])
            break

        if x == 'X':
            contador += 10
            try:
                if lista[j+1] == 'X':
                    contador += 10
                    try:
                        if lista[j+2] == 'X':
                            contador += 10
                        else:
                            try:
                                contador += int(lista[j+2])
                            except:
                                continue
                    except:
                        continue
                else:
                    if lista[j+2] == '/':
                        contador += 10
                    else:
                        contador += int(lista[j+1])
                        contador += int(lista[j+2])
            except:
                continue
        elif x == '/':
            contador += 10 - int(lista[j-1])
            if lista[j+1] == 'X':
                contador += 10
            else:
                contador += int(lista[j+1])
        else:
            contador += int(lista[j])

    return contador


print(bowling_score('11 11 11 11 11 11 11 11 11 11'))
print(bowling_score('X X X X X X X X X XXX'))
print(bowling_score('5/ 4/ 3/ 2/ 1/ 0/ X 9/ 4/ 8/8')) # 150
print(bowling_score('00 00 00 00 00 00 00 00 00 0/X'))

"""
Este codigo es muy farragoso y nada practico, debido a las normas complejas de los bolos.
"""

# Refactorización del codigo:

def bowlingScore(frames):
    score, a, b = 0, 1, 1  # Asigna las variables.

    for final, j in enumerate(frames.rsplit(' ', 1)):
        for i in j.replace(' ', ''):
            ball = 10 if i == 'X' else 10 - ball if i == '/' else int(i)  # Separa los plenos y semiplenos y añade la puntuación.
            score += a * ball
            a, b = (b, 1) if final else (b + 1, 2) if i == 'X' else (b + 1, 1) if i == '/' else (b, 1)  # Puntua los tiros normales
    return score
