#      zona de codigos python


def pedir_cpu():
    c = float(input("uso de cpu "))
    return c

def procesar_cpu():
    peligro = 0
    mediciones = 0
    uso = pedir_cpu()

    while uso >= 0:
        mediciones = mediciones + 1
        if uso > 90:
            print("peligro uso critico")

            peligro = peligro + 1
        uso = pedir_cpu()
    return peligro , mediciones

def ver_cpu(peligro, mediciones):

    print("total de medicione", mediciones)
    print("Peligro critico", peligro)


#      codigo principal de python

peligro, mediciones = ver_cpu ()

ver_cpu = (peligro,mediciones)