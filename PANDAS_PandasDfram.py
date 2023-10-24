import pandas as pd
import random 
SEPARADOR = ("*" * 20) + "\n"

#Creacion de un DataFrame a partir de un diccionario 
diccionario_notas_aleatorias = { \
     "Crescencio":[random.randrange(60,101) for x in range(3)], \
     "Domitila":[80,100,57], "Rutilio":[80,70,57], "Panfilo":[20,100,100], \
     "Ludoviko":[100,100,100]}
notas_diccionario = pd.DataFrame(diccionario_notas_aleatorias)
notas_diccionario.index =  ["Programacion", "Base de datos", "Contabilidad"]

#Accesar los datos de un DF mediante una columna, recordar que cada columna es una Serie
print(notas_diccionario ["Domitila"])
print()
print(notas_diccionario.Domitila) 
print(SEPARADOR)

#Accesar los datos de un DF en un renglon
print(notas_diccionario.loc["Programacion"])
print()
print(notas_diccionario.loc["Base de datos"])
print()
print(notas_diccionario.loc["Contabilidad"])