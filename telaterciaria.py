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
        dep = [] # lista chamada dep
        x = open("bd.txt", "r") #variavel x ira abrir o arquivo de lê
        for Linha in x: # laço de repetição ira percorrer as linhas do arquivo
            dep.append(Linha) #a função append vai adicioanr os dados da variavel na lista
            x.close #fecha o arquivo
        position = int(self.inp.get()) #variavel ira receber a entrada do usuario e converter para inteiro
        dep.remove(dep[position]) # a função remove ira remover o item com base no indice 
        x = open("bd.txt", "w") # variavel abre o arquivo
        for Linha in dep: # laço de repetição ira percorrer o arquivo novamnete
            x.write(Linha) #e ira escrever a alteração
        x.close
        self.top.destroy()


