# from https://www.youtube.com/watch?v=Wb1YFgHqUZ8

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

        #moving the label into its own frame
        dialog_frame = tk.Frame(self)
        dialog_frame.pack(padx=20, pady=15)
        tk.Label(dialog_frame, text='GUI Boilerplate').pack()

        #creating button frame and placing the buttons inside
        button_frame = tk.Frame(self)
        button_frame.pack(padx=15, pady=(0, 15), anchor='e')
        tk.Button(button_frame, text='OK', default='active', command=self.click_ok).pack(side='right')
        tk.Button(button_frame, text='Cancel', command=self.click_cancel).pack(side='right')

    def click_ok(self):
        print("User clicked ok")

    def click_cancel(self):
        print("User click cancel")
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()