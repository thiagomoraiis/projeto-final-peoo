from tkinter import *
from tkinter import messagebox
from turtle import window_height

from telaprincipal import PrimeiraTela

class MasterFrame:
    def __init__(self, mestre):
        self.root = mestre
        self.root.title("Banco")
        self.frame1 = Frame(mestre)
        self.frame1["padx"] = 150
        self.frame1["pady"] = 70
        self.frame1.pack()
        self.titulo = Label(
            self.frame1, text="Banco", foreground="white", background="orange"
        )
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
        self.frame2 = Frame(mestre)
        self.frame2.pack()
        self.label_btn1 = Label(
            self.frame2, text="Nome", foreground="white", background="orange"
        )
        self.label_btn1.pack(side=TOP)
        self.input1 = Entry(self.frame2)
        self.input1.pack(side=LEFT)
        self.frame3 = Frame(mestre)
        self.frame3.pack()
        self.label_btn2 = Label(
            self.frame3, text="Senha", foreground="white", background="orange"
        )
        self.label_btn2.pack(side=TOP)
        self.input2 = Entry(self.frame3)
        self.input2.pack()
        self.frame4 = Frame(mestre)
        self.frame4.pack()
        self.btn = Button(
            self.frame4, text="Entrar", foreground="white", background="orange"
        )
        self.btn["command"] = self.autenticar
        self.btn.pack()
        self.msg = Label(
            self.frame4, text=""
        )
        self.msg.pack()

    def autenticar(self):
        nomeUser = self.input1.get()
        senhaUser = self.input2.get()
        if nomeUser == "Lavinia" and senhaUser == "12345":
            self.msg["text"] = "LOGADO!"
            PrimeiraTela()
        elif nomeUser == "Lavinia":
            messagebox.showerror(title="Erro!", message="A senha está incorreta!")
        elif senhaUser == "12345":
            messagebox.showerror(title="Erro!", message="O nome do usuario está incorreto!")
        else:
            messagebox.showerror(title="Dados incorretos!", message="Informe Novamente!")
            self.root.withdraw()


raiz = Tk()
MasterFrame(raiz)
raiz.mainloop()
