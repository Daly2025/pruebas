# academia.py

# Importar la clase Alumno desde el archivo alumno.py
from Alumno import Alumno
# Importar la librería Faker
from faker import Faker

# Crear instancia de Faker
fake = Faker()

# Crear una instancia de Alumno con datos aleatorios generados por Faker
alumno = Alumno(fake.name(), fake.random_int(18, 30), fake.random_int(0, 100))

# Imprimir la información del alumno
print(alumno)

# Comprobar si el alumno es mayor de edad
print(alumno.es_mayor_de_edad())



class Academia:
    def __init__(self):
        self.alumnos = []

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def contar_mayores_de_edad(self):
        # Cuenta cuántos alumnos son mayores de edad
        return sum(1 for alumno in self.alumnos if alumno.es_mayor_de_edad() == f"{alumno.nombre} es mayor de edad.")

# Crear instancias de Academia y Alumno
academia = Academia()
alumno1 = Alumno("Juan", 18, 7)
alumno2 = Alumno("Maria", 17, 9)
alumno3 = Alumno("Pedro", 20, 6)

# Agregar alumnos a la academia
academia.agregar_alumno(alumno1)
academia.agregar_alumno(alumno2)
academia.agregar_alumno(alumno3)

# Contar cuántos alumnos son mayores de edad
print("Número de alumnos mayores de edad:", academia.contar_mayores_de_edad())



class Academia:
    def __init__(self):
        self.alumnos = []

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def contar_nombres_repetidos(self):
        conteo_nombres = {}
        for alumno in self.alumnos:
            if alumno.nombre in conteo_nombres:
                conteo_nombres[alumno.nombre] += 1
            else:
                conteo_nombres[alumno.nombre] = 1
        return conteo_nombres

# Crear instancias de Academia y Alumno
academia = Academia()
alumno1 = Alumno("Juan", 18, 7)
alumno2 = Alumno("Maria", 17, 9)
alumno3 = Alumno("Juan", 20, 6)
alumno4 = Alumno("Pedro", 22, 8)

# Agregar alumnos a la academia
academia.agregar_alumno(alumno1)
academia.agregar_alumno(alumno2)
academia.agregar_alumno(alumno3)
academia.agregar_alumno(alumno4)

# Contar cuántos nombres se repiten
nombres_repetidos = academia.contar_nombres_repetidos()
print("Nombres repetidos y sus conteos:", nombres_repetidos)


