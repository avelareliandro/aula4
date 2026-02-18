class Paciente:
    def __init__(self, nome, idade, altura, peso, tipo_sanguineo, dat_consult, queixa=None):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.tipo_sanguineo = tipo_sanguineo
        self.queixa = queixa
        self.dat_consult = dat_consult if isinstance(dat_consult, list) else ([dat_consult] if dat_consult is not None else []) # O que essa nova linha faz (Passo a passo):Primeiro teste: É uma lista? Se sim, usa ela mesma. Segundo teste (se não for lista): O valor é diferente de None? Se for algo como uma única data "10/02", ele coloca nos colchetes: ["10/02"]. Se for None (vazio), ele entrega uma lista vazia: [].

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
    
p = Paciente("Maria", 30, 1.65, 60, "O+", "10/02")
print(p.nome)       
p.a