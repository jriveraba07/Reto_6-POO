# Ejercicio - 2

#* Una función que permita validar si una palabra es un palíndromo. 
#! Condición: 
#! No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

#* funcion 

def palindrome(x):
    T : bool = True
    n : int = len(x)
    for i in range(n//2):
        if x[i] != x[n-1-i]:
            return not T
    return T

#* Programa principal

stringp = str(input("ingrese una palabra para saber si es palindrome: "))
y = palindrome(stringp)

#* salida

print(f"¿es '{stringp}' palindromo ? {y}")    
