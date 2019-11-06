"""
    Clase 06: Funciones Puras y Efectos secundarios
    author: @Jorgeflowers18
"""
import csv

def lineasDiccionario(archivo):
    return csv.DictReader(archivo, delimiter = '\t')
    
with open('data/trabajadores.csv') as midata:
    data = list(lineasDiccionario(midata))
    
    # Primera pregunta
    # se declara una funcion con la cual se seleccione los que tienen paises 
    # con una longiutd de mas de 10 caracteres con un filter y list para que
    # sea visible
    f = lambda x: len(list(x.items())[2][1]) > 10
    print(list(filter(f, data)))
   