import Tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title("App Title")

        self.master.resizable(False, False)
        self.master.tk_setPalette(background='#ececec')

        #center the frame on the screen        
        x = (self.master.winfo_screenwidth() - self.master.winfo_reqwidth()) / 2
        y = (self.master.winfo_screenheight() - self.master.winfo_reqheight()) / 3
        self.master.geometry("+{}+{}".format(x, y))

        self.master.config(menu=tk.Menu(self.master))

        tk.Label(self, text="This is your GUI boilerplate").pack()

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()