class Aluno:
    # Notas dos alunos devem ser de 0 a 100
    def __init__(self, nome, nota1, nota2, nota3, nota4):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    # Calcula Média das notas
    def calculaMedia(self):
        return (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4

    # Informa se aluno está aprovado ou não
    def estaAprovado(self):
        return self.calculaMedia() > 60

