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
        self.buttons = []

        Interface._instances.append(self)

    def createWindow(self, inst):
        if inst == 0:
            self.window = Tk()
        else:
            self.window = Toplevel()

        self.window.title(self.name)
        self.window.geometry("%dx%d" % (self.sizex, self.sizey))

    def createButton(self, name, action, args=None, placex=0, placey=0, relative=False):
        if args != None:
            btn = Button(
                self.window,
                text=name,
                command=lambda: action(args),
                width=10,
                font=self.font,
            )
        else:
            btn = Button(
                self.window, text=name, command=action, width=10, font=self.font
            )

        if not relative:
            btn.place(x=placex, y=placey)
        else:
            btn.place(relx=placex, rely=placey, anchor="nw")

        self.buttons.append(btn)
        return btn

    def update(self):
        self.window.mainloop()

    def getWindow(self):
        return self.window
