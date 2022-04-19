

def wave(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]

print(wave('laola'))

x = 'hola'
print(x[:3])  # rodaja del principio indica cuantas letras aparecen desde el inicio

print(x[1].upper()) # rodaja aislante de una sola con metodo

print(x[1:])    # rodaja hasta el final indica cuantas letras se quitan desde el principio

print(x[2:3])  # rodaja entre una y otra(combina tecnicas

# ojo con las rodajas