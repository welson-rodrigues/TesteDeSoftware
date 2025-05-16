class Aluno:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def getNomeCompleto(self):
        return self.nome + " " + self.sobrenome

    def maiorIdade(self):
        return self.idade >= 18