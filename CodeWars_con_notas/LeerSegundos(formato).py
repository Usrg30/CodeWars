# Segundos a Formato Humano legible

"""
360s son 6 minutos /60
3600s son 60 min es dicir una hora /60
con f"" permite añadir las variables a la string con los {} y dentro el nombre de la variable.
f"{HH:0>2d}:{MM:0>2d}:{SS:0>2d}" dar formato a los digitos con f"
con .format() seria {:02}.format(HH) z = "{:02}:{:02}:{:02}".format(HH,MM,SS)
"""

def make_readable(seconds):
    HH = seconds // 3600
    MM = seconds // 60 - (HH * 60)
    SS = seconds % 60
    return "Segundos excedidos" if seconds > 359999 else f"{HH:0>2d}:{MM:0>2d}:{SS:0>2d}"

print(make_readable(6547))


