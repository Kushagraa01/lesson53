import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.askquestion("Question Box", "Do you want to continue?")

root=tk.Tk()
root.title("Messagebox example")
root.geometry('300x400')

button=tk.Button(root,text='Click me', command=show_message)
button.pack()

root.mainloop()