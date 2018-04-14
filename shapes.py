from Tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=200)
canvas.pack()

blackLine = canvas.create_line(0,0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill='red')

#start pointx, y, width, height
square = canvas.create_rectangle(25, 25, 100, 100, fill='blue')

canvas.delete(redLine)
# canvas.delete(ALL)

root.mainloop()