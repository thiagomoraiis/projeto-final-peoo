from tkinter import *
from turtle import pos
class QuintaTela:
    def __init__(self, mestre = None):
        self.top = Toplevel()
        self.top.title("Edição horarios")
        self.fr5 = Frame(self.top)
        self.fr5["padx"] = 100
        self.fr5["pady"] = 100
        self.fr5.pack()
        self.ti = Label(self.fr5, text="Editar seu horario", background='#0277db', foreground='white', )
        self.ti["font"] = ("Arial", "10", "bold")
        self.ti.pack()
        self.fr5 = Label(self.top, text=" Posição do agendamento: ")
        self.fr5.pack(side=LEFT)
        self.C3 = Entry(self.top, background='white')
        self.C3.pack(side=LEFT)
        self.fr5 = Label(self.top, text=" Mudar o horario do agendamento:")
        self.fr5.pack(side=LEFT)
        self.C2 = Entry(self.top, background='white')
        self.C2.pack(side=LEFT)
        self.fr5 = Button(self.top, text='Confirmar horario',
        background='#00FF00')
        self.fr5["command"] = self.editar
        self.fr5.pack()
        self.ti = Label(self.top, text="")
        self.ti.pack()

    def editar(self):
        nomes = []
        f = open("bd.txt", "r")
        for linha in f:
            nomes.append(linha)
            f.close
        pos = int(self.C3.get())
        novo = self.C2.get()
        nomes[pos] = novo
        f = open("bd.txt", "w")
        for linha in nomes:
            f.write(linha)
            f.write("\n")
        f.close