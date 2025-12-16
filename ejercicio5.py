#        zoan de codigos python


def pedir_precio():
    p = float(input("precio del pro: "))
    return p

def pedir_cantidad():
    c = int(input("cantidad: "))
    return c

def procesar_compra():
    subtotal = 0
    seguir = input("añadir pro (si/no): ")

    while seguir != "no":
        precio = pedir_precio()

        cantidad = pedir_cantidad()

        subtotal = subtotal + (precio * cantidad)

        seguir = input("agregar otro pro (si/no): ")
    return subtotal
def calcular_descuento(subtotal):
    
    if subtotal > 1000:
        desc = subtotal * 0.10
    else:
        if subtotal > 500:
            desc = subtotal * 0.05
        else:
            desc = 0
    total = subtotal - desc
    return total, desc
def ver_total(total, desc):

    print("descuento aplicado:", desc)

    print("valor final a pagar:", total)

#      Codigo principal de python

subtotal = procesar_compra()

total, desc = calcular_descuento(subtotal)

ver_total(total, desc)