'''Escribir una función que lea dos ficheros csv con una lista larga de datos de personas (50 personas y 1000 personas) y llame a dos funciones que pongan su nombre en formato capitalizado y calculen la letra de DNI correspondiente. Realiza la comprobación de rendimiento con la librería cProfile y muestra los datos. Describe que indica cada dato que nos proporciona cProfile.
Solución / Datos cProfile
'''
import csv
import cProfile

def datos(nombre):
    return nombre.title()

def letra_dni(dni_numero):
    letras = "ABCDEFGHIJKLMNÑOPQRSTUV"
    return letras[(dni_numero + 1) % 23]

def procesar_csv(nombre_archivo):
    personas = []
    
    with open():

        for
    
    return


def main():
    personas_50 = procesar_csv("personas_50.csv")
    personas_1000 = procesar_csv("personas_1000.csv")
    
    print(f"Datos 50 personas: {personas_50}")  # 
    print(f"Datos 1000 personas: {personas_1000}")  # 

if __name__ == "__main__":
    cProfile.run('main()')