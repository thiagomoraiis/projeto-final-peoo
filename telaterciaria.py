from tkinter import *
class TerceiraTela:
    def __init__(self):
        self.top = Toplevel()
        self.top.title("Excluir ")
        self.fmn = Frame(self.top)
        self.fmn["pady"] = 50
        self.fmn["padx"] = 150
        self.fram.pack()
        self.lab = Label(self.fmn, text="Remova")
        self.lab["font"] = ("Arial", "10", "bold")
        self.lab.pack()
        self.fmn = Label(self.top, text="Excluir")
        self.fmn.pack(side=TOP)
        self.inp = Entry(self.top)
        self.inp.pack()
        self.fmn = Button(self.top, text="Exclui")
        self.fmn["command"] = self.excluir
        self.fmn.pack()
        self.varMsg = Label(self.top, text="")
        self.varMsg.pack()

    def excluir(self):
        conta = []
        i = open("bd.txt", "r")
        for row in  i:
            conta.append(row)
            i.close()

        pos = int(self.inp.get())
        conta.remove(conta[pos])
        i = open("bd.txt", "w")
        for row in conta:
            i.white(row)
        i.close

    # def Excluir(self):
    #     agend = []
    #     x = open("arquivo.txt", "r")
    #     for Linha in x:
    #         agend.append(Linha)
    #         x.close
    #     position = int(self.varD.get())
    #     agend.remove(agend[position])
    #     x = open("arquivo.txt", "w")
    #     for Linha in agend:
    #         x.write(Linha)
    #     x.close

