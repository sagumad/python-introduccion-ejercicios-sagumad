# quito ejercicio creacion de ciclos con for y while

# primero un ciclo for para contar del 1 al 5
# declaro la variable suma 
suma = 0

for i in range(1, 6):
    print("Número:", i)
    suma += i
    
# se imprime los resultados

print("Suma total con for:", suma)

# segundo un ciclo while para tambien contar del 1 al 5

# se declara la variable contador y la segunda variable de sumar 
contador = 1
suma2 = 0

while contador <= 5:
    print("Número:", contador)
    suma2 += contador
    contador += 1
    
# se imprime los resultados


print("Suma total con while:", suma2)