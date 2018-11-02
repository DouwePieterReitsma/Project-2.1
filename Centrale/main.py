import tkinter

top = tkinter.Tk()
top.title("Centrale")
top.minsize(1024,768)

helloLabel = tkinter.Label(top, text = "Hoi")
helloLabel.pack()

top.mainloop()