import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("480x480") # largeur * hauteur 
        self.master.minsize(width=715, height=550)
        self.master.maxsize(width=715, height=550)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "1Hedddllo Wdfdrtyfoddrld\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.label= tk.Label(master=self.master, bg="#FDF6B2", fg="black",font=("Roboto",18), width=53, text="Application de test de mise à jour auto").place(x=0,y=200)

    def say_hi(self):
        print("Hello Worlddfdf!")
root = tk.Tk()
app = App(master=root)

app.mainloop()

