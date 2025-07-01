# Ejercicio - 5

#* hacer un programa Escribir una función que reciba una lista de string y retorne 
#*  unicamente aquellos elementos que tengan los mismos caracteres.
#*  e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]

#* funciones

def ingresa_listas(mensaje):
    s = input(mensaje)
    s = s[1:-1]
    l = s.split(',')
    return [str(i) for i in l]

def separa_caracteres(x):
    s = [str(i) for i in x]
    return s

def compara_strings(x, y):
    s1 = separa_caracteres(x)
    s2 = separa_caracteres(y)
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

def impresor(x):
    n = len(x)
    if n == 0:
        return []
    elif n == 1:
        return x[0]
    else:
        k = x[n-1]
        for i in x[:-1]:
            print(i)
        return k

def devuelve_strings(x):
    k = x.copy()
    f = []
    for i in k:
        d = []
        if len(k) <= 1:
            break
        elif i not in k:
            continue
        else:
            for j in k:
                if compara_strings(i, j):
                    d.append(j)
            if len(d) == 1:
                k.remove(i)
            else:
                k = [i for i in k if i not in d]
                f.append(d)
    return impresor(f)

#* programa principal

A = ["amor", "roma", "perra", "menso", "mora", "ramo", "rrepa"]
y = devuelve_strings(A)

#* salida

print(y)




            