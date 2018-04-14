# from Tkinter import *

# root = Tk()

# def leftClick(event):
#     print('Left Mouse Click')

# def rightClick(event):
#     print("Right Mouse Click")

# frame = Frame(root, width=600, height=400)
# frame.bind('<Button-1>', leftClick)
# frame.bind('<Button-3>', rightClick)
# frame.pack()

# root.mainloop()

from Tkinter import *


class BuckysButtons:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text='Quit', command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("You clicked the 'Print Message' button")

root = Tk()
b = BuckysButtons(root)
root.mainloop()