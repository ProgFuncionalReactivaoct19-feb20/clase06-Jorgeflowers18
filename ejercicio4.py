"""
    Clase 06: Funciones Puras y Efectos secundarios
    author: @Jorgeflowers18
"""
import csv

def lineas(archivo):
    return csv.reader(archivo, delimiter = ';')
    
with open('data/data-estudiantes.csv') as midata:
    print(list(map(lambda x: x[1], filter(lambda x: x[1] !="email", list(lineas(midata))))))




