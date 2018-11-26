import tkinter as tk

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

matplotlib.use("TkAgg")

class Gegevens(tk.Frame):
    def __init__(self, parent, controller):
        super(Gegevens, self).__init__(parent)

        self.controller = controller


        # temperature
        temperature_label = tk.Label(self, text="Huidige Temperatuur")
        temperature_label.grid(row=0, column=0)

        figure1 = Figure(figsize=(3, 3), dpi=100)
        a = figure1.add_subplot(111)
        self.temperature_canvas = FigureCanvasTkAgg(figure1, self)
        self.temperature_canvas.get_tk_widget().grid(row=1, column=0, columnspan=2, padx=15, pady=15)

        # light intensity
        light_intensity_label = tk.Label(self, text="Huidige Lichtintensiteit")
        light_intensity_label.grid(row=0, column=2)

        figure2 = Figure(figsize=(3, 3), dpi=100)
        a = figure2.add_subplot(111)
        self.light_intensity_canvas = FigureCanvasTkAgg(figure2, self)
        self.light_intensity_canvas.get_tk_widget().grid(row=1, column=2, columnspan=2, padx=15, pady=15)

        # 





    def update_graph(self, graph, xdata, ydata):
        pass