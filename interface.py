from tkinter import *


class Interface:
    _instances = []

    @classmethod
    def getInstances(cls):
        return cls._instances

    def __init__(self, name, sizex=500, sizey=500):
        self.window = Tk(useTk=FALSE)
        self.name = name
        self.sizex = sizex
        self.sizey = sizey

        Interface._instances.append(self)

    def createWindow(self, inst):
        if inst == 0:
            self.window = Tk()
        else:
            self.window = Toplevel()

        self.window.title(self.name)
        self.window.geometry("%dx%d" % (self.sizex, self.sizey))

    def update(self):
        self.window.mainloop()
