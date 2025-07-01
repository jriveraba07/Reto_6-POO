# Ejercicio - 4

#* Función que reciba una lista de números enteros 
#* Y retorne la mayor suma entre dos elementos consecutivos.

#* funciones

def ingresa_lista(mensaje):
    s = input(mensaje)
    s = s[1:-1]
    l = s.split(",")
    return [int(i) for i in l]

def lista_num(x):
    for i in range(len(x) - 1):
        if i == 0:
            v = x[i] + x[i + 1]
            u = i
        elif x[i] + x[i + 1] > v and i != 0:
            v = x[i] + x[i + 1]
            u = i
    return v, u, u + 1
    
        
#* programa principal

try:
    lista = ingresa_lista("Ingresa lista (entre corchetes y separado por comas) para saber su mayor suma con dos numeros seguidos: ")

    while len(lista) == 1:
        lista = ingresa_lista("La lista solo posee un elemento, vuelve a ingresar: ")

    y, p, f = lista_num(lista)

    #* salida

    print("La suma mas alta es", y, "con los numeros con posición en", p, "y", f, "(comenzando desde 0)")
except Exception as e:
    print(f'"hay un error tipo <{e}>, recuerda la lista con corchetes y con comas entre elementos,
           los elementos deben ser unicamente enteros y la lista no debe estar vacia"')