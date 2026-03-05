#octavo ejercicio implementacion e iteracion de colecciones con ciclos 


# Crear una lista de números
numeros = [1, 2, 3, 4, 5]

# Crear una lista vacía donde se guardarán los números pares
pares = []

# Recorrer cada número de la lista
for numero in numeros:
    # Verificar si el número es par
    if numero % 2 == 0:
        # Agregar el número par a la nueva lista
        pares.append(numero)

# Mostrar la lista original
print("Números originales:", numeros)

# Mostrar la nueva lista con números pares
print("Números pares:", pares)


# Crear un diccionario con nombres y edades
personas = {
    "Ana": 17,
    "pablo": 22,
    "santiago": 15
}

# Crear una lista vacía para guardar los nombres de mayores de edad
mayores = []

# Recorrer el diccionario obteniendo nombre y edad
for nombre, edad in personas.items():
    # Verificar si la persona es mayor de edad
    if edad >= 18:
        # Agregar el nombre a la lista
        mayores.append(nombre)

# Mostrar las personas mayores de edad
print("Personas mayores de edad:", mayores)