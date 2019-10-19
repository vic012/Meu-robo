#encoding='utf-8'
from tkinter import *
from tkinter.filedialog import askopenfilename
from but import butDesktop
from instrucao import Info
import pandas as pd

class Inicializar:
	def __init__(self, master=None):
		#Determina a fonte e o tamanho padrão dos textos
		self.fonte_padrao = ('Arial', '10')
		#determina o lugar da mensagem secundária
		self.mensagem = Frame(master)
		self.mensagem['pady'] = 5
		self.mensagem.pack()
		#Inserir a imagem do But
		self.img = Button(self.mensagem)
		imagem = PhotoImage(file='.\\imagens\\but.png')
		self.img.config(image=imagem)
		self.img.imagem= imagem
		self.img['padx'] = 40
		self.img['pady'] = 20
		self.img.pack(side=LEFT)
		#Pede ao usuário o valor das médias das vendas com cartões
		self.titulo = Label(self.mensagem, text='Olá, meu nome é But')
		self.titulo['font'] = ('Helvetica', '12', 'bold', 'italic')
		self.titulo.pack()
		self.titulo = Label(self.mensagem, text='Eu realizarei os lançamentos das vendas por você. \n Para começar, por favor, insira o valor da média de vendas com cartões.')
		self.titulo['font'] = ('Helvetica', '10')
		self.titulo['foreground'] = '#03125a'
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
		self.autentica['text'] = 'CONTINUAR'
		self.autentica['font'] = ('Calibri', '8', 'bold')
		self.autentica['foreground'] = '#c7cbe0'
		self.autentica['background'] = '#03125a'
		self.autentica['width'] = 10
		self.autentica['command'] = self.but_iniciar
		self.autentica.pack(side=LEFT)
		#Botão de informação
		self.autentica = Button(self.butões)
		self.autentica['text'] = 'INFORMAÇÃO'
		self.autentica['font'] = ('Calibri', '8', 'bold')
		self.autentica['foreground'] = '#c7cbe0'
		self.autentica['background'] = '#03125a'
		self.autentica['width'] = 12
		self.autentica['command'] = self.informacao
		self.autentica.pack(side=LEFT)
		#Botão CANCELAR
		self.autentica = Button(self.butões)
		self.autentica['text'] = 'CANCELAR'
		self.autentica['font'] = ('Calibri', '8', 'bold')
		self.autentica['foreground'] = '#c7cbe0'
		self.autentica['background'] = '#03125a'
		self.autentica['width'] = 8
		self.autentica['command'] = self.butões.quit
		self.autentica.pack(side=LEFT)
		#Avaliação do But
		self.autentica = Button(self.butões)
		self.autentica['text'] = 'AVALIE O MEU TRABALHO'
		self.autentica['font'] = ('Calibri', '8', 'bold')
		self.autentica['foreground'] = '#c7cbe0'
		self.autentica['background'] = '#03125a'
		self.autentica['width'] = 20
		self.autentica['command'] = self.informacao
		self.autentica.pack(side=LEFT)

	def informacao(self):
		informe = Info()
		informe.mensagem()

	def but_iniciar(self):
		vendas_com_cartoes = self.valor_cartao.get()
		selec_arquivo = askopenfilename()
		iniciar = butDesktop(vendas_com_cartoes, selec_arquivo)
		iniciar.verificacao()
		
root = Tk()
imagem = PhotoImage(file='.\\imagens\\but.png')
root.title('But de vendas')
root.iconphoto(False, imagem)
root.geometry('600x150')
Inicializar(root)
root.mainloop()