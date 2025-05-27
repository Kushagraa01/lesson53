# Top Window Example
from tkinter import *

def open_top_window():
    top = Toplevel()
    top.title("Top Window")
    Label(top, text="This is a top-level window").pack(pady=10)

root = Tk()
root.title("Top Window Example")

btn = Button(root, text="Open Top Window", command=open_top_window)
btn.pack(pady=20)

root.mainloop()
