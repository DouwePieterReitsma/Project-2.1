import tkinter as tk

class Instellingen(tk.Frame):
    def __init__(self, parent, controller):
        super(Instellingen, self).__init__(parent)

        self.controller = controller

        # labels
        titel_label = tk.Label(self, text="Wijzig hier uw instellingen voor het rolluik")
        maximum_temperature_label = tk.Label(self, text="Maximum Temperatuur")
        minimum_temperature_label = tk.Label(self, text="Minimum Temperatuur")
        lichtmax_label = tk.Label(self, text="Maximum Lichtintensiteit")
        lichtmin_label = tk.Label(self, text="Minimale Lichtintensiteit")

        # inputs
        self.maximum_temperature_input_field = tk.Entry(self)
        self.minimum_temperature_input_field = tk.Entry(self)

        self.maximum_light_intensity_input_field = tk.Entry(self)
        self.minumum_light_intensity_input_field = tk.Entry(self)

        # label alignment
        titel_label.grid(column=1, row=1, columnspan=2, pady=20)
        maximum_temperature_label.grid(row=2, column=0)
        minimum_temperature_label.grid(row=3, column=0)
        lichtmax_label.grid(row=2, column=2, sticky="W")
        lichtmin_label.grid(row=3, column=2, sticky="W")

        # input field alignment

        self.maximum_temperature_input_field.grid(row=2, column=1, pady=5, padx=2)
        self.minimum_temperature_input_field.grid(row=3, column=1, pady=5, padx=2)

        self.maximum_light_intensity_input_field.grid(row=2, column=3, pady=5, padx=2)
        self.minumum_light_intensity_input_field.grid(row=3, column=3, pady=5, padx=2)