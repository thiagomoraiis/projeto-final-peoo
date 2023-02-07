from tkinter import *
from turtle import window_height
from tkinter import messagebox
from telaterciaria import TerceiraTela
from telaquartenaria import QuintaTela
from telasecundaria import SegundaTela

class PrimeiraTela:
    def __init__(self, mestre=None):
        self.fram1 = Toplevel()
        self.fram1.title("Janela 2")
        self.wid = Frame(self.fram1)
        self.wid["padx"] = 150
        self.wid["pady"] = 30
        self.wid.pack()

        self.message1 = Label(self.wid, text="O que deseja fazer?", background="red", foreground="white")
        self.message2 = Label(self.fram1, text="")
        self.message1.pack() 
        self.message2.pack()

        self.btn_listar = Button(self.wid, background="cyan", foreground="white")
        self.btn_listar["text"] = "Listar"
        self.btn_listar["command"] = self.listando
        self.btn_listar.pack()
        self.message1.pack()

        self.btn_editar = Button(self.wid, background="cyan", foreground="white")
        self.btn_editar["text"] = "Editar"
        self.btn_editar["command"] = self.editar
        self.btn_editar.pack()
        self.message1.pack()

        self.btn_deletar = Button(self.wid, background="cyan", foreground="white")
        self.btn_deletar["text"] = "Excluir"
        self.btn_deletar["command"] = self.deletar
        self.btn_deletar.pack()
        self.message1.pack()

        self.btn_listar = Button(self.wid, background="cyan", foreground="white")
        self.btn_listar["text"] = "Adicionar"
        self.btn_listar["command"] = self.add
        self.btn_listar.pack()
        self.message1.pack()

        self.btn_listar = Button(self.wid, background="cyan", foreground="white")
        self.btn_listar["text"] = "Sair"
        self.btn_listar["command"] = self.logout
        self.btn_listar.pack()
        self.message1.pack()

        # self.btn_deletar = Button(self.wid, background="cyan", foreground="white")
        # self.btn_deletar["text"] = "Remover todo o dinheiro"
        # self.btn_deletar["command"] = self.deletar 
        # self.btn_deletar.pack()
        # self.msg.pack()

        # self.btn_editar = Button(self.wid, background="cyan", foreground="white")
        # self.btn_editar["text"] = "Atualizar o dinheiro"
        # self.btn_editar["command"] = self.editar
        # self.btn_editar.pack()
        # self.msg.pack()

        # self.btn_adicionar = Button(self.wid, background="cyan", foreground="white")
        # self.btn_adicionar["text"] = "Adicionar dinheiro a conta"
        # self.btn_adicionar["command"] = self.add
        # self.btn_adicionar.pack()
        # self.msg.pack()

        # self.btn_sair = Button(self.wid, background="cyan", foreground="white")
        # self.btn_sair["text"] = "Sair"
        # self.btn_sair["command"] = self.logout
        # self.btn_sair.pack()
        # self.message2 = Label(self.fram1, text="")
        # self.message2.pack()

    def listando(self, mestre=None):
        self.fram1 = Toplevel()
        self.fram1.title("Janela de listagem")
        self.list = Frame(self.fram1)
        self.list["padx"] = 150
        self.list["pady"] = 30
        self.list.pack()
        self.titulo1 = Label(self.list, text="Sua lista:", background="orange", foreground="white")
        self.titulo1.pack()
        self.fram2 = Frame(self.fram1)
        self.fram2.pack()
        arquivo = open('bd.txt', 'r')
        for arq in arquivo:
            self.dados = Label(self.list, text=arq, foreground="#202024")
            self.dados.pack()

    def listar(self):
        PrimeiraTela()

    def logout(self):
        self.fram1.destroy()
            # self.wid.destroy()
    def deletar(self):
        TerceiraTela()
    def add(self):
        SegundaTela()
    def editar(self):
        QuintaTela()