from tkinter import *
from tkinter import messagebox
from turtle import window_height

from telaquartenaria import QuintaTela
from telasecundaria import SegundaTela
from telaterciaria import TerceiraTela


class PrimeiraTela:
    def __init__(self, mestre=None):
        self.fram1 = Toplevel() #criação do widget toplevel
        self.fram1.title("Janela 2")
        self.fram1["padx"] = 150 #preenchimento no eixo x
        self.fram1["pady"] = 70 #preenchimento no eixo y

        self.message1 = Label(
            self.fram1, text="Qual operação deseja realizar??", background="red", foreground="white"
        ) #label geral da pagina 
        self.message2 = Label(self.fram1, text="")
        self.message1.pack()
        self.message2.pack()

        self.btn_listar = Button(self.fram1, background="orange", foreground="white") #botão que executara o listamento dos depositos
        self.btn_listar["text"] = "Historico de depositos"
        self.btn_listar["command"] = self.listando # botão receberar a função de detalhar
        self.btn_listar.pack()
        self.message1.pack()

        self.btn_editar = Button(self.fram1, background="orange", foreground="white") #botão que executara a edição
        self.btn_editar["text"] = "Editar Saldo atual"
        self.btn_editar["command"] = self.edit # botão receberar a função de edit
        self.btn_editar.pack()
        self.message1.pack()

        self.btn_deletar = Button(self.fram1, background="orange", foreground="white") #botão que executara o listamento dos depositos
        self.btn_deletar["text"] = "Cancelar deposito"
        self.btn_deletar["command"] = self.deletar #botão recebera a função de deletar itens
        self.btn_deletar.pack()
        self.message1.pack()

        self.btn_listar = Button(self.fram1, background="orange", foreground="white") #botão executara a adição dos depositos
        self.btn_listar["text"] = "Fazer novo deposito"
        self.btn_listar["command"] = self.add #botão executara a adição de depositos
        self.btn_listar.pack()
        self.message1.pack()

        self.btn_sair = Button(self.fram1, background="red", foreground="white")
        self.btn_sair["text"] = "Sair"
        self.btn_sair["command"] = self.logout #função que executar a desconexão do usuario na pagina
        self.btn_sair.pack()
        self.message1.pack()

    def listando(self, mestre=None):
        self.frame_listar = Toplevel()
        self.frame_listar.title("Depositos")
        self.list = Frame(self.frame_listar)
        self.list["padx"] = 150
        self.list["pady"] = 70
        self.list.pack()
        self.titulo1 = Label(
            self.list, text="Historico de depositos:", background="orange", foreground="white"
        )
        self.titulo1.pack()
        self.fram2 = Frame(self.frame_listar)
        self.fram2.pack()
        bd = open("bd.txt", "r")
        for arq in bd:
            self.dados = Label(self.list, text=arq, foreground="#202024")
            self.dados.pack()

    def detalhar(self):
        PrimeiraTela()

    def logout(self):
        self.fram1.destroy()

    def deletar(self):
        TerceiraTela()

    def add(self):
        SegundaTela()

    def edit(self):
        QuintaTela()