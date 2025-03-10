def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primeros_n_primos(n):
    primos = []
    numero = 2
    while len(primos) < n:
        if es_primo(numero):
            primos.append(numero)
        numero += 1
    return primos

n = int(input("Introduce un número: "))
print(f"Los primeros {n} números primos son: {primeros_n_primos(n)}")
