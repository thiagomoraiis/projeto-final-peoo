from tkinter import *
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
        self.fr5.pack(side=TOP)
        self.C3 = Entry(self.top, background='white')
        self.C3.pack(side=LEFT)
        self.fr5 = Label(self.top, text=" Mudar o horario do agendamento:")
        self.fr5.pack(side=TOP)
        self.C2 = Entry(self.top, background='white')
        self.C2.pack(side=LEFT)
        self.fr5 = Button(self.top, text='Confirmar horario',
        background='#00FF00')
        self.fr5["command"] = self