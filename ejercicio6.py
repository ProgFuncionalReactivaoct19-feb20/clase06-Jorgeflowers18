"""
    Clase 06: Funciones Puras y Efectos secundarios
    author: @Jorgeflowers18
"""
import csv

def lineasDiccionario(archivo):
    return csv.DictReader(archivo, delimiter = ';')
    
with open('data/data-estudiantes.csv') as midata:
    data = list(lineasDiccionario(midata))
    print(list(map(lambda x: x[0] + "%s" % " - " + x[1] , zip(list(map(lambda x: x.split(" ")[1], list(map(lambda x: list(x.items())[0][1], data)))) , list(map(lambda x: x.split(".")[0], list(map(lambda x: list(x.items())[1][1], data))))))))