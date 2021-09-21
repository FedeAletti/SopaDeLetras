# Se valida que N sea mayor = 15
def pedir_dato(N):
    if N >= 15:
        return N
    else: 
        # Se utiliza la recursividad para volver a pedir el dato y validarlo
        pedir_dato(int(input("ERROR, ingrese numero mayor o igual a 15: ")))
