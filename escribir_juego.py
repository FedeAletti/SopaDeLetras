from pedir_datos_tablero import *
from generar_tablero import generar_tablero, tablero

# N = 15
# archivo_nombre = "PEdro"
pedir_datos_tablero()
generar_tablero()
import csv
celdas = []


for i in range(N):
    colNum = str(i)
    celdas.append(colNum)


with open(pedirNombreArchivo() + ".csv","w", newline='') as csvfile:
    #fieldnames = celdas    
    writer = csv.writer(csvfile, delimiter="|")

    #writer.writeheader()
    writer.writerow(celdas)
    writer.writerows(tablero)
                      
