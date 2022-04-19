# Validación de IP

"""
Forma poco practica de obtener la validación del formato IP
"""

def is_valid_IP(strng):
    x = strng.split('.')
    if len(x) != 4:
        return False
    else:
        for i in x:
            try:
                if int(i) > 255 or int(i) < 0:
                    return False
                if ' ' in i:
                    return False
                if len(i) > 1 and i[0] == '0':
                    return False
                else:
                    continue
            except:
                return False
    return True



print(is_valid_IP('195.156.05.0'))


# Mejor Codigo:  (expresiones regulares)

"""
Mejores practicas usar REGEX
"""

import re
def is_valid_IP(strng):
    return bool(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}(?=$)', strng))
