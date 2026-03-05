#Ejercicio numero cuatro uso y manejo de condicionales


#declaro la variable del numero
numero = 8

# condicional para verificar si el numero es positivo
if numero > 0:
    print("El número es positivo.")
elif numero == 0:
    print("El número es cero.")
else:
    print("El número es negativo.")

# condicional para verificar si es par
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# y una condicional adicional para verificar si una persona es mayor de edad

#declaro la variable de la edad
edad = 20

if edad >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")