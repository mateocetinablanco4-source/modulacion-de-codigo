#zona de codigos python

def pedir():
    h = int(input("Horas de mas trabajadas: "))
    return h

def procesar():
    total = 0
    emp = 0
    horas = pedir()
    
    while horas >= 0:
        if horas > 5:
            bono = horas * 15
            total = total + bono
            emp = emp + 1
        else:
            if horas > 0:
                bono = horas * 10
                total = total + bono
                emp = emp + 1
        horas = pedir()
    return total, emp
def mostrar(total, emp):

    print("Bonificacion total:", total)

    print("Empleados con bonificacion:", emp)

#codigo principal de python

total, emp = procesar()

mostrar(total, emp)