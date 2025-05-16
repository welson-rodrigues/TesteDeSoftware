import unittest

from Aluno.Aluno import Aluno

class AlunoTest(unittest.TestCase):
    aluno = Aluno("Welson", "Rodrigues", 50)
    def testeNomeCompleto(self):
        self.assertEqual("Welson Rodrigues", self.aluno.getNomeCompleto())

    def testeIdade(self):
        self.assertEqual(True, self.aluno.maiorIdade())

if __name__ == '__main__':
    unittest.main()
