from tkinter import *
import os
from tkinter import messagebox

class Application:
    def __init__(self,master=None):
        self.container = Frame(master)
        self.container["pady"] = 20
        self.container.pack()
        
        # NOME
        self.msg = Label(self.container,text = "SHUTDOWN MACHINE")
        self.msg["font"] = ("arial","20","bold")
        self.msg.pack(side = TOP)

        # TEXTO PARA O INPUT
        self.timeLabel = Label(self.container,text = "\n QUANTOS MINUTOS PARA O SHUTDOWN? \n")
        self.timeLabel["font"] = ("arial","14")
        self.timeLabel.pack(side = TOP)
        
        # COLETA DE DADOS
        self.time = Entry(self.container)
        self.time["width"] = 20
        self.time.pack()
        self.time.pack(pady=10)
        
        #BOTAO CANCEL
        self.cancel = Button(self.container)
        self.cancel["text"] = "CANCELAR"
        self.cancel["font"] = ("arial", "10")
        self.cancel["command"] = self.stop_shutdown
        self.cancel.pack(side = BOTTOM)
        self.cancel.pack(pady=5)

        #BOTAO DE INPUT
        self.enter = Button(self.container)
        self.enter["text"] = "INICIAR"
        self.enter["font"] = ("arial","10")
        self.enter["command"] = self.shutdown
        self.enter.pack()

    #FUNCAO DESLIGAR COMPUTADOR
    def shutdown(self):
        time = self.time.get()
        time = int(time)
        time_final = (60 * time)
        os.system(f'shutdown -s -t {time_final}')
        messagebox.showinfo("SHUTDOWN MACHINE",f'O SEU COMPUTADOR IRÁ DESLIGAR EM {time} MINUTOS')

    #FUNCAO CANCELAR SHUTDOWN
    def stop_shutdown(self):
        os.system("shutdown -a")
        messagebox.showinfo("SHUTDOWN MACHINE", "VOCÊ CANCELOU O DESLIGAMENTO")





root = Tk()
Application(root)
root.mainloop()