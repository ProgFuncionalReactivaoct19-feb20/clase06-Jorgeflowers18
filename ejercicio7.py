"""
    Clase 06: Funciones Puras y Efectos secundarios
    author: @Jorgeflowers18
"""
import csv

def lineasDiccionario(archivo):
    return csv.DictReader(archivo, delimiter = '\t')
    
with open('data/trabajadores.csv') as midata:
    data = list(lineasDiccionario(midata))
    # PREGUNTA UNO
    # se declara una funcion con la cual se seleccione los que tienen paises 
    # con una longiutd de mas de 10 caracteres con un filter y list para que
    # sea visible
    print(list(filter(lambda x: len(list(x.items())[2][1]) > 10, data)))
    print("\n")
    # PREGUNTA DOS
    # imprimimos la lista ordenada de acuerdo al dia de nacimiento con un sorted y un key
    print(sorted(list(filter(lambda x: len(list(x.items())[2][1]) > 10, data)), key = lambda x: list(x.items())[1][1].split("-")[2]))
    