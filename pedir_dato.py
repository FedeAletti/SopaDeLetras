def pedir_dato(N):
    if N >= 15:
        return N
    else: 
        pedir_dato(int(input("Error, ingrese numero mayor o igual a 15: ")))
