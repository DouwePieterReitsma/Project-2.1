import tkinter as tk

class Rolluikbesturing(tk.Frame):
    def __init__(self, parent, controller):
        super(Rolluikbesturing, self).__init__(parent)

        self.controller = controller

        label = tk.Label(self, text="Rolluikbesturing, oprollen of uitrollen. \nKlik op de knop om het rolluik te besturen ", font=('Helvetica', 12))
        label.grid(row= 2, rowspan=2, column=0, columnspan=2, pady=10,padx=10)

        roll_in_button = tk.Button(self, text="⬆", bg='gray', fg='#ffffff', relief='flat', bd=8, height=1, font=('Courier', 30),
                            command=self.roll_in)
        roll_in_button.grid(row=2, column=2, columnspan=2, pady=20)

        roll_out_button = tk.Button(self, text="⬇", bg='gray', fg='#ffffff', relief='flat', bd=8, height=1, font=('Courier', 30),
                            command=self.roll_out)
        roll_out_button.grid(row=3, column=2, columnspan=2, pady=20)
    
    def roll_in(self):
        roll_in_label = tk.Label(self, text="Rolluik gaat omhoog...", font=('Helvetica', 10))
        roll_in_label.grid(row=4, column=1, columnspan=2, pady=10,padx=10)

    def roll_out(self):
        roll_out_label = tk.Label(self, text="Rolluik gaat omlaag...", font=('Helvetica', 10))
        roll_out_label.grid(row=4, column=1, columnspan=2, pady=10,padx=10)