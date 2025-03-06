class Coche:
    # El constructor de la clase (__init__) se utiliza para inicializar los atributos del objeto
    def __init__(self, modelo, color):
        self.modelo = modelo  # Atributo del modelo del coche
        self.color = color    # Atributo del color del coche
        self.velocidad = 0    # Atributo de la velocidad inicial (en km/h)

    # Método para mostrar la información del coche
    def mostrar_info(self):
        print(f"Modelo: {self.modelo}, Color: {self.color}, Velocidad: {self.velocidad} km/h")
    
    # Método para cambiar el color del coche
    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        print(f"El color del coche ha sido cambiado a {self.color}.")
    
    # Método para simular que el coche acelera
    def acelerar(self, incremento):
        self.velocidad += incremento  # Aumenta la velocidad en 'incremento' km/h
        print(f"El coche ha acelerado. Nueva velocidad: {self.velocidad} km/h")

# Crear una instancia (objeto) de la clase Coche
mi_coche = Coche("Toyota Corolla", "rojo")

# Mostrar la información inicial del coche
mi_coche.mostrar_info()

# Cambiar el color del coche
mi_coche.cambiar_color("azul")

# Acelerar el coche
mi_coche.acelerar(20)  # Aumenta la velocidad en 20 km/h
mi_coche.acelerar(30)  # Aumenta la velocidad en 30 km/h

# Mostrar la información del coche después de acelerar
mi_coche.mostrar_info()
