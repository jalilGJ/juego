# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:46:34 2020

@author: jalil garcia jeronimo
"""

def jugar(intento=1):#Funcion recursiva 
    print("¿De que color es la naranja?")
    respuesta =str (input())
    if respuesta != "anaranjado": #condicion o caso base
        if intento < 3: 
            print ("\nFallaste! Inténtalo de nuevo") 
            intento += 1 
            jugar(intento)#se llama la funcion asi mismo,creando un buclea hasta llegar a igualar la condicion o funcion
        else: 
            print ("\nPerdiste!") 
    else:
        print ("\nGanaste!") 
jugar()#para comenzar el rpograma