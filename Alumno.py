class Alumno:
    def __init__(self, nombre, edad, calificacion=0):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion  # Atributo para la calificación, por defecto es 0

    def __str__(self):
        # Devuelve una cadena con la información del alumno
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Calificación: {self.calificacion}"

    def actualizar_calificacion(self, nueva_calificacion):
        # Actualiza la calificación del alumno
        self.calificacion = nueva_calificacion
        print(f"Calificación de {self.nombre} actualizada a {self.calificacion}")

    def aprobado(self):
        # Verifica si el alumno ha aprobado (por ejemplo, si la calificación es 6 o mayor)
        if self.calificacion >= 6:
            return f"{self.nombre} ha aprobado."
        else:
            return f"{self.nombre} no ha aprobado."
    
    # Método para comprobar si el alumno es mayor de edad
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return f"{self.nombre} es mayor de edad."
        else:
            return f"{self.nombre} no es mayor de edad."

# Crear una instancia de la clase Alumno
alumno1 = Alumno("Juan", 18, 7)

# Imprimir la información del alumno
print(alumno1)

# Actualizar la calificación del alumno
alumno1.actualizar_calificacion(5)

# Comprobar si el alumno ha aprobado
print(alumno1.aprobado())

# Comprobar si el alumno es mayor de edad
print(alumno1.es_mayor_de_edad())

# Imprimir la información actualizada del alumno
print(alumno1)


   