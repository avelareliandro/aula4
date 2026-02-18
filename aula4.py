class Paciente:
    def __init__(self, nome, idade, altura, peso, tipo_sanguineo, dat_consult, queixa=None):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.tipo_sanguineo = tipo_sanguineo
        self.queixa = queixa
        # O que essa nova linha faz (Passo a passo):Primeiro teste: É uma lista? Se sim, usa ela mesma. Segundo teste (se não for lista): O valor é diferente de None? Se for algo como uma única data "10/02", ele coloca nos colchetes: ["10/02"]. Se for None (vazio), ele entrega uma lista vazia: [].
        self.dat_consult = dat_consult if isinstance(dat_consult, list) else (
            [dat_consult] if dat_consult is not None else [])

    def altera_idade(self, nova_idade):
        self.idade = nova_idade

    def altera_nome(self, novo_nome):
        self.nome = novo_nome

    def altera_altura(self, nova_altura):
        self.altura = nova_altura

    def altera_peso(self, novo_peso):
        self.peso = novo_peso

    def altera_tipo_sanguineo(self, novo_tipo_sanguineo):
        self.tipo_sanguineo = novo_tipo_sanguineo

    def altera_queixa(self, nova_queixa):
        self.queixa = nova_queixa

    def altera_dat_consult(self, nova_dat_consult):
        self.dat_consult.append(nova_dat_consult)

    def adiciona_nome(self, nome):
        self.nome = nome

p = Paciente("Ana", 28, 1.70, 65, "B+", None)
print(p.nome)

p = Paciente("Maria", 30, 1.65, 60, "O+", "10/02")
print(p.nome)
p.altera_nome("Maria Silva")
print(p.nome)
p.altera_idade(31)
print(p.idade)
p.altera_altura(1.66)
print(p.altura)
p.altera_peso(62)
print(p.peso)
p.altera_tipo_sanguineo("A+")
print(p.tipo_sanguineo)
p.altera_queixa("Dor de cabeça")
print(p.queixa)
p.altera_dat_consult("15/03")
print(p.dat_consult)

p = Paciente("João", 25, 1.80, 75, "A-", ["05/01", "20/02"])
print(p.nome)
print(p.dat_consult)
p.altera_dat_consult("10/03")
print(p.dat_consult)    
p = Paciente("Ana", 28, 1.70, 65, "B+", None)
print(p.nome)
print(p.nome)

