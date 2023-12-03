from interface import *
from binary_func import *
from client import *


def enviarDados(Entry):
    string = Entry.get()
    binary = stringToBin(string)
    hexadecimal = str(binToHex(binary))

    list = []
    text_8b6t = ""
    soma_ant = 0
    for i in range(2, len(hexadecimal)):
        if i % 2 != 0 and hexadecimal[i] != None:
            str_hex = hexadecimal[i - 1] + hexadecimal[i]
            list.append(encode8b6t(str_hex))


    soma = 0
    flag_inverte = False


    for i in list:
        for j in i:
            flag_inverte = False
            text_8b6t += " "
            soma_ant = soma
            soma = sum(j)
            if soma_ant == 1 and soma == 1:
                flag_inverte = True
                for x in j:
                    x = -x
                    text_8b6t += str(x)
                    soma = -1
            print(soma)
            for x in j:
                if flag_inverte == False:
                    text_8b6t += str(x)



    send(text_8b6t)
    tela3 = Interface("Conversão da String", 400, 300)
    tela3.createWindow(2)

    T1 = Text(tela3.getWindow(), height=5, width=45)
    T1.pack()
    text = "Binário:\n" + str(binary)
    T1.insert(END, text)

    T2 = Text(tela3.getWindow(), height=5, width=45)
    T2.pack()
    text = "Hexadecimal:\n" + hexadecimal
    T2.insert(END, text)

    T3 = Text(tela3.getWindow(), height=5, width=45)
    T3.pack()
    text = "8b/6t:\n" + text_8b6t
    T3.insert(END, text)

    tela3.update()


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
    interface1.createButton("Enviar", enviarDados, args=(E1), placex=150, placey=170)

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
