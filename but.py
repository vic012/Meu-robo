#encoding='utf-8'
import pandas as pd
import pyautogui as pyg

class butDesktop:
	def __init__(self, vendas_com_cartoes, arquivo_de_dados):
		#Ler o arquivo que contém os dados
		self.arquivo = pd.read_csv(arquivo_de_dados, sep=';', encoding='utf-8')
		#transforma os dados em dataframe
		self.df_arquivo = pd.DataFrame(self.arquivo)
		self.vendas_com_cartoes = vendas_com_cartoes

	def verificacao(self):
		#Deve verificar se o valor das vendas com cartões é maior que qualquer valor de venda nos dados
		valor_base = float(self.vendas_com_cartoes)
		#O teste será iniciado, se todos os itens da lista forem maiores prosseguir, senão deve iniciar outra etapa
		teste = list()
		for item in self.df_arquivo['Valor']:
			numero = item.replace('.' , '')
			definitivo = numero.replace(',','.')
			valor = float(definitivo)
			if(valor > valor_base):
				teste.append('maior')
			else:
				teste.append('menor')
		if('menor' in teste):
			alerta = pyg.confirm(text='Existem valores de vendas com cartões maiores que o total de vendas do dia.\nVocê deseja que eu faça a correção?', title='Alerta')
			if(alerta == 'OK'):
				self.auterar_valores(valor_base)
			else:
				pyg.alert('Meu trabalho por aqui foi encerrado!\nMuito obrigado por solicitar a minha ajuda. Até a próxima!!!!', title='Despedida', button='Encerrar o But')
				exit()
		else:
			pass
			#self.trata_dados()

	def auterar_valores(self, valor_base):
		for venda in df_arquivo['Valor']:
			numero = venda.replace('.' , '')
			definitivo = numero.replace(',','.')
			valor = float(definitivo)
			print(valor_base, valor)

	def trata_dados(self):
		#Retira os caracteres indesejados da (series data) e adiciona a uma lista
		lista_data = list()
		for item in self.df_arquivo['Data']:
			#Retira a string padrão Total do dia
			string = item.strip('Total do dia')
			#Retira (:)
			string_formatada = string.strip(':')
			#Adiciona a listacriada acima
			lista_data.append(string_formatada)
		#Transforma em um novo dataframe as informações antigas
		self.df_arquivo['Data'] = lista_data
		self.verifica_tela()
		
	def verifica_tela(self):
		#deve verificar se o usuário está com a tela aberta em primeira instância
		localiza = list()
		try:
			#Detecta a tela por meio de uma imagem predefinida com tema verde
			localiza.append(pyg.locateCenterOnScreen('.\\imagens\\plus_verde.png', grayscale=True))
			self.verifica_modulo(localiza, '.\\imagens\\calc_verde.png')
		except:
			try:
				#Detecta a tela por meio de uma imagem predefinida com tema azul
				localiza.append(pyg.locateCenterOnScreen('.\\imagens\\plus_azul.png', grayscale=True))
				self.verifica_modulo(localiza, '.\\imagens\\calc_azul.png')
			except:
				try:
					#Detecta a tela por meio de uma imagem predefinida com tema cinza
					localiza.append(pyg.locateCenterOnScreen('.\\imagens\\plus_cinza.png', grayscale=True))
					self.verifica_modulo(localiza, '.\\imagens\\calc_cinza.png')
				except:
					try:
						#Detecta a tela por meio de uma imagem predefinida com tema preto
						localiza.append(pyg.locateCenterOnScreen('.\\imagens\\plus_preto.png', grayscale=True))
						self.verifica_modulo(localiza, '.\\imagens\\calc_preto.png')
					except:
						#Notifica o usuário caso ele não esteja na tela correta
						pyg.alert(text='Vá para a tela do sistema Domínio', title='Tela não encontrada', button='OK')
	
	def verifica_modulo(self, plus, imagem):
		#Clica no plus informado
		pyg.click(plus[0])
		#Verifica se está no módulo correto
		localiza_modulo = list()
		try:
			localiza_modulo.append(pyg.locateCenterOnScreen('.\\imagens\\contabilidade.png', grayscale=True))
			pyg.alert(text='Módulo correto, deseja iniciar o but?', title='Inicialização do but', button='OK')
			pyg.click(plus[0])
			self.iniciar_but()
		except:
			pyg.click(pyg.locateCenterOnScreen(imagem, grayscale=True))
			pyg.alert(text='O módulo foi alterado, deseja iniciar o but?', title='Inicialização do but', button='OK')
			self.iniciar_but()

	def iniciar_but(self):
		#Ler o arquivo CSV das vendas e retorna ao usuário a quantidade de lançamentos que serão feitos
		tamanho = len(self.arquivo['Data'])
		mensagem = 'O arquivo contém {} registro(s), sendo assim será(ão) efetuado(s) {} lançamento(s), por favor, confirme que não há nenhum processo nessa empresa em andamento que atrapalhe o meu trabalho! preencha "confirmo" ou clique em "cancel" ou "ok" com o campo em brando'.format(tamanho, tamanho)
		iniciar = (pyg.prompt(mensagem, title='Quantidade de lançamentos e inicialização do but'))
		#Pede confirmação ao usuário, se ele quiser executar o but deve inserir (confirmo) e seré inicializado, senão o programa será
		#Finalizado
		if (iniciar == 'confirmo'):
			#Verifica se os lançamentos padrões já está na tela, senão deve iniciar um novo
			localiza_janela = list()
			try:
				localiza_janela.append(pyg.locateCenterOnScreen('.\\imagens\\lanc_padroes.png', grayscale=True))
				pyg.alert(text='O but seria iniciado', title='Inicialização', button='Muito Bem')
				#self.but(tamanho)
			except:
				#Inicializa a tela de lançamentos
				pyg.hotkey('Alt', 'm', 'p')
				pyg.hotkey('Space')
		else:
			pyg.alert(text='O but não foi inicializado!')

	def but(self, tamanho):
		#Define uma contagem para iniciar um loop
		contagem = 0
		#Começa um novo lançamento
		pyg.hotkey('Alt', 'n')
		pyg.hotkey('1')
		pyg.hotkey('Enter')
		while(contagem <= tamanho):
			if(contagem > tamanho):
				pyg.alert(text='{} Lançamentos realizados com sucesso'. format(tamanho), title='But finalizado', button='OK')
				break
			else:
				#Deve verificar a cada loop se a janela de lançamentos padrões está aberta, se sim prosseguir, senão pausar
				localiza_janela = list()
				try:
					localiza_janela.append(pyg.locateCenterOnScreen('.\\imagens\\lanc_padroes.png', grayscale=True))
					pyg.typewrite(self.df_arquivo['Data'][contagem])
					pyg.hotkey('Tab')
					pyg.typewrite(self.df_arquivo['Valor'][contagem])
				except:
					pyg.alert(text='Alguém roubou as minhas baterias, infelizmente não poderei concluir o meu trabalho', title='Interrupção do But', button='Que pena!')
			contagem = contagem + 1
		#Insere a data