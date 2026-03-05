# ejercio diez definicion de bloques de codigo reutilizables con (def)

# Definir una función que suma dos números
def sumar(a, b):
    # Retornar la suma de los dos valores
    return a + b


# Definir una función que verifica si un número es par
def es_par(numero):
    # Verificar si el residuo de la división entre 2 es cero
    if numero % 2 == 0:
        return True
    else:
        return False


# Programa principal

# Solicitar dos números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Llamar la función sumar y guardar el resultado
resultado_suma = sumar(num1, num2)

# Mostrar el resultado de la suma
print("La suma es:", resultado_suma)


# Solicitar un número para verificar si es par
numero_verificar = int(input("Ingrese un número para verificar si es par: "))

# Llamar la función es_par y mostrar el resultado
if es_par(numero_verificar):
    print("El número es par.")
else:
    print("El número es impar.")