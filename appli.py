import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hello_label = tk.Label(self, text="Hello, World!")
        self.hello_label.pack(side="top")

root = tk.Tk()
app = App(master=root)
app.mainloop()

