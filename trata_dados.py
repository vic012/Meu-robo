import pandas as pd

class dadosArquivo:
	def __init__(self, arquivo):
		self.arquivo = arquivo

	def test(self):
		print(self.arquivo)