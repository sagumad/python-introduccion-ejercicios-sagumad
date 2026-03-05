#noveno ejercicio uso del input avanzado y formateo de cadenas 

# Solicitar datos al usuario
nombre = input("escriba su nombre: ")
edad = input("escriba su edad: ")
ciudad = input("escriba su ciudad: ")

# Crear una frase usando formateo de cadenas
mensaje = f"Hola {nombre}, tienes {edad} años y vives en {ciudad}."

# Mostrar el mensaje en pantalla
print(mensaje)


# Solicitar una palabra al usuario
texto = input("piensa en una palabra: ")

# Solicitar cuántas veces desea repetirla y convertir a entero
veces = int(input("¿Cuántas veces desea repetirla?: "))

# Multiplicar el texto por la cantidad indicada
resultado = texto * veces

# Mostrar el texto repetido
print("Texto repetido:", resultado)
