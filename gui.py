import tkinter as tk
from tkinter import *
from tkinter import messagebox

m = Tk()
m.title('tic-tac-toe')

clicked = True
ans = 0


def disableButtons():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)


def checkwin():
    global winner
    winner = False

    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg = "green")
        b2.config(bg = "green")
        b3.config(bg = "green")
        winner = True
        messagebox.showinfo("tic-tac-toe", "CONGRATULATIONS! X WINS")
        disableButtons()

    if b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        b4.config(bg = "green")
        b5.config(bg = "green")
        b6.config(bg = "green")
        winner = True
        messagebox.showinfo("tic-tac-toe", "CONGRATULATIONS! X WINS")
        disableButtons()

    if b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        b7.config(bg = "green")
        b8.config(bg = "green")
        b9.config(bg = "green")
        winner = True
        messagebox.showinfo("tic-tac-toe", "CONGRATULATIONS! X WINS")
        disableButtons()

    if b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        b1.config(bg = "green")
        b4.config(bg = "green")
        b7.config(bg = "green")
        winner = True
        messagebox.showinfo("tic-tac-toe", "CONGRATULATIONS! X WINS")
        disableButtons()

    if b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        b2.config(bg = "green")
        b5.config(bg = "green")
        b8.config(bg = "green")
        winner = True
        messagebox.showinfo("tic-tac-toe", "CONGRATULATIONS! X WINS")
        disableButtons()

    if b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        b3.config(bg = "green")
        b6.config(bg = "green")
        b9.config(bg = "green")
        winner = True
        messagebox.showinfo("tic-tac-toe", "CONGRATULATIONS! X WINS")
        disableButtons()

    if b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        b1.config(bg = "green")
        b5.config(bg = "green")
        b9.config(bg = "green")
        winner = True
        messagebox.showinfo("tic-tac-toe", "CONGRATULATIONS! X WINS")
        disableButtons()

    if b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
        b3.config(bg = "green")
        b5.config(bg = "green")
        b7.config(bg = "green")
        winner = True
        messagebox.showinfo("tic-tac-toe", "CONGRATULATIONS! X WINS")
        disableButtons()



    elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        b1.config(bg = "green")
        b2.config(bg = "green")
        b3.config(bg = "green")
        winner = True
        messagebox.showinfo("tic-tac-toe", "CONGRATULATIONS! O WINS")
        disableButtons()

    if b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
        b4.config(bg = "green")
        b5.config(bg = "green")
        b6.config(bg = "green")
        winner = True
        messagebox.showinfo("tic-tac-toe", "CONGRATULATIONS! O WINS")
        disableButtons()

    if b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        b7.config(bg = "green")
        b8.config(bg = "green")
        b9.config(bg = "green")
        winner = True
        messagebox.showinfo("tic-tac-toe", "CONGRATULATIONS! O WINS")
        disableButtons()

    if b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        b1.config(bg = "green")
        b4.config(bg = "green")
        b7.config(bg = "green")
        winner = True
        messagebox.showinfo("tic-tac-toe", "CONGRATULATIONS! O WINS")
        disableButtons()

    if b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
        b2.config(bg = "green")
        b5.config(bg = "green")
        b8.config(bg = "green")
        winner = True
        messagebox.showinfo("tic-tac-toe", "CONGRATULATIONS! O WINS")
        disableButtons()

    if b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
        b3.config(bg = "green")
        b6.config(bg = "green")
        b9.config(bg = "green")
        winner = True
        messagebox.showinfo("tic-tac-toe", "CONGRATULATIONS! O WINS")
        disableButtons()

    if b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
        b1.config(bg = "green")
        b5.config(bg = "green")
        b9.config(bg = "green")
        winner = True
        messagebox.showinfo("tic-tac-toe", "CONGRATULATIONS! O WINS")
        disableButtons()

    if b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
        b3.config(bg = "green")
        b5.config(bg = "green")
        b7.config(bg = "green")
        winner = True
        messagebox.showinfo("tic-tac-toe", "CONGRATULATIONS! O WINS")
        disableButtons()

    if ans == 9 and winner == False:
        messagebox.showinfo("tic-tac-toe", "it's a tie, no one wins!")
        disableButtons()

def b_clicked(b):
    global clicked, ans

    if b["text"]=="" and clicked == True:
        b["text"] = "X"
        clicked = False
        ans+=1
        checkwin()

    elif b["text"]=="" and clicked == False:
        b["text"] = "O"
        clicked = True
        ans+=1
        checkwin()

    else:
        messagebox.showerror("tic-tac-toe", "the box is already selected. pick another box!")


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, ans
    clicked = True
    ans = 0

    b1 = Button(m, text='', font = ("helvetica", 20), height=3, width = 6, bg = "SystemButtonFace", command=lambda: b_clicked(b1))
    b2 = Button(m, text='', font = ("helvetica", 20), height=3, width = 6, bg = "SystemButtonFace", command=lambda: b_clicked(b2))
    b3 = Button(m, text='', font = ("helvetica", 20), height=3, width = 6, bg = "SystemButtonFace", command=lambda: b_clicked(b3))

    b4 = Button(m, text='', font = ("helvetica", 20), height=3, width = 6, bg = "SystemButtonFace", command=lambda: b_clicked(b4))
    b5 = Button(m, text='', font = ("helvetica", 20), height=3, width = 6, bg = "SystemButtonFace", command=lambda: b_clicked(b5))
    b6 = Button(m, text='', font = ("helvetica", 20), height=3, width = 6, bg = "SystemButtonFace", command=lambda: b_clicked(b6))

    b7 = Button(m, text='', font = ("helvetica", 20), height=3, width = 6, bg = "SystemButtonFace", command=lambda: b_clicked(b7))
    b8 = Button(m, text='', font = ("helvetica", 20), height=3, width = 6, bg = "SystemButtonFace", command=lambda: b_clicked(b8))
    b9 = Button(m, text='', font = ("helvetica", 20), height=3, width = 6, bg = "SystemButtonFace", command=lambda: b_clicked(b9))

    b1.grid(row = 0, column = 0)
    b2.grid(row = 0, column = 1)
    b3.grid(row = 0, column = 2)

    b4.grid(row = 1, column = 0)
    b5.grid(row = 1, column = 1)
    b6.grid(row = 1, column = 2)

    b7.grid(row = 2, column = 0)
    b8.grid(row = 2, column = 1)
    b9.grid(row = 2, column = 2)

my_menu = Menu(m)
m.config(menu = my_menu)
options_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label="options", menu=  options_menu)
options_menu.add_command(label="reset game",command = reset)

reset()


m.mainloop()