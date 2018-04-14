# from https://www.youtube.com/watch?v=Wb1YFgHqUZ8

import Tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        # self.master.title("App Title")

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
        tk.Label(dialog_frame, text='Please authenticate with your username and password before continuing.').pack()

        username_frame = tk.Frame(self)
        username_frame.pack(padx=15, pady=15)
        tk.Label(username_frame, text='Username:').pack(side='left')
        tk.Entry(username_frame).pack(side='left')

        password_frame = tk.Frame(self)
        password_frame.pack(padx=15, pady=5)
        tk.Label(password_frame, text='Password:').pack(side='left')
        tk.Entry(password_frame).pack(side='left')

        #creating button frame and placing the buttons inside
        button_frame = tk.Frame(self)
        button_frame.pack(padx=15, pady=(0, 15), anchor='e')
        tk.Button(button_frame, text='OK', default='active', command=self.click_ok).pack(side='right')
        tk.Button(button_frame, text='Cancel', command=self.click_cancel).pack(side='right')

        #final touches
        self.master.protocol('WM_DELETE_WINDOW', self.click_cancel)
        self.master.bind('<Return>', self.click_ok)
        self.master.bind('<Escape>', self.click_cancel)

    def click_ok(self):
        print("User clicked ok")

    def click_cancel(self):
        print("User click cancel")
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()