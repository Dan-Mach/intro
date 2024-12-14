from tkinter import *
import tkinter as tk

root = tk.Tk()

def window (grid):
    root.title("Button")


def myClick():
    myLabel = Label(root, text= "Click me")
    myLabel.pack()
    

myButton = Button (root, text="Carrier", command=myClick ) 

myButton.pack()

root.mainloop()