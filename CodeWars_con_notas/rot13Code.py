# Codificación ROT13

"""
Ejercicio de Codificación del metodo rot13
"""


def rot13(message):
    texto = ''
    for i in message:
        if 65 <= ord(i) <= 90:
            x = ord(i) + 13
            if x > 90:
                x = x - 90 + 64
                texto += chr(x)
            else:
                texto += chr(x)
        elif 97 <= ord(i) <= 122:
            x = ord(i) + 13
            if x > 122:
                x = x - 122 + 96
                texto += chr(x)
            else:
                texto += chr(x)
        else:
            texto += i
    return texto


print(rot13("How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf."), "Ubj pna lbh gryy na rkgebireg sebz na\nvagebireg ng AFN? In the elevators,\nthe extrovert looks at the OTHER guy's shoes.")


# Mejor codigo.
# Existe metodo enconde para esto. :)


def rot13(message):
    return message.encode('rot13')
