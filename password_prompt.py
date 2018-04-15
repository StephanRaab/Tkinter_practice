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

        #message vs label, message will auto-wrap text by default
        tk.Message(self, text='Please authenticate with your username and password before continuing.',
        font='System 12 bold', justify='left', aspect=800).pack(pady=(15,0))

        dialog_frame = tk.Frame(self)
        dialog_frame.pack(padx=20, pady=15, anchor='w')

        tk.Label(dialog_frame, text='Username:').grid(row=0, column=0, sticky='w')

        self.user_input = tk.Entry(dialog_frame, background='white', width=24)
        self.user_input.grid(row=0, column=1, sticky='w')
        self.user_input.focus_set()

        tk.Label(dialog_frame, text='Password:').grid(row=1, column=0, sticky='w')
 
        self.password_input = tk.Entry(dialog_frame, background='white', width=24, show='*')
        self.password_input.grid(row=1, column=1, sticky='w')

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
        print("The User clicked 'OK':\nUsername: {}\nPassword: {}".format(self.user_input.get(),
         self.password_input.get()))

    def click_cancel(self):
        print("User click cancel")
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()