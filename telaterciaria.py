from tkinter import *
class TerceiraTela:
    def __init__(self):
        self.top = Toplevel()
        self.top.title("deletar ")
        self.fmn = Frame(self.top)
        self.fmn["pady"] = 50
        self.fmn["padx"] = 150
        self.fmn.pack()
        self.lab = Label(self.fmn, text="Remova")
        self.lab["font"] = ("Arial", "10", "bold")
        self.lab.pack()
        self.fmn = Label(self.top, text="deletar")
        self.fmn.pack(side=TOP)
        self.inp = Entry(self.top)
        self.inp.pack()
        self.fmn = Button(self.top, text="Exclui")
        self.fmn["command"] = self.deletar
        self.fmn.pack()
        self.varMsg = Label(self.top, text="")
        self.varMsg.pack()

    # def deletar(self):
    #     nomes = []
    #     f = open("bd.txt", "r")
    #     for row in  f:
    #         nomes.append(row)
    #         # f.close()

    #     pos = int(self.inp.get())
    #     nomes.remove(nomes[pos])
    #     f = open("bd.txt", "w")
    #     for row in nomes:
    #         f.white(row)
    #     f.close

    def deletar(self):
        agend = []
        x = open("bd.txt", "r")
        for Linha in x:
            agend.append(Linha)
            x.close
        position = int(self.inp.get())
        agend.remove(agend[position])
        x = open("bd.txt", "w")
        for Linha in agend:
            x.write(Linha)
        x.close

