from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import selectNumbers
import sendMessage
import createMessage
from tkinter import *
import sys
import time



class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.concluido = Label(self.widget1,text="Concluido!")
        self.concluido["font"] = ("Calibri", "9", "italic")
        self.msg = Label(self.widget1, text="Escolha um arquivo")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Selecionar arquivos"
        self.sair["font"] = ("Calibri", "9")
        self.sair["width"] = 20
        self.sair.bind("<Button-1>", self.escolherArquivo)
        self.sair.pack()
        self.enviar = Button(self.widget1)
        self.enviar["text"] = "Enviar menssagens"
        self.enviar["font"] = ("Calibri", "9")
        self.enviar["width"] = 20
        self.enviar.bind("<Button-1>", self.enviarMenssagem)
        self.enviar.pack()
        options = [
            "Primeiro contato - AME",
            "Aviso - AME",
            "Ambulatório de Especialidades",
            "Cancelamento",
            #"nova menssagem"
        ]
        self.variable = StringVar(self.widget1)
        self.variable.set(options[0])
        self.w = OptionMenu(self.widget1, self.variable,options[0],options[1],options[2],options[3],)#options[4]
        self.w.pack()

    def escolherArquivo(self, event):
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        self.msg = Label(self.msg, text=filename)
        self.msg.pack()
    def enviarMenssagem(self, event):
        arquivo = self.msg["text"]
        msg = self.variable.get()
        if msg == "Ambulatório de Especialidades":
            messageData = selectNumbers.selectMessageDataAmb(arquivo)
        elif msg == "Cancelamento":
            messageData = selectNumbers.CancelamentoDaAgenda(arquivo)
        else:
            messageData = selectNumbers.selectMessageData(arquivo)
        if self.msg != "Escolha um arquivo":
            messageDataFormat = selectNumbers.formatNumbers(messageData)
            driver = sendMessage.initialize()
            for number in messageDataFormat:
                root.update()
                message = createMessage.createMessage(number,msg)
                sendMessage.sendMessage(number[5], message, driver, number[4])
            driver.close()
            driver.quit()
        self.concluido.pack()
        root.update()
        sys.exit()
root = Tk()
Application(root)
root.mainloop()
