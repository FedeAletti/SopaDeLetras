from pedir_dato import pedir_dato
import math

lista_palabras = []
N = pedir_dato(int(input("Ingresar un número mayor o igual a 15: ")))
numero_de_palabras = math.floor(N / 3) - 1

def pedir_datos_tablero():

    for i in range(numero_de_palabras):

        palabra = input("Ingresar las palabras: ")
        if len(palabra) > (N / 3):

            print("la palabra no se puede incluir en la sopa de letras")
        elif palabra == "fin":
            break

        else:
            lista_palabras.append(palabra)

        print(lista_palabras)

    def pedirNombreArchivo():
        archivo_nombre = input("Nombre del archivo: ")
        if len(archivo_nombre) <= 30:
            archivo = open(archivo_nombre + ".csv","w")
        else: pedirNombreArchivo() 
        archivo.close 
            
    pedirNombreArchivo()


pedir_datos_tablero()