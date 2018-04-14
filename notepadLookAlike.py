from Tkinter import *

def doNothing():
    print("Don't do anything!")

def quitProgram():
    print("You quit the program :(")

root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='New Project', command=doNothing)
subMenu.add_command(label='New', command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=quitProgram)

editMenu = Menu(menu)
subEditMenu = Menu(editMenu)
menu.add_cascade(label='Edit', menu=subEditMenu)
subEditMenu.add_command(label="undo")
subEditMenu.add_command(label="redo")

root.mainloop()