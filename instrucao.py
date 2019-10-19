#Encoding='utf-8'
import pyautogui as pyg

class Info:
	def __init__(self):
		self.texto_1 = 'Antes de inciar, ajuste algumas opções na empresa que serão realizadas as vendas.'
		self.texto_2 = '1° Vá aos parâmetros da contabilidade => Geral => Lançamentos => Outras opções e selecione: Não permitir alterar o número do lote nos lançamentos'
		self.texto_3 = '2° No quadro "Repetir após gravar o lançamento" => Cursor em: Selecione Data'
		self.texto_padrao = self.texto_1 + '\n' + self.texto_2 + '\n' + self.texto_3

	def mensagem(self):
		pyg.alert(self.texto_padrao, title='Informações necessárias', button='OK')