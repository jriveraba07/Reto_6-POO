# Ejercicio - 1

#* Una funcion que realice operaciones basicas:
#* (suma, resta, multiplicacion, division) entre dos numeros segun la eleccion del usuario, 
#* La forma de entrada de la función será los dos operandos y el caracter usado para la operación.
#* Ej: entrada: (1,2,"+"), salida (3).

#* Función 

def operacion_basica(a, b, operacion):
    if operacion == "+": 
        return a + b
    elif operacion == "-":
        return a - b
    elif operacion == "*":
        return a * b
    elif operacion == "/":
        return a / b
    else:
        return "caracter no valido"

#* programa principal

try:
    x = float(input("introduce el primer numero: "))
    y = float(input("introduce el segundo numero: "))
    operador = str(input("introduce la operación a realizar (+, -, *, /): "))
    resultado = operacion_basica(x, y, operador)

    #* salida

    print("el resultado es:", resultado)
except Exception as e:
    print(f"hay un error tipo '{e}', recuerda poner los datos como se piden")
    