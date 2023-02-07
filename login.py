from tkinter import *
from turtle import window_height
from tkinter import messagebox
from telaprincipal import PrimeiraTela

class MasterFrame:
    def __init__(self, mestre):
        self.root = mestre
        self.root.title("Banco")
        self.frame1 = Frame(mestre)
        self.frame1["padx"] = 100
        self.frame1["pady"] = 50
        self.frame1.pack()
        self.titulo = Label(self.frame1, text="Banco", foreground="black", background="white")
        self.titulo["font"] = ("Open Sans", "10", "bold")
        self.titulo.pack()
        self.frame2 = Frame(mestre)
        self.frame2.pack()
        self.label_btn1 = Label(self.frame2, text="Nome", foreground="black")
        self.label_btn1.pack(side=TOP)
        self.input1 = Entry(self.frame2)
        self.input1.pack(side=LEFT)
        self.frame3 = Frame(mestre)
        self.frame3.pack()
        self.label_btn2 = Label(self.frame3, text="Senha", foreground="black")
        self.label_btn2.pack(side=TOP)
        self.input2 = Entry(self.frame3)
        self.input2.pack()
        self.frame4 = Frame(mestre)
        self.frame4.pack()
        self.btn = Button(self.frame4, text="Entrar", foreground="black", background="white")
        self.btn["command"] = self.autenticacao
        self.btn.pack()
        self.msg = Label(self.frame4, text="")
        self.msg.pack()

    def autenticacao(self):
        nameLog = self.input1.get()
        passwordLog = self.input2.get()
        if nameLog == "Tatiane" and passwordLog == "123":
            self.msg["text"] = "SUCESSO!"
            PrimeiraTela()
        elif nameLog == "Tatiane":
            messagebox.showerror(title="Erroo!", message="Senha do Usuario Incorreta!")
        elif passwordLog == "123":
            messagebox.showerror(title="Erroo!", message="Nome do usuario Incorreto!")
        else:
            messagebox.showerror(title="Dados incorretos!", message="Digite Novamente!")
            self.root.withdraw()

raiz = Tk()
MasterFrame(raiz)
raiz.mainloop()