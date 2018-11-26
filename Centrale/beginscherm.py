import tkinter as tk
from tkinter import *

class BeginScherm(tk.Frame):
    def __init__(self, parent, controller):
        super(BeginScherm, self).__init__(parent)

        self.controller = controller

        welkom = tk.Label(self, text="Welkom bij de centrale voor uw zonnescherm \n selecteer hieronder uw zonnescherm", font=("Courier", 14))

        welkom.grid(column=0, row=0, columnspan=4, padx=15, pady=15, sticky=W)