def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

def contar_vocales_consonantes(texto):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    num_vocales = sum(1 for char in texto if char in vocales)
    num_consonantes = sum(1 for char in texto if char in consonantes)
    return num_vocales, num_consonantes

def palabra_mas_larga(texto):
    palabras = texto.split()
    return max(palabras, key=len)

texto = input("Introduce un texto: ")

cantidad_palabras = contar_palabras(texto)
num_vocales, num_consonantes = contar_vocales_consonantes(texto)
palabra_larga = palabra_mas_larga(texto)

print(f"La cantidad de palabras es: {cantidad_palabras}")
print(f"La cantidad de vocales es: {num_vocales}")
print(f"La cantidad de consonantes es: {num_consonantes}")
print(f"La palabra más larga es: {palabra_larga}")
