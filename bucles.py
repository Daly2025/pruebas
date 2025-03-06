def piramide1(n):
    for i in range (n):
        print("*" * (n-i))
        
piramide1(20)

# Solicitar al usuario que ingrese el número de filas para la pirámide
filas = int(input("Ingrese el número de filas para la pirámide: "))

# Bucle for para dibujar la pirámide
for i in range(1, filas + 1):
    espacios = ' ' * (filas - i)
    asteriscos = '*' * (2 * i - 1)
    print(espacios + asteriscos)

        
        