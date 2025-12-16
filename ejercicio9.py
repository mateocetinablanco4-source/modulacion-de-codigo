#      zona de codigos de python


def pedir_vendido():
    v = int(input("Cantidad vendida hoy: "))
    return v

def procesar_inventario():
    stock = 50
    punto = 10

    vendido = pedir_vendido()

    while vendido >= 0:
        stock = stock - vendido

        if stock <= punto:
            print("Aviso de Reposición importante")

            break

        vendido = pedir_vendido()

    return stock

def ver_inventario(stock):

    print("Stock final:", stock)
    print(f"stock final :(stock)")

#   codigo principal de python
v = pedir_vendido()

stock_final = procesar_inventario()

ver_inventario(stock_final)