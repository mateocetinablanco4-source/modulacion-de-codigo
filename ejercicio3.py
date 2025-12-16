#       Zona de codigos python


def pedir():
 t = input("Tipo D deposito R retiro o FIN: ")
 return t

def cantidad():
    m = float(input("CANTIDAD "))
    return m

def calcular():

    saldo = 1000
    trans = 0
    tipo = pedir()

    while tipo != "FIN":
        if tipo == "D":
            m = cantidad()

            saldo = saldo + m
            trans = trans + 1
        else:
            if tipo == "R":
                m = cantidad()
                if saldo - m >= 0:
                    saldo = saldo - m
                    trans = trans + 1
                else:
                    print("no se puede retirar, saldo no alcanzado ")
            else:
                print("Dato no valido")

        tipo = pedir()
    return saldo, trans
def ver(saldo, trans):

    print("saldo final:", saldo)
    print("transacciones validas:", trans)

#     Codigo principal de python

saldo, trans = calcular ()

ver(saldo, trans)

