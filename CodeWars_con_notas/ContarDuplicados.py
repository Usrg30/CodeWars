# Cuenta los cuplicados:

# Indica cuantas letras estan duplicadas en una string

def duplicate_count(text):
    text1 = text.lower()
    repeat = ''
    for i in text1:
        x = text1.count(i)
        if x >= 2:
            repeat += i
        else:
            continue
    return len(set(repeat))

print(duplicate_count("abcdeaB"))

# Mejor codigo:
"""
Mediante compresión de listas es mas limpio el codigo, en este caso se crea una lista con
la string en formato set, para indicar las letras unicas, y solo se añaden mediante el control if
que si estan presentes en mas de una ocasión, se añaden a la lista. Con len se cuentan cuantas hay.
Tambien se pueden obtener que letras se repiten, quitando el len.
"""

s = 'abcdeaB'

def duplicate_count(s):
  return len([i for i in set(s.lower()) if s.lower().count(i)>1])



# Codigo intermedio antes del final

y = []  # lista las letras repetidas

x = [i for i in set(s.lower()) if s.lower().count(i)>1]
for i in set(s.lower()):  # el for itera sobre las letras unicamente
    if s.lower().count(i)>1:  # esto añade a la lista solo las letras que se cuenten en mas de una ocasion en la string original.
        y.append(i)  # añade a la lista

print(y)  # letras repetidas
print(len(y))  # cuantas letras repetidas hay










