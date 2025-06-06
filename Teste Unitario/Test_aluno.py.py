import unittest
from Aluno import Aluno

class TestAluno(unittest.TestCase):

    def test_calculaMedia(self):
        # Sucesso: média correta
        aluno_sucesso = Aluno("João", 80, 90, 70, 100)  # média: 85
        self.assertEqual(aluno_sucesso.calculaMedia(), 85)

        # Falha: (não deve ser 60)
        aluno_falha = Aluno("Maria", 50, 50, 50, 50)  # média: 50
        self.assertNotEqual(aluno_falha.calculaMedia(), 60)

    def test_estaAprovado(self):
        # Sucesso: aprovado (média > 60)
        aluno_aprovado = Aluno("Carlos", 80, 70, 90, 100)  # média: 85
        self.assertTrue(aluno_aprovado.estaAprovado())

        # Falha: reprovado (média <= 60)
        aluno_reprovado = Aluno("Ana", 40, 50, 60, 50)  # média: 50
        self.assertFalse(aluno_reprovado.estaAprovado())

if __name__ == '__main__':
    unittest.main()
