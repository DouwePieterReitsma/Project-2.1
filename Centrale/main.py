import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
from tkinter import *
matplotlib.use("TkAgg")


class Centrale(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Centrale")
        self.resizable(False, False)
        self.title_font = tkfont.Font(family='Courier', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (BeginScherm, RolluikBesturing, Gegevens, Instellingen):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("BeginScherm")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class BeginScherm(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        welkom = ttk.Label(self, text="Welkom bij de centrale voor uw zonnescherm \n selecteer hieronder uw zonnescherm",
                           font=("Courier", 14))
        welkom.grid(column=0, row=1, columnspan=4, padx=15, pady=15, sticky=W)

        button1 = ttk.Button(self, text="Beginscherm",
                             command=lambda: controller.show_frame("BeginScherm"))
        button2 = ttk.Button(self, text="RolluikBesturing",
                             command=lambda: controller.show_frame("RolluikBesturing"))
        button3 = ttk.Button(self, text="Gegevens",
                             command=lambda: controller.show_frame("Gegevens"))
        button4 = ttk.Button(self, text="Instellingen",
                             command=lambda: controller.show_frame("Instellingen"))

        button1.config(width=26)
        button2.config(width=26)
        button3.config(width=26)
        button4.config(width=26)
        button1.grid(column=0, row=0, sticky=W+E)
        button2.grid(column=1, row=0, sticky=W+E)
        button3.grid(column=2, row=0, sticky=W+E)
        button4.grid(column=3, row=0, sticky=W+E)

       # photo = PhotoImage(file="logozengltd.gif")
       # welkom2 = ttk.Label(self, image=photo)
       # welkom2.grid(column=0, row=3, sticky=W)


class RolluikBesturing(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button1 = ttk.Button(self, text="Beginscherm",
                             command=lambda: controller.show_frame("BeginScherm"))
        button2 = ttk.Button(self, text="RolluikBesturing",
                             command=lambda: controller.show_frame("RolluikBesturing"))
        button3 = ttk.Button(self, text="Gegevens",
                             command=lambda: controller.show_frame("Gegevens"))
        button4 = ttk.Button(self, text="Instellingen",
                             command=lambda: controller.show_frame("Instellingen"))

        button1.config(width=26)
        button2.config(width=26)
        button3.config(width=26)
        button4.config(width=26)
        button1.grid(column=0, row=0, sticky=W+E)
        button2.grid(column=1, row=0, sticky=W+E)
        button3.grid(column=2, row=0, sticky=W+E)
        button4.grid(column=3, row=0, sticky=W+E)

        def omhoog():
            omhooglabel = tk.Label(self, text="Rolluik gaat omhoog...", font=('Helvetica', 10))
            omhooglabel.grid(row=4, column=1, columnspan=2, pady=10,padx=10)

        def omlaag():
            omlaaglabel = tk.Label(self, text="Rolluik gaat omlaag...", font=('Helvetica', 10))
            omlaaglabel.grid(row=4, column=1, columnspan=2, pady=10,padx=10)

        label = tk.Label(self, text="Rolluik besturing, oprollen of uitrollen. \nKlik op de knop om het rolluik te besturen ", font=('Helvetica', 12))
        label.grid(row= 2, rowspan=2, column=0, columnspan=2, pady=10,padx=10)
        omhoogbutton = tk.Button(self, text="⬆", bg='gray', fg='#ffffff', relief='flat', bd=8, height=1, font=('Courier', 30),
                            command=omhoog)
        omhoogbutton.grid(row=2, column=2, columnspan=2, pady=20)
        omlaagbutton = tk.Button(self, text="⬇", bg='gray', fg='#ffffff', relief='flat', bd=8, height=1, font=('Courier', 30),
                            command=omlaag)
        omlaagbutton.grid(row=3, column=2, columnspan=2, pady=20)


class Gegevens(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button1 = ttk.Button(self, text="Beginscherm",
                             command=lambda: controller.show_frame("BeginScherm"))
        button2 = ttk.Button(self, text="RolluikBesturing",
                             command=lambda: controller.show_frame("RolluikBesturing"))
        button3 = ttk.Button(self, text="Gegevens",
                             command=lambda: controller.show_frame("Gegevens"))
        button4 = ttk.Button(self, text="Instellingen",
                             command=lambda: controller.show_frame("Instellingen"))


        button1.config(width=26)
        button2.config(width=26)
        button3.config(width=26)
        button4.config(width=26)
        button1.grid(column=0, row=0, sticky=W+E)
        button2.grid(column=1, row=0, sticky=W+E)
        button3.grid(column=2, row=0, sticky=W+E)
        button4.grid(column=3, row=0, sticky=W+E)

        temperatuur = ttk.Label(self, text="Huidige Temperatuur")
        temperatuur.grid(column=0, row=2, columnspan=2, padx=5, pady=5)
        test1 = Figure(figsize=(3, 3), dpi=100)
        a = test1.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 3, 1, 2, 4, 5, 6])
        canvas = FigureCanvasTkAgg(test1, self)
        canvas.get_tk_widget().grid(column=0, row=3, columnspan=2, padx=15, pady=15)

        lichtintensiteit = ttk.Label(self, text="Huidige Lichtintensiteit")
        lichtintensiteit.grid(column=2, row=2, columnspan=2, padx=5, pady=5)
        test2 = Figure(figsize=(3, 3), dpi=100)
        a = test2.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 3, 1, 2, 4, 5, 6])
        canvas = FigureCanvasTkAgg(test2, self)
        canvas.get_tk_widget().grid(column=2, row=3, columnspan=2, padx=15, pady=15)

        afstand = ttk.Label(self, text="Huidige uitrollengte")
        afstand.grid(column=1, row=4, columnspan=2, padx=5, pady=5)
        test3 = Figure(figsize=(3, 3), dpi=100)
        a = test3.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 3, 1, 2, 4, 5, 6])
        canvas = FigureCanvasTkAgg(test3, self)
        canvas.get_tk_widget().grid(column=1, row=5, columnspan=2, padx=15, pady=15)

