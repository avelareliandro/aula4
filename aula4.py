class Paciente:
    def __init__(self, nome, idade, altura, peso, tipo_sanguineo, dat_consult, queixa=None):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.tipo_sanguineo = tipo_sanguineo
        self.queixa = queixa
        self.dat_consult = dat_consult if isinstance(dat_consult, list) else ([dat_consult] if dat_consult is not None else [])

    def envelhecer(self):
        self.idade += 1

    def engordar(self, kg):
        self.peso += kg

    def emagrecer(self, kg):
        self.peso -= kg

    def __str__(self):
        return f"Paciente: {self.nome}, Idade: {self.idade}, Peso: {self.peso}kg"
