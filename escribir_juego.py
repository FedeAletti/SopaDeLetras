from pedir_datos_tablero import *
from generar_tablero import generar_tablero, tablero

# N = 15
# archivo_nombre = "PEdro"
pedir_datos_tablero()
generar_tablero()
import csv
celdas = []
soluciones = []
archivo_nom = pedirNombreArchivo()

for i in range(N):
    colNum = str(i)
    celdas.append("Col" + colNum)

for i in range(len(lista_palabras)):
    palNum = str(i)
    soluciones.append("Palabra" + palNum)


with open(archivo_nom + ".csv","w", newline='') as csvfile:
    #fieldnames = celdas    
    writer = csv.writer(csvfile, delimiter="|")

    #writer.writeheader()
    writer.writerow(celdas)
    writer.writerows(tablero)

with open(archivo_nom + "_solucion" + ".csv","w", newline='') as csvfile:
    #fieldnames = celdas    
    writer = csv.writer(csvfile, delimiter="|")

    #writer.writeheader()
    writer.writerow(soluciones)
    writer.writerow(lista_palabras)
                      
