class Pessoa:
	nome: str
	idade: int
	
	def setNome(self, nome: str):
		self.nome = nome
	
	def setIdade(self, idade: int):
		if idade < 0:
			raise Exception('Idade com erro')
		self.idade = idade

	def getNome(self):
		return self.nome
	
	def getIdade(self):
		return self.idade
