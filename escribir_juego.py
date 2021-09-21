from pedir_datos_tablero import *
from generar_tablero import generar_tablero, tablero, ubicacionSolucion
import csv

pedir_datos_tablero()
generar_tablero()
celdas = []
soluciones = ubicacionSolucion
nombreArchivo = pedirNombreArchivo()

for i in range(N):
    celdas.append("Col" + str(i+1))
    

with open(nombreArchivo + ".csv","w", newline='') as csvfile:
   
    writer = csv.writer(csvfile, delimiter="|")
    writer.writerow(celdas)
    writer.writerows(tablero)

with open(nombreArchivo + "_solucion" + ".csv","w", newline='') as csvfile:
        
    writer = csv.writer(csvfile)
    writer.writerows(soluciones)
                      
