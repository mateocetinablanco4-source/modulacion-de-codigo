#        codigo principal de python


def pedir_venta():
    v = float(input("monto de venta del vendedor"))
    return v

def procesar_ventas():

    meta = 5000
    cumplidos = 0
    total = 0
    venta = pedir_venta()

    while venta > 0:
        total = total + 1
        if venta >= meta:
            cumplidos = cumplidos + 1
            print("met cumplida")
        venta = pedir_venta()

    return cumplidos, total

def ver_ventas(cumplidos, total):

    print("vendedores con finalidad cumplida", cumplidos)
    print("total de vendedores procesados", total)

#       codigo principal de python

c, t = procesar_ventas()

ver_ventas(c, t)