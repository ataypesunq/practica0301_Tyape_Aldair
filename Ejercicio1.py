'''Escribir dos funciones, una función que reciba un número entero positivo n y calcule el número de fibonacci asociado a ese número de manera recursiva y otra función que haga la misma operación pero con bucles.
Con ambas funciones, calcular y comparar el tiempo de ejecución para n = (1, 10, 20, 30 y 40) por fuerza bruta.
'''
import datetime
def recursiva(n):
    '''Esta función recibe el numeroentero positivo y calcula el numero de fibonacci de forma recursiva.
    Parametros:
        - n: numeor entero positivo
    Return:
        - Devuelve el numero de fibonacci q corresponde a n.
    '''
    if n <= 1:
        return n
    return recursiva(n - 1) + recursiva(n - 2)

def iterativa(n):
    '''Esta función recibe el numeroentero positivo y calcula el numero de fibonacci de forma iterativa.
    Parametros:
        - n: numeor entero positivo
    Return:
        - Devuelve el numero de fibonacci que corresponde a n.
    '''
    if n <= 1:
        return n
    a = 0
    b = 1
    numero = 2
    while numero <= n:
        a = b
        b = a + b
        numero += 1
        return b

if __name__ == "__main__":
    valores_n = [1, 10, 20, 30, 40]
    print(f"n    Recursivo     Iterativo")

    for n in valores_n:
        start_time = datetime.datetime.now()
        recursiva(n)
        end_time = datetime.datetime.now()
        compar1_recursivo = (end_time - start_time)

        start_time = datetime.datetime.now()
        iterativa(n)
        end_time = datetime.datetime.now()
        compar2_iterativo = (end_time - start_time)

        print(n, compar1_recursivo, compar2_iterativo)