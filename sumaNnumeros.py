# Programa que calcula la suma de los primeros N números enteros.

# Se pide al usuario que ingrese un número N
n = int(input("Introduce un número entero N: "))

# Inicializamos la variable suma en 0
suma = 0

# Usamos un bucle para sumar los números del 1 al N
for i in range(1, n+1):
    suma += i  # Sumar cada número i al total de suma

# Imprimir el resultado de la suma
print(f"La suma de los primeros {n} números enteros es: {suma}")

# Añadimos esta línea para esperar que el usuario presione Enter antes de cerrar
input("Presiona Enter para salir...")