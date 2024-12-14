from tkinter import *

root = Tk()

e = Entry(root, width=20 )
e.pack()
e.insert(0,"Enter your name")


def myClick():
  
    hello = "Hello " + e.get()
    myLabel = Label(root, text= hello)
    myLabel.pack()
    
e.delete(0,"end")

myButton = Button (root,text="Button", command= myClick)
myButton.pack()


root.mainloop()
