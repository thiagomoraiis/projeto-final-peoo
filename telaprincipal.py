from tkinter import *
from tkinter import messagebox
from turtle import window_height

from telaquartenaria import QuintaTela
from telasecundaria import SegundaTela
from telaterciaria import TerceiraTela


class PrimeiraTela:
    def __init__(self, mestre=None):
        self.fram1 = Toplevel()
        self.fram1.title("Janela 2")
        self.fram1["padx"] = 150
        self.fram1["pady"] = 30
        # self.fram1.pack()

        self.message1 = Label(
            self.fram1, text="O que deseja fazer?", background="red", foreground="white"
        )
        self.message2 = Label(self.fram1, text="")
        self.message1.pack()
        self.message2.pack()

        self.btn_listar = Button(self.fram1, background="cyan", foreground="white")
        self.btn_listar["text"] = "Listar"
        self.btn_listar["command"] = self.listando
        self.btn_listar.pack()
        self.message1.pack()

        self.btn_editar = Button(self.fram1, background="cyan", foreground="white")
        self.btn_editar["text"] = "Editar"
        self.btn_editar["command"] = self.editar
        self.btn_editar.pack()
        self.message1.pack()

        self.btn_deletar = Button(self.fram1, background="cyan", foreground="white")
        self.btn_deletar["text"] = "Excluir"
        self.btn_deletar["command"] = self.deletar
        self.btn_deletar.pack()
        self.message1.pack()

        self.btn_listar = Button(self.fram1, background="cyan", foreground="white")
        self.btn_listar["text"] = "Adicionar"
        self.btn_listar["command"] = self.add
        self.btn_listar.pack()
        self.message1.pack()

        self.btn_sair = Button(self.fram1, background="cyan", foreground="white")
        self.btn_sair["text"] = "Sair"
        self.btn_sair["command"] = self.logout
        self.btn_sair.pack()
        self.message1.pack()

    def listando(self, mestre=None):
        self.frame_listar = Toplevel()
        self.frame_listar.title("Janela de listagem")
        self.list = Frame(self.frame_listar)
        self.list["padx"] = 150
        self.list["pady"] = 30
        self.list.pack()
        self.titulo1 = Label(
            self.list, text="Sua lista:", background="orange", foreground="white"
        )
        self.titulo1.pack()
        self.fram2 = Frame(self.frame_listar)
        self.fram2.pack()
        arquivo = open("bd.txt", "r")
        for arq in arquivo:
            self.dados = Label(self.list, text=arq, foreground="#202024")
            self.dados.pack()

    def listar(self):
        PrimeiraTela()

    def logout(self):
        self.fram1.destroy()

    def deletar(self):
        TerceiraTela()

    def add(self):
        SegundaTela()

    def editar(self):
        QuintaTela()
