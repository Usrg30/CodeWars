# Pasar Segundos a Formato legible(ampliado)

"""
Pasa segundos a años dias horas minutos y segundos.
Si el numero no es grande, no indicara el elemento al que no llegue.
"""


def format_duration(seconds):
    words = ["year", "day", "hour", "minute", "second"]

    if not seconds:
        return "now"
    else:
        m, s = divmod(seconds, 60)  # divmod cociente y resto, en este caso lo usamos para filtrar los 60 seg min etc
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        y, d = divmod(d, 365)

        time = [y, d, h, m, s]

        duration = []

        for x, i in enumerate(time):  # enumerate obtiene el indice y el elemento de la lista
            if i == 1:
                duration.append(f"{i} {words[x]}")  # esto combina la palabra con el numero obtenido
            elif i > 1:
                duration.append(f"{i} {words[x]}s")

        if len(duration) == 1:
            return duration[0]
        elif len(duration) == 2:
            return f"{duration[0] and duration[1]}"
        else:
            return ", ".join(duration[:-1]) + " and " + duration[-1]


print(format_duration(3662))
