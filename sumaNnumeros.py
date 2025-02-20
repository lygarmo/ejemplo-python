# Programa que calcula la suma de los primeros N números enteros.

# Función para validar que la entrada sea un número entero positivo
def obtener_numero():
    while True:
        try:
            n = int(input("Introduce un número entero N: "))
            if n <= 0:
                print("Por favor, ingresa un número entero positivo.")
            else:
                return n
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

# Llamar a la función para obtener un número válido
n = obtener_numero()

# Inicializamos la variable suma en 0
suma = 0

# Usamos un bucle para sumar los números del 1 al N
for i in range(1, n+1):
    suma += i  # Sumar cada número i al total de suma

# Imprimir el resultado de la suma
print(f"La suma de los primeros {n} números enteros es: {suma}")

# Añadimos esta línea para esperar que el usuario presione Enter antes de cerrar
input("Presiona Enter para salir...")
