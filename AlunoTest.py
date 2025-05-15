import unittest

from Aluno import Aluno

class AlunoTest(unittest.TestCase):
    aluno = Aluno("Welson", "Rodrigues", 21)
    def test_something(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
