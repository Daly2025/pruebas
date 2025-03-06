# Solicitar al usuario que ingrese dos números y la operación a realizar
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
operacion = input("Introduce la operación a realizar (suma, resta, multiplicación, división): ")

# Usar match-case para realizar la operación correspondiente
match operacion:
    case "suma":
        print("La suma es:", numero1 + numero2)
    case "resta":
        print("La resta es:", numero1 - numero2)
    case "multiplicación":
        print("La multiplicación es:", numero1 * numero2)
    case "división":
        print("La división es:", numero1 / numero2)
    case _:
        print("Operación no contemplada")
        
# Ejecutar el script y probar con diferentes valores
# python pruebas.py
# Inicializar la suma
suma = 0

# Solicitar al usuario que ingrese el primer número
numero = float(input("Ingrese un número (0 para terminar): "))

# Bucle while para continuar sumando números hasta que se ingrese 0
while numero != 0:
    # Agregar el número a la suma
    suma += numero
    # Solicitar al usuario que ingrese el siguiente número
    numero = float(input("Ingrese otro número (0 para terminar): "))

# Imprimir el resultado de la suma
print(f"La suma total es: {suma}")

def mostrar_menu():
    print("Menú de opciones:")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Elija una opción: ")

    if opcion == '1':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"La suma es: {num1 + num2}")
    elif opcion == '2':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"La resta es: {num1 - num2}")
    elif opcion == '3':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"La multiplicación es: {num1 * num2}")
    elif opcion == '4':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if num2 != 0:
            print(f"La división es: {num1 / num2}")
        else:
            print("Error: No se puede dividir por cero.")
    elif opcion == '5':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")
        
        
        # Lista de números
numeros = [1, 2, 3, 4, 5]

# Inicializar la suma
suma = 0

# Bucle for para sumar todos los números en la lista
for numero in numeros:
    suma += numero

# Imprimir el resultado
print(f"La suma de los números es: {suma}")



