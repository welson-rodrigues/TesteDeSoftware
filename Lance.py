class Lance:
    def __init__(self, nome_usuario, valor):
        self.nome_usuario = nome_usuario
        self.valor = valor

class Leilao:
    def __init__(self, nome_produto, valor_inicial):
        self.nome_produto = nome_produto
        self.valor_inicial = valor_inicial
        self.lances = []

    def cadastrar_lance(self, lance: Lance):
        if lance.valor > self.valor_inicial:
            self.lances.append(lance)
            return True
        return False

    def obter_vencedor(self):
        if not self.lances:
            return None
        return max(self.lances, key=lambda l: l.valor) #Retorna o lance com o maior valor dentro da lista de lance
