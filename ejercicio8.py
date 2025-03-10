class SistemaVotacion:
    def __init__(self):
        self.candidatos = []
        self.votantes = set()
        self.votos = {}

    def registrar_candidato(self, nombre):
        if nombre not in self.candidatos:
            self.candidatos.append(nombre)
            self.votos[nombre] = 0
            print(f"Candidato {nombre} registrado con éxito.")
        else:
            print(f"El candidato {nombre} ya está registrado.")

    def registrar_votante(self, id_votante):
        if id_votante not in self.votantes:
            self.votantes.add(id_votante)
            print(f"Votante {id_votante} registrado con éxito.")
        else:
            print(f"El votante {id_votante} ya está registrado.")

    def emitir_voto(self, id_votante, candidato):
        if id_votante in self.votantes and candidato in self.candidatos:
            if id_votante not in self.votos_emitidos:
                self.votos[candidato] += 1
                self.votos_emitidos.add(id_votante)
                print(f"Voto registrado para el candidato {candidato}.")
            else:
                print("Este votante ya ha emitido su voto.")
        else:
            print("Votante no registrado o candidato no válido.")

    def mostrar_resultados(self):
        print("Resultados de la votación:")
        for candidato, votos in self.votos.items():
            print(f"{candidato}: {votos} votos")


sistema = SistemaVotacion()

# Ejemplo de uso:
# Registrar candidatos
sistema.registrar_candidato("Candidato 1")
sistema.registrar_candidato("Candidato 2")

# Registrar votantes
sistema.registrar_votante("Votante 1")
sistema.registrar_votante("Votante 2")

# Emitir votos
sistema.emitir_voto("Votante 1", "Candidato 1")
sistema.emitir_voto("Votante 2", "Candidato 2")

# Mostrar resultados
sistema.mostrar_resultados()
