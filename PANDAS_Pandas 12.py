import numpy as np
import pandas as pd 

SEPARADOR = ("*" * 20) + "\n"

#Crear una serie con valores iniciales 
notas = pd.Series([87, 100, 85, 60, 78])
print(type(notas))
print(notas)
print(SEPARADOR)



#Crea una serie de 6 elementos que tengan el mismo valor 
iguales = pd.Series(100, range(6))
print(type(iguales))
print(iguales)
print(SEPARADOR)



#Estadistica descriptiva para una serie 
print("notas :")
print(f"{notas}")
print(f"cantidad = {notas.count()}")
print(f"media = {notas.mean()}")
print(f"mínimo = {notas.min()}")
print(f"máximo = {notas.max()}")
print(f"desviación standar = {notas.std()}")
print("Sumarizacion descriptiva:")
print(notas.describe())
print(SEPARADOR)



#Serie con indices personalizados 
print("Series con indices personalizados:")
notas_asignadas = pd.Series([87, 100, 85, 60, 78], index=["Crescencio", "Domitilo", "Rutilio", "Panfilo", "Ludoviko"])

print(notas_asignadas)
print(SEPARADOR)




print("Series generada a partir de un diccionario")
notas_asignadas_dict = pd.Series({"Crescencio":87, "Domitila":100, "Rutilio":85, "Panfilo":60, "Ludoviko":78})

print(notas_asignadas_dict)
print(SEPARADOR)





#Acceso a elementos en una serie por valores de indices 
print(f"La calificacion de Rutilio es {notas_asignadas_dict['Rutilio']}")
print(f"La calificacion de Rutilio es {notas_asignadas_dict.Rutilio}")