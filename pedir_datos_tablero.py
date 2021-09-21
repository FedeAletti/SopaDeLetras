from pedir_dato import pedir_dato
import math

# Se crea el array de palabras a encontrar y el nombre del archivo
listaPalabras = []
archivoNombre = ""

# Se pide el valor de N a utilizar para crear la matriz
N = pedir_dato(int(input("Ingresar un número mayor o igual a 15: ")))
# Se setea la cantidad de palabras
numeroDePalabras = math.floor(N / 3) - 1

def pedir_datos_tablero():

    for i in range(numeroDePalabras):

        palabra = (input("Ingresar las palabras: ").lower())
        if len(palabra) > (N / 3):
            print("la palabra no se puede incluir en la sopa de letras")
        elif palabra == "fin":
            break
        else:
            listaPalabras.append(palabra)

        print(listaPalabras)


def pedirNombreArchivo():
    archivoNombre = input("Nombre del archivo: ")
    if len(archivoNombre) <= 30:
        return archivoNombre
    else: pedirNombreArchivo("ERROR, el nombre del archivo es muy largo, intentar de nuevo: ")    
