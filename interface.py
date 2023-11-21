from tkinter import *


class Interface:
    _instances = []

    @classmethod
    def getInstances(cls):
        return cls._instances

    def __init__(self, name, sizex=500, sizey=500, font="Calibri"):
        self.window = Tk(useTk=FALSE)
        self.name = name
        self.sizex = sizex
        self.sizey = sizey
        self.font = font

        Interface._instances.append(self)

    def createWindow(self, inst):
        if inst == 0:
            self.window = Tk()
        else:
            self.window = Toplevel()

        self.window.title(self.name)
        self.window.geometry("%dx%d" % (self.sizex, self.sizey))

    def createEntry(self, text, width=20):
        self.window.title(self.name)
        L1 = Label(self.window, text=text, font=self.font, width=width)
        L1.pack(side=LEFT)

        E1 = Entry(self.window)
        E1["width"] = 25
        E1.pack(side=LEFT)

    def update(self):
        self.window.mainloop()
