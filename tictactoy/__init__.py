from tkinter import *
from tkinter import ttk
from tkinter import messagebox

ActivePlayer = 1
p1 = []
p2 = []

root = Tk()
root.title("Tic Tac Toy : Player 1")
style = ttk.Style()
style.theme_use('classic')

bu1 = ttk.Button(root, text=" ")
bu1.grid(row=0, column=0, sticky='snew', ipadx=40, ipady=40)
bu1.config(command=lambda: Buclick(1))

bu2 = ttk.Button(root, text=" ")
bu2.grid(row=0, column=1, sticky='snew', ipadx=40, ipady=40)
bu2.config(command=lambda: Buclick(2))

bu3 = ttk.Button(root, text=" ")
bu3.grid(row=0, column=2, sticky='snew', ipadx=40, ipady=40)
bu3.config(command=lambda: Buclick(3))

bu4 = ttk.Button(root, text=" ")
bu4.grid(row=1, column=0, sticky='snew', ipadx=40, ipady=40)
bu4.config(command=lambda: Buclick(4))

bu5 = ttk.Button(root, text=" ")
bu5.grid(row=1, column=1, sticky='snew', ipadx=40, ipady=40)
bu5.config(command=lambda: Buclick(5))

bu6 = ttk.Button(root, text=" ")
bu6.grid(row=1, column=2, sticky='snew', ipadx=40, ipady=40)
bu6.config(command=lambda: Buclick(6))

bu7 = ttk.Button(root, text=" ")
bu7.grid(row=2, column=0, sticky='snew', ipadx=40, ipady=40)
bu7.config(command=lambda: Buclick(7))

bu8 = ttk.Button(root, text=" ")
bu8.grid(row=2, column=1, sticky='snew', ipadx=40, ipady=40)
bu8.config(command=lambda: Buclick(8))

bu9 = ttk.Button(root, text=" ")
bu9.grid(row=2, column=2, sticky='snew', ipadx=40, ipady=40)
bu9.config(command=lambda: Buclick(9))


def Buclick(id):
    global ActivePlayer
    global p1
    global p2
    if (ActivePlayer == 1):
        SetLayout(id, 'X')
        p1.append(id)
        root.title("Tic Tac Toy : Player 2")
        ActivePlayer = 2
        print("P1:{}".format(p1))
    elif (ActivePlayer == 2):
        SetLayout(id, 'O')
        p2.append(id)
        root.title("Tic Tac Toy : Player 1")
        ActivePlayer = 1
        print("P2:{}".format(p2))
    Check_Winner()


def SetLayout(id,text):
    if (id == 1):
        bu1.config(text=text)
        bu1.state(['disabled'])
    elif (id == 2):
        bu2.config(text=text)
        bu2.state(['disabled'])
    elif (id == 3):
        bu3.config(text=text)
        bu3.state(['disabled'])
    elif (id == 4):
        bu4.config(text=text)
        bu4.state(['disabled'])
    elif (id == 5):
        bu5.config(text=text)
        bu5.state(['disabled'])
    elif (id == 6):
        bu6.config(text=text)
        bu6.state(['disabled'])
    elif (id == 7):
        bu7.config(text=text)
        bu7.state(['disabled'])
    elif (id == 8):
        bu8.config(text=text)
        bu8.state(['disabled'])
    elif (id == 9):
        bu9.config(text=text)
        bu9.state(['disabled'])
resetbut = ttk.Button(root,text="New Game")
resetbut.grid(row=3,column=1,pady=10,padx=10,ipady=10,ipadx=10)
resetbut.config(command=lambda :reset())

def Check_Winner():
    winner = -1
    if ((1 in p1) and (2 in p1) and (3 in p1)):
        winner = 1
    if ((1 in p2) and (2 in p2) and (3 in p2)):
        winner = 2
    if ((4 in p1) and (5 in p1) and (6 in p1)):
        winner = 1
    if ((4 in p2) and (5 in p2) and (6 in p2)):
        winner = 2
    if ((7 in p1) and (8 in p1) and (9 in p1)):
        winner = 1
    if ((7 in p2) and (8 in p2) and (9 in p2)):
        winner = 2
    if ((1 in p1) and (4 in p1) and (7 in p1)):
        winner = 1
    if ((1 in p2) and (4 in p2) and (7 in p2)):
        winner = 2
    if ((2 in p1) and (5 in p1) and (8 in p1)):
        winner = 1
    if ((3 in p1) and (6 in p1) and (9 in p1)):
        winner = 1
    if ((1 in p1) and (5 in p1) and (9 in p1)):
        winner = 1
    if ((3 in p1) and (5 in p1) and (7 in p1)):
        winner = 1
    if ((2 in p2) and (5 in p2) and (8 in p2)):
        winner = 2
    if ((3 in p2) and (6 in p2) and (9 in p2)):
        winner = 2
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        winner = 2
    if ((3 in p2) and (5 in p2) and (7 in p2)):
        winner = 2
    if winner == 1:
        messagebox.showinfo(title='cong.',message='Player 1 is Winner')
    if winner == 2:
        messagebox.showinfo(title='cong.',message='Player 2 is Winner')

def reset():
    p1.clear()
    p2.clear()
    root.destroy()
    Buclick(1)




