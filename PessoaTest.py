import unittest
from Pessoa import Pessoa

class PessoaTest(unittest.TestCase):
    def teste_setIdade(self):
        pessoa = Pessoa()
        pessoa.setNome('Um nome')
        with self.assertRaises(Exception):
            pessoa.setIdade(-1)

if __name__ == '__main__':
    unittest.main()
