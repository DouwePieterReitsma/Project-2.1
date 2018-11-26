import tkinter as tk
from tkinter import font as tkfont
from tkinter import *

from gegevens import Gegevens
from beginscherm import BeginScherm
from rolluikbesturing import Rolluikbesturing
from instellingen import Instellingen

class Centrale(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(Centrale, self).__init__(*args, **kwargs)

        # window settings
        self.wm_title("Centrale")
        self.resizable(False, False)
        self.title_font = tkfont.Font(family='Courier', size=18, weight="bold", slant="italic")
        #self.geometry("800x600")

        # button container
        button_container = tk.Frame(self)
        button_container.grid(row=0, column=0)

        button1 = tk.Button(button_container, text="Beginscherm",
                             command=lambda: self.show_frame("BeginScherm"))
        button2 = tk.Button(button_container, text="Rolluikbesturing",
                             command=lambda: self.show_frame("Rolluikbesturing"))
        button3 = tk.Button(button_container, text="Gegevens",
                             command=lambda: self.show_frame("Gegevens"))
        button4 = tk.Button(button_container, text="Instellingen",
                             command=lambda: self.show_frame("Instellingen"))

        button1.config(width=26)
        button2.config(width=26)
        button3.config(width=26)
        button4.config(width=26)
        button1.grid(column=0, row=0, sticky=W+E)
        button2.grid(column=1, row=0, sticky=W+E)
        button3.grid(column=2, row=0, sticky=W+E)
        button4.grid(column=3, row=0, sticky=W+E)

        # container settings
        container = tk.Frame(self)
        #container.pack(side="top", fill="both", expand=True)
        container.grid(row=1, column=0)
        container.grid_rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        # add frames
        self.frames = {}

        for F in (BeginScherm, Gegevens, Rolluikbesturing, Instellingen):
            page_name = F.__name__

            frame = F(parent=container, controller=self)

            frame.grid(row=1, column=0, sticky='nsew')

            self.frames[page_name] = frame

    def show_frame(self, page_name):
        frame = self.frames[page_name]

        frame.tkraise()