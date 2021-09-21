# from pedir_datos_tablero import pedir_datos_tablero, N 
# import random


# def generar_tablero(fila, col):
 
#     for i in range(fila):
#         listaFila = []        
#         for j in range(col):
#             listaFila.append(random.choice("abcdefghijklmnopqrstuvwxyz"))
#         matriz.append(listaFila)
            
#     return matriz


# matriz = []
# generar_tablero(N,N)


# ____________________________________________________________________________
from pedir_datos_tablero import pedir_datos_tablero, N, lista_palabras

import random 
import string

tableroTamaño = N
palabras = lista_palabras

tablero = [['_' for _ in range (tableroTamaño)] for _ in range(tableroTamaño)]

def generar_tablero():

    orientaciones = ['izquierda', 'arriba']

    for palabra in palabras:
        tamanioPalabra = len(palabra)

        # El estado es no ubicado por defecto
        ubicado = False 

        # Mientras ubicado sea false
        while not ubicado:

            #Probar con una orientacion random de la lista de orientaciones
            orientacion = random.choice(orientaciones)

            if orientacion == 'izquierda':
                # Izquierda a derecha
                paso_x = 1
                paso_y = 0
            if orientacion == 'arriba':
                # Arriba a abajo
                paso_x = 0
                paso_y = 1

            # Aca se elige la posición inicial de la palabra
            # Ubica entre posicion 0 y el ancho/alto de la matriz
            x_position = random.randint(0, tableroTamaño)
            y_position = random.randint(0, tableroTamaño)

            # Ver si se puede insertar en esa posición:
            ending_x = x_position + tamanioPalabra * paso_x
            ending_y = y_position + tamanioPalabra * paso_y

            if ending_x < 0 or ending_x >= tableroTamaño: continue
            if ending_y < 0 or ending_y >= tableroTamaño: continue

            # Estado de fallo al ubicar en falso por defecto
            falloAlUbicar = False

            for i in range(tamanioPalabra):
                caracter = palabra[i]
                
                # Asignando al caracter en una nueva posición
                new_position_x = x_position + i * paso_x
                new_position_y = y_position + i * paso_y

                # Ubicando caracter en fila - columna dentro de la matriz
                nueva_posicion_caracter = tablero[new_position_x][new_position_y]

                # Revisa no pisar otro caracter / salirse del tablero
                if nueva_posicion_caracter != '_':
                    if nueva_posicion_caracter == caracter: continue
                else:
                    falloAlUbicar = True
                    break
            
            if falloAlUbicar:
                continue
            else:
                for i in range(tamanioPalabra):
                    caracter = palabra[i]

                    new_position_x = x_position + i * paso_x
                    new_position_y = y_position + i * paso_y

                    tablero[new_position_x][new_position_y] = caracter
                # Cambio de estado de Ubicado a true para finalizar bucle
                ubicado = True
            






        # for x in range(tableroTamaño):
        #     print (' '.join(tablero[x]))
    return tablero
    
# Reemplazo de espacios por letras en random
for x in range(tableroTamaño):
    for y in range(tableroTamaño):
        if (tablero[x][y] == '_'):
            tablero[x][y] = random.choice("abcdefghijklmnopqrstuvwxyz")
# Orientacion

#Impresion
# generar_tablero()