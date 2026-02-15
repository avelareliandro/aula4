class Paciente:
    def __init__(self, nome, idade, altura, peso, tipo_sanguineo, dat_consult, queixa=None):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.tipo_sanguineo = tipo_sanguineo
        self.queixa = queixa
        self.dat_consult = dat_consult if isinstance(dat_consult, list) else ([dat_consult] if dat_consult is not None else []) # O que essa nova linha faz (Passo a passo):Primeiro teste: É uma lista? Se sim, usa ela mesma. Segundo teste (se não for lista): O valor é diferente de None? Se for algo como uma única data "10/02", ele coloca nos colchetes: ["10/02"]. Se for None (vazio), ele entrega uma lista vazia: [].

    def envelhecer(self):
        self.idade += 1

    def engordar(self, kg):
        self.peso += kg

    def emagrecer(self, kg):
        self.peso -= kg

    def __str__(self):
        return f"Paciente: {self.nome}, Idade: {self.idade}, Peso: {self.peso}kg"
