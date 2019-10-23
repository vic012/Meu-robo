#encoding='utf-8'
from tkinter import *
from tkinter.filedialog import askopenfilename
from but import butDesktop

class JanelaVendaCartoes:

	def __init__(self, master=None):
		#Determina a fonte e o tamanho padrão dos textos
		self.fonte_padrao = ('Arial', '10')
		#Gera a janela principal
		self.mensagem = Frame(master)
		self.mensagem['pady'] = 5
		self.mensagem.pack()
		#Pede ao usuário o valor das médias das vendas com cartões
		self.titulo = Label(self.mensagem, text='Por favor, insira o valor da média de vendas com cartões')
		self.titulo['font'] = ('Helvetica', '12', 'bold', 'italic')
		self.titulo.pack()
		#Tela para inserir os valores das vendas com cartões
		self.tela_cartao = Frame(master)
		self.tela_cartao['padx'] = 30
		self.tela_cartao.pack()
		self.cartao_label = Label(self.tela_cartao)
		self.cartao_label.pack(side=LEFT)
		#campo para inserir o valor
		self.valor_cartao = Entry(self.tela_cartao)
		self.valor_cartao['width'] = 30
		self.valor_cartao['foreground'] = '#03125a'
		self.valor_cartao['font'] = self.fonte_padrao
		self.valor_cartao.pack(side=LEFT)
		#Define o campo dos botões
		self.butões = Frame(master)
		self.butões['pady'] = 8
		self.butões.pack()
		#Botão ENTER
		self.autentica = Button(self.butões)
		self.autentica['text'] = 'CONFIRMAR'
		self.autentica['font'] = ('Calibri', '8', 'bold')
		self.autentica['foreground'] = '#c7cbe0'
		self.autentica['background'] = '#03125a'
		self.autentica['width'] = 12
		self.autentica['command'] = self.but_iniciar
		self.autentica.pack(side=LEFT)

	def but_iniciar(self):
		vendas_com_cartoes = self.valor_cartao.get()
		selec_arquivo = askopenfilename()
		print(vendas_com_cartoes)
		print(selec_arquivo)
		#iniciar = butDesktop(vendas_com_cartoes, selec_arquivo)
		#iniciar.verificacao()