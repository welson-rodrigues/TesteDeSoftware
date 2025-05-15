import unittest

from Aluno import Aluno

class AlunoTest(unittest.TestCase):
    aluno = Aluno("Welson", "Rodrigues", 21)
    def testeNomeCompleto(self):
        self.assertEqual("Welson Rodrigues", self.aluno.getNomeCompleto())

if __name__ == '__main__':
    unittest.main()
