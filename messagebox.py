from Tkinter import *
import tkMessageBox

root = Tk()

tkMessageBox.showinfo('Window Title', "Monkeys can live up to 300 years.")

# this is a yes/no question
answer = tkMessageBox.askquestion('Question 1', 'Do you like silly faces?')

if answer == 'yes':
 print("8====D~")

root.mainloop()