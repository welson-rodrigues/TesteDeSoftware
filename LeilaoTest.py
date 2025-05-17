import unittest
from Lance import Lance, Leilao

class TestLeilao(unittest.TestCase):
    def funcLeilao(self):
        self.leilao = Leilao("Notebook", 1000)

    def maior_que_valor_inicial(self):
        lance = Lance("Alice", 1200)
        resultado = self.leilao.cadastrar_lance(lance)
        self.assertTrue(resultado)
        self.assertIn(lance, self.leilao.lances)

    def menor_ou_igual_valor_inicial(self):
        lance = Lance("Bob", 1000)
        resultado = self.leilao.cadastrar_lance(lance)
        self.assertFalse(resultado)
        self.assertNotIn(lance, self.leilao.lances)

    def vencedor(self):
        l1 = Lance("Alice", 1200)
        l2 = Lance("Bob", 1500)
        l3 = Lance("Carlos", 1300)
        self.leilao.cadastrar_lance(l1)
        self.leilao.cadastrar_lance(l2)
        self.leilao.cadastrar_lance(l3)
        vencedor = self.leilao.obter_vencedor()
        self.assertEqual(vencedor.nome_usuario, "Bob")
        self.assertEqual(vencedor.valor, 1500)

    def vencedor_sem_lances(self):
        vencedor = self.leilao.obter_vencedor()
        self.assertIsNone(vencedor)

if __name__ == "__main__":
    unittest.main()