class Instellingen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        titel = ttk.Label(self, text="Wijzig hier uw instellingen voor het rolluik")
        button1 = ttk.Button(self, text="Beginscherm",
                             command=lambda: controller.show_frame("BeginScherm"))
        button2 = ttk.Button(self, text="RolluikBesturing",
                             command=lambda: controller.show_frame("RolluikBesturing"))
        button3 = ttk.Button(self, text="Gegevens",
                             command=lambda: controller.show_frame("Gegevens"))
        button4 = ttk.Button(self, text="Instellingen",
                             command=lambda: controller.show_frame("Instellingen"))

        tempmax = ttk.Label(self, text="Maximum Temperatuur")
        tempmin = ttk.Label(self, text="Minimum Temperatuur")
        lichtmax = ttk.Label(self, text="Maximum Lichtintensiteit")
        lichtmin = ttk.Label(self, text="Minimale Lichtintensiteit")


        invoer1 = ttk.Entry(self)
        invoer2 = ttk.Entry(self)
        invoer3 = ttk.Entry(self)
        invoer4 = ttk.Entry(self)

        titel.grid(column=1, row=1, columnspan=2, pady=20)

        button1.config(width=26)
        button2.config(width=26)
        button3.config(width=26)
        button4.config(width=26)
        button1.grid(column=0, row=0, sticky=W+E)
        button2.grid(column=1, row=0, sticky=W+E)
        button3.grid(column=2, row=0, sticky=W+E)
        button4.grid(column=3, row=0, sticky=W+E)

        tempmax.grid(row=2, column=0)
        tempmin.grid(row=3, column=0)
        lichtmax.grid(row=2, column=2, sticky="W")
        lichtmin.grid(row=3, column=2, sticky="W")
        invoer1.grid(row=2, column=1, pady=5)
        invoer2.grid(row=3, column=1, pady=5)
        invoer3.grid(row=2, column=3, pady=5)
        invoer4.grid(row=3, column=3, pady=5)


if __name__ == "__main__":
    app = Centrale()
    app.mainloop()