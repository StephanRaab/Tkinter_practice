import Tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title("Hello World")

        tk.Label(self, text="This is your GUI boilerplate").pack()

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()