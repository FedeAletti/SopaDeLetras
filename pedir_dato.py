def pedir_dato(n):
    if n >= 15:
        return n
    else: 
        pedir_dato(int(input("Error, ingrese numero mayor o igual a 15: ")))
