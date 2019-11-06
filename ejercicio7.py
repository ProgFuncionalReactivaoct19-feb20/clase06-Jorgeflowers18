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
    
    # PREGUNTA DOS
    # copiamos la lista de la primera pregunta
    lista1 = list(filter(lambda x: len(list(x.items())[2][1]) > 10, data))
    # separamos por posiciones las fechas para ser ordenadas
    f = lambda x: list(x.items())[1][1].split("-")
    # creamos una lista con las cuales se pueda ordenar de acuerdo al día de nacimiento 
    lista2 = list(map(f, lista1))
    # imprimimos la lista ordenada de acuerdo al dia con un sorted y un key
    print(list(sorted(lista2, key = lambda x: x[2])))
    