import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
matplotlib.use("TkAgg")


class Centrale(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Centrale")

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

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

        button1 = ttk.Button(self, text="Beginscherm",
                             command=lambda: controller.show_frame("BeginScherm"))
        button2 = ttk.Button(self, text="RolluikBesturing",
                             command=lambda: controller.show_frame("RolluikBesturing"))
        button3 = ttk.Button(self, text="Gegevens",
                             command=lambda: controller.show_frame("Gegevens"))
        button4 = ttk.Button(self, text="Instellingen",
                             command=lambda: controller.show_frame("Instellingen"))

        button1.grid(column=0, row=0)
        button2.grid(column=1, row=0)
        button3.grid(column=2, row=0)
        button4.grid(column=3, row=0)


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

        button1.grid(column=0, row=0)
        button2.grid(column=1, row=0)
        button3.grid(column=2, row=0)
        button4.grid(column=3, row=0)


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

        button1.grid(column=0, row=0)
        button2.grid(column=1, row=0)
        button3.grid(column=2, row=0)
        button4.grid(column=3, row=0)

        test1 = Figure(figsize=(2, 2), dpi=100)
        a = test1.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 3, 1, 2, 4, 5, 6])

        canvas = FigureCanvasTkAgg(test1, self)
        canvas.get_tk_widget().grid(column=0, row=2, columnspan=2)

        test2 = Figure(figsize=(2, 2), dpi=100)
        a = test2.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 3, 1, 2, 4, 5, 6])

        canvas = FigureCanvasTkAgg(test2, self)
        canvas.get_tk_widget().grid(column=2, row=2, columnspan=2)


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

        TempMax = ttk.Label(self, text="Maximum Temperatuur")
        TempMin = ttk.Label(self, text="Minimum Temperatuur")

        e1 = ttk.Entry(self)
        e2 = ttk.Entry(self)

        titel.grid(column=1, row=1, columnspan=2)
        button1.grid(column=0, row=0)
        button2.grid(column=1, row=0)
        button3.grid(column=2, row=0)
        button4.grid(column=3, row=0)

        TempMax.grid(row=2, column=0, sticky="W")
        TempMin.grid(row=2, column=0, sticky="W")
        e1.grid(row=2, column=1)
        e2.grid(row=3, column=1)


if __name__ == "__main__":
    app = Centrale()
    app.mainloop()