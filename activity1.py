import tkinter as tk
from PIL import Image , ImageTk

root=tk.Tk()
root.title("Image example")
root.geometry('300x400')
upload= Image.open('sample.jpg')
image= ImageTk.PhotoImage(upload)

label=tk.Label(root, image=image, )
label.pack()

root.mainloop()