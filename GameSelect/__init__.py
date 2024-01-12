from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()
root.title("Select Game")
root.configure(background='#e1d8b2')
root.geometry("250x400")

style = ttk.Style()
style.configure('TLabel', background='#e1d8b2')
style.configure('TButton', background='#e1d8b2')
style.configure('TRadiobutton', background='#e1d8b2')
try:
    photo = PhotoImage(file= "cereal-tic-tac-toe.gif")
    resize_photo = photo.subsample(2, 2)

finally:print("ok")
TicToyGame = ttk.Button(root,width=20,image=resize_photo)
TicToyGame.grid(row=2, column=2, columnspan=2, padx= 10,pady=10)



root.mainloop()

def buttonoftic():

    import tictactoy
    root.destroy()

TicToyGame.config(command= buttonoftic())




