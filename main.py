from interface import *
from binary_func import *


def enviarDados(Entry):
    string = Entry.get()
    binary = stringToBin(string)

    print(binary)


def interfaceDeEnvio():
    interface1.createWindow(1)
    L1 = Label(
        interface1.getWindow(),
        text="String Qualquer:",
        width=20,
        height=20,
        font=interface1.font,
    )
    L1.pack(side=LEFT)

    E1 = Entry(
        interface1.getWindow(),
    )
    E1["width"] = 17
    E1["font"] = interface1.font
    E1.pack(side=LEFT)

    interface1.createButton("Enviar", enviarDados, args=(E1), placex=236, placey=165)

    interface1.update()


def interfaceRecebendo():
    print("Salve")


inicial = Interface("Janela Inicial", 400, 300)
interface1 = Interface("Interface de Codificação", 400, 300)
interface2 = Interface("Interface de Decodificação", 400, 300)

inicial.createWindow(0)
inicial.getWindow().rowconfigure(0, weight=1)
inicial.getWindow().columnconfigure(0, weight=1)

inicial.getWindow().rowconfigure(1, weight=1)


Button(inicial.getWindow(), text="Interface 1", command=interfaceDeEnvio).grid(
    row=0, column=0, sticky="NSEW"
)
Button(inicial.getWindow(), text="Interface 2", command=interfaceRecebendo).grid(
    row=1, column=0, sticky="NSEW"
)

inicial.update()
