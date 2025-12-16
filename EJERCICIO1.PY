#        zona de codigos


def pedir():
    pedir = int(input(" digite la calificaion "))
    return pedir

def cantidad():
    c = int(input(" Cuantos pedidos son "))
    return c

def procesar(c):
    total = 0
    cont = 0   
    for n in range(c):
        print(" Calificacion del pedido:")
        cal = int(input("Del 1 al 5 "))  
        if cal > 5:
            cal = 5
        if cal < 1:
            cal = 1
        if cal == 5:
            print("Sobresaliente")  
        total = total + cal
        cont = cont + 1
    return total, cont

def calcular(total, cont):
    if cont > 0:
        promocion = total / cont
    else:
        promocion = 0
    return promocion

def ver(promocion):
    print("El resultado es:", promocion)

#      codigo prncipal python

producto = pedir()

c = cantidad()

total, cont = procesar(c)

promocion = calcular(total, cont)

ver (promocion)
