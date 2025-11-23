from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image , ImageTk
import random

def open_top_window():
    top = tk.Toplevel()
    top.title("Top Window")
    top.configure(bg='light blue')
    top.geometry('600x400')

    Label(top,text='Please chose one of them ',bg='light blue').pack()
    Label(top,text='rock ,paper ,scissor',bg='light blue').pack()
    Label(top,text='Enter your choice',bg='light blue').pack()

    user_entry=tk.Entry(top)
    user_entry.pack()

    btn=tk.Button(top,text='get result', command=result ,bg='red')
    btn.pack()
    user_ans= user_entry.get()
    Label(top,text=result(user_ans),bg='light blue').pack()
    
    def result():
        if user_ans == computer_ans:
         print("it's a tie")
        elif user_ans =="rock"and computer_ans =="paper":
         print("Computer wins!")
        elif user_ans =="scissor"and computer_ans =="rock":
         print("Computer wins!")
        elif user_ans =="paper"and computer_ans =="scissor":
         print("Computer wins!")
        elif user_ans =="rock"and computer_ans =="scissor":
         print("User wins!")
        elif user_ans =="scissor"and computer_ans =="paper":
          print("User win!")
        elif user_ans =="paper"and computer_ans =="rock":
         print("User win!")
        else:
         print('Please enter corret value')
        user_ans= user_entry.get()
    

        def computer_ans():
          part=["rock","paper","scissor"]
          return random.choices(part)   





def ask_question():
  response=messagebox.askquestion('question box','Do you want to play rock, paper and scissor?')
  if response == 'yes':
        open_top_window()

root=tk.Tk()
root.title("Rock , paper and scissor")
root.configure(bg='light green')   
root.geometry('700x450')

upload= Image.open('rock_paper_scissors.png')
image= ImageTk.PhotoImage(upload)

label=tk.Label(root ,text= "Hello! welcome to my game.",bg='light green')
label.pack()
label1=tk.Label(root ,text= "Let's play rock, paper and scissor",bg='light green')
label1.pack()
btn1=tk.Button(root,text= 'lets start',command =ask_question,bg='red')
btn1.pack()

label2=tk.Label(root,image=image)
label2.pack()

tk.mainloop()