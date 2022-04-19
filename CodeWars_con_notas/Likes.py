# Likes

"""
Crear un modelo como el las redes sociales, en cual segun el numero de likes
salgan ninguno, uno, dos, o tres nombres y a mayores el numero restante de likes
Se puede hacer con un swich tambien en vez de con if elif else.
"""


def likes(names):
    name_number = len(names)
    if name_number == 0:
        return "no one likes this"
    elif name_number == 1:
        return f"{names[0]} likes this"
    elif name_number == 2:
        return f"{names[0]} and {names[1]} like this"
    elif name_number == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names)-2} others like this"


print(likes(['paco', 'alex', 'manolo', 'tony']))



# Codigo con Swich:

def likes(names):
    swich = {
        0 : "no one likes this",
        1 : f"{names[0]} likes this",
        2 : f"{names[0]} and {names[1]} like this",
        3 : f"{names[0]}, {names[1]} and {names[2]} like this",
        4 : f"{names[0]}, {names[1]} and {len(names)-2} others like this"
    }
    return swich[len(names)]

print(likes(['paco', 'alex', 'manolo']))