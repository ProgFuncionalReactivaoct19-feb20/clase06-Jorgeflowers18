"""
    Clase 06: Funciones Puras y Efectos secundarios
    author: @Jorgeflowers18
"""
import csv

def lineasDiccionario(archivo):
    return csv.DictReader(archivo, delimiter = ';')
    
with open('data/data-estudiantes.csv') as midata:
    print(list(map(lambda x: list(x.items())[0][1],list(lineasDiccionario(midata)))))