import tkinter as tk
import subprocess



class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hello_label = tk.Label(self, text="Hello, Banana!")
        self.hello_label.pack(side="top")

subprocess.call('python update.py',shell=True)
root = tk.Tk()
app = App(master=root)
app.mainloop()

