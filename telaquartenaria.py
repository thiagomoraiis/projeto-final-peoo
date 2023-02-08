from tkinter import *
from turtle import color
class QuintaTela:
    def __init__(self, mestre = None):
        self.top = Toplevel()
        self.top.title("Edição horarios")
        self.fr = Frame(self.top)
        self.fr["padx"] = 150
        self.fr["pady"] = 70
        self.fr.pack()
        self.lab = Label(self.fr, text="Editar seu horario", background='#0277db', foreground='white', )
        self.lab["font"] = ("Arial", "10", "bold")
        self.lab.pack()
        self.fr = Label(self.top, text=" Posição do agendamento: ")
        self.fr.pack(side=LEFT)
        self.inpu1 = Entry(self.top, background='white')
        self.inpu1.pack(side=LEFT)
        self.fr = Label(self.top, text=" Mudar o horario do agendamento:")
        self.fr.pack(side=LEFT)
        self.inpu2 = Entry(self.top, background='white')
        self.inpu2.pack(side=LEFT)
        self.fr = Button(self.top, text='Confirmar horario',
        background='#00FF00')
        self.fr["command"] = self.editar
        self.fr.pack()
        self.lab = Label(self.top, text="")
        self.lab.pack()

    def editar(self):
        dindin = []
        f = open("bd.txt", "r")
        for linha in f:
            dindin.append(linha)
            f.close
        pos = int(self.inpu1.get())
        novo = self.inpu2.get()
        dindin[pos] = novo
        f = open("bd.txt", "w")
        for linha in dindin:
            f.write(linha)
            f.write("\n")
        f.close
        self.top.destroy()