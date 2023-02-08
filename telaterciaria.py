from tkinter import *
class TerceiraTela:
    def __init__(self):
        self.top = Toplevel()
        self.top.title("Cancelamento")
        self.fmn = Frame(self.top)
        self.fmn["pady"] = 70
        self.fmn["padx"] = 150
        self.fmn.pack()
        self.lab = Label(self.fmn, text="Cancele")
        self.lab["font"] = ("Arial", "10", "bold")
        self.lab.pack()
        self.fmn = Label(self.top, text="Cancelar deposito")
        self.fmn.pack(side=TOP)
        self.inp = Entry(self.top)
        self.inp.pack()
        self.fmn = Button(self.top, text="Exclui")
        self.fmn["command"] = self.deletar
        self.fmn.pack()
        self.varMsg = Label(self.top, text="")
        self.varMsg.pack()

    def deletar(self):
        dep = []
        x = open("bd.txt", "r")
        for Linha in x:
            dep.append(Linha)
            x.close
        position = int(self.inp.get())
        dep.remove(dep[position])
        x = open("bd.txt", "w")
        for Linha in dep:
            x.write(Linha)
        x.close
        self.top.destroy()


