from  tkinter import *
from  tkinter import  ttk
from  tkinter import  messagebox
import sqlite3



root = Tk()
root.title("Login Page")
root.configure(background='#e1d8b2')
root.geometry("250x400")
style = ttk.Style()
style.configure('TLabel', background='#e1d8b2')
style.configure('TButton', background='#e1d8b2')
style.configure('TRadiobutton', background='#e1d8b2')

ttk.Label(root, text="Enter user name").grid(row=1, column=2,columnspan=2, padx=50, pady=10,sticky='snew')
textUserName = Text(root, width=16, height=1, font=('Arial', 12), pady=1, padx=1 )
textUserName.grid(row=2, column=2, columnspan=2, padx= 50 )

ttk.Label(root, text="Enter password").grid(row=3, column=2,columnspan=2, padx=50, pady=10,sticky='snew')
textPassWord = Text(root, width=16, height=1, font=('Arial', 12), pady= 1 , padx=1)
textPassWord.grid(row=4, column=2, columnspan=2, padx=50)

bu1 = ttk.Button(root, text="Submit")
bu1.grid(row=5, column=3, padx=10, pady=10)
b2 = Button(root, text = "Exit",
            command = root.destroy)

b2.grid(row=6,column=2)

bu1.config(command= lambda :Take_input())

def Take_input():
    USERINPUT = textUserName.get("1.0","end-1c")
    PASSINPUT = textPassWord.get("1.0","end-1c")

    if (USERINPUT == "admin") and (PASSINPUT == "admin"):
        messagebox.showinfo(title="Logging", message="Login Succeeds")
        root.destroy()
        import GameSelect


    else:
        messagebox.showinfo(title="Logging", message="Login Failed\n Try Again")




root.mainloop()