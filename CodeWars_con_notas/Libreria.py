# Libreria

"""
Indica la suma de los numeros que se indican en el libro, se gun el indice de la primera letra
"""


def stock_list(listOfArt, listOfCat):
    if (len(listOfArt) == 0) or (len(listOfCat) == 0):
        return ''
    result = ''
    for cat in listOfCat:  # se itera sobre la lista de resultados pedido
        total = 0
        for book in listOfArt:  # cada libro se compara el codigo inicial con el de la lista que se pide
            if (book[0] == cat[0]):
                total += int(book.split(" ")[1])  # se suma al resultado y se formatea la str para que quede como se pide
        if (len(result) != 0):
            result += " - "
        result += "(" + str(cat) + " : " + str(total) + ")"
    return result



b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
print(stock_list(b, c))