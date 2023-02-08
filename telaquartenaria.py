from tkinter import *
from turtle import color
class QuintaTela:
    def __init__(self, mestre = None):
        self.top = Toplevel() #inicialização do widget de nivel superior que sera parametros de outros widgets
        self.top.title("Atualização") #titulo janeja
        self.fr = Frame(self.top) #criaçaõ de frame
        self.fr["padx"] = 150 #preencimento no eixo x (horizontal)
        self.fr["pady"] = 70 #preencimento do eixo y (vertical)
        self.fr.pack() #empacotamento do frame que irá exibi-lo na tela 
        self.lab = Label(self.fr, text="Editar seu saldo", background='orange', foreground='white') #Label para ajudar na orientação do usuario
        self.lab["font"] = ("Arial", "10", "bold") #definição do estilo das fontes
        self.lab.pack()
        self.fr = Label(self.top, text="Numero do deposito: ")
        self.fr.pack(side=LEFT) #empacotamento do frame e ajustar a posição do label
        self.inpu1 = Entry(self.top, background='white') #Entry é responsavel por receber os dados do usuario que serão manipulados posteriormente
        self.inpu1.pack(side=LEFT)
        self.fr = Label(self.top, text="Mudar valor:")
        self.fr.pack(side=LEFT)
        self.inpu2 = Entry(self.top, background='white')
        self.inpu2.pack(side=LEFT)
        self.fr = Button(self.top, text='Confirmar',
        background='#00FF00') #inicialização do botao que vai realizar as ações do usuario
        self.fr["command"] = self.edit #o comando iria receber o botão e, ao clicar, o botão executara o comando da função edit
        self.fr.pack() #
        self.lab = Label(self.top, text="")
        self.lab.pack()

    def edit(self):
        dindin = [] #criação de lista
        f = open("bd.txt", "r") #variavel que ira abrir o arquivo e ler ele
        for linha in f: #laço de repetição que ira percorrer as linha do arquivo
            dindin.append(linha) #função metodo append ira adicionar a variavel "linha" toda vez que p codigo for percorrido  
            f.close #close ira fechar o arquivo
        pos = int(self.inpu1.get()) #variavel "pos" ira receber a entrada do primeiro Entry e ira fazer o casting(converter uma variavel para outro tipo),
                                    # convertendo uma string para um numero inteiro
        novo = float(self.inpu2.get()) #variavel novo ira converter o segundo Entry em numero de ponto flutuante  
        dindin[pos] = novo #o indice da lista ira receber o novo valor que o usuario modificar
        f = open("bd.txt", "w") #variavel ira novamente abrir o arquivo e reescrever o que esta no indice que foi fornecido pelo usuario, editando-o
        for linha in dindin: #laço de repetição que ira percorrer a lista 
            f.write(str(linha)) # write ira, de fato, sobrescrever o que o usuario quiser edit 
            f.write("\n") #quebrar linha
        f.close 
        self.top.destroy() #ao clicar no botão, ele ira destruir o frame, voltando para a tela inicial