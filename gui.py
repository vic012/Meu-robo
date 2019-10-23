#encoding='utf-8'
from tkinter import *
from tkinter.filedialog import askopenfilename
from but import butDesktop
from instrucao import Info
from janela_card import JanelaVendaCartoes
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
		#Define o campo dos botões
		self.butões = Frame(master)
		self.butões['pady'] = 8
		self.butões.pack()
		#Botão VENDA COM CARTÕES
		self.autentica = Button(self.butões)
		self.autentica['text'] = 'VENDA COM CARTÕES'
		self.autentica['font'] = ('Calibri', '8', 'bold')
		self.autentica['foreground'] = '#c7cbe0'
		self.autentica['background'] = '#03125a'
		self.autentica['width'] = 18
		self.autentica['command'] = self.vendas_com_cartoes
		self.autentica.pack(side=LEFT)
		#Botão VENDA SEM CARTÕES
		self.autentica = Button(self.butões)
		self.autentica['text'] = 'VENDA SEM CARTÕES'
		self.autentica['font'] = ('Calibri', '8', 'bold')
		self.autentica['foreground'] = '#c7cbe0'
		self.autentica['background'] = '#03125a'
		self.autentica['width'] = 18
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
		#Botão INFORMAÇÕES
		self.autentica = Button(self.butões)
		self.autentica['text'] = 'INFORMAÇÕES'
		self.autentica['font'] = ('Calibri', '8', 'bold')
		self.autentica['foreground'] = '#c7cbe0'
		self.autentica['background'] = '#03125a'
		self.autentica['width'] = 12
		self.autentica['command'] = self.informacao
		self.autentica.pack(side=LEFT)

	def informacao(self):
		informe = Info()
		informe.mensagem()

	def vendas_com_cartoes(self):
		root = Tk()
		root.title('Vendas com cartões')
		root.geometry('600x110')
		JanelaVendaCartoes(root)
		root.mainloop()
		
root = Tk()
imagem = PhotoImage(file='.\\imagens\\but.png')
root.title('But de vendas')
root.iconphoto(False, imagem)
root.geometry('600x130')
Inicializar(root)
root.mainloop()
