from tkinter import *

class SegundaTela:
    def __init__(self, mestre=None):
        self.top = Toplevel()
        self.top.title("Janela 2")
        self.fram2 = Frame(self.top)
        self.fram2["pady"] = 70
        self.fram2["padx"] = 150
        self.fram2.pack()
        self.label1 = Label(self.fram2, text="Adicionar um novo valor", background="white", foreground="black")
        self.label1["font"] = ("Open Sans", "12", "bold")
        self.label1.pack()
        self.labeu = Label(self.top, text="Adicionar um novo valor")
        self.labeu.pack(side=TOP)
        self.input3 = Entry(self.top, text="Confirmar adição", background="white", foreground="black")
        self.input3.pack(side=TOP)
        self.button = Button(self.top, text="Adicionar", background="white", foreground="black")
        self.button["command"] = self.adicionar
        self.button.pack()
        self.label3 = Label(self.top, text="")
        self.label3.pack()

    def adicionar(self):
        var1 = open('bd.txt', 'a')
        var2 = self.input3.get()
        var1.write(var2)
        var1.write('\n')
        self.top.destroy()

