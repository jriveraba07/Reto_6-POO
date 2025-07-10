# Ejercicio - 3

#* Función que reciba una lista de números y devuelva solo aquellos que son primos.
#* La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

import math

#* funciones

def ingresa_lista(mensaje):
        s = input(mensaje)
        s = s[1:-1]
        l = s.split(",")
        return [int(i) for i in l]
    

def es_primo(x):
    try:
        T : bool = True
        if x <= 1:
            return not T
        elif x == 2:
            return T
        else:
            for i in range(2, int(math.sqrt(x))):
                if x % i == 0:
                    return not T
                else: 
                    continue 
        return T
    except TypeError:
        return f"no ingresaste bien el dato, debe ser numerico!!!"

def lista_primo(x): 
    d = []
    for i in range(len(x)):
        if es_primo(x[i]):
            d.append(x[i])
        else: 
            continue    
    return d #La funcion se puede simplificar en: return [i for i in x if es_primo(i)]

#* programa principal

try:

    lista = ingresa_lista("Introduce la lista para tener los primos: ")
    y = lista_primo(lista)

    #* salida

    print("los primos en la lista son:", y)  

except Exception as e:
    print(f"hay un error tipo <{e}>, recuerda la lista con corchetes y con comas entre elementos, los elementos deben ser unicamente enteros")

    