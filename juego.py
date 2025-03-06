import random

# Elige un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Mensaje inicial
print("¡Bienvenido al juego de adivinar el número!")
print("Estoy pensando en un número entre 1 y 100. ¡Intenta adivinarlo!")

# Inicializamos el número de intentos
intentos = 0

# Bucle para que el jugador siga adivinando hasta acertar
while True:
    # Solicitar la adivinanza del jugador
    try:
        adivinanza = int(input("Introduce tu adivinanza: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    # Aumentar el contador de intentos
    intentos += 1

    # Comprobamos si la adivinanza es correcta, baja o alta
    if adivinanza < numero_secreto:
        print("¡Demasiado bajo! Intenta nuevamente.")
    elif adivinanza > numero_secreto:
        print("¡Demasiado alto! Intenta nuevamente.")
    else:
        print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
        break  # Sale del bucle cuando se adivina correctamente
    
    
    
    
    import random

# Elige un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Mensaje inicial
print("¡Bienvenido al juego de adivinar el número!")
print("Estoy pensando en un número entre 1 y 100. ¡Intenta adivinarlo!")
print("Tienes 10 intentos para adivinar el número.")

# Inicializamos el número de intentos
intentos = 0
max_intentos = 10

# Bucle para que el jugador siga adivinando hasta acertar o llegar al límite de intentos
while intentos < max_intentos:
    try:
        # Solicitar la adivinanza del jugador
        adivinanza = int(input("Introduce tu adivinanza: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    # Aumentar el contador de intentos
    intentos += 1

    # Comprobamos si la adivinanza es correcta, baja o alta
    if adivinanza < numero_secreto:
        print("¡Demasiado bajo! Intenta nuevamente.")
    elif adivinanza > numero_secreto:
        print("¡Demasiado alto! Intenta nuevamente.")
    else:
        print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
        break  # Sale del bucle cuando se adivina correctamente

    # Si el jugador llega al límite de intentos
    if intentos == max_intentos:
        print(f"¡Perdiste! El número secreto era {numero_secreto}.")
        break

