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
