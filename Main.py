''' Hello bro, I hope you are fine at your place, blessed day to you,
    I don't have words to tell you anything, so bye... 
    this code is written by me.... Thank you'''

from tkinter import *
from math import sqrt

window = Tk()
# click function
def click(event):
    global screen_value
    global Entry_Widget
    value = event.widget.cget("text")
    if value == "CA" :
        screen_value.set("")
        Entry_Widget.update()

    elif value == "C":
        text = screen_value.get()[:-1]
        Entry_Widget.delete(0,END)
        Entry_Widget.insert(0,text)

    elif value == "=":
        e = screen_value.get()
        e = e.replace("√", "sqrt")
        e = e.replace("^", "**")
        if screen_value.get().isdigit():
            new_value = int(screen_value.get())
        else:
            new_value = eval(e)
        screen_value.set(new_value)
    else:
        if value == "√":
            screen_value.set(screen_value.get() + "√(")
            Entry_Widget.update()
        else:
            screen_value.set(screen_value.get() + value)
            Entry_Widget.update()
        
    

# variables for Calculator
title_name = "Calculator"
windows_Size = "668x687"

# initialising the window 
window.title(title_name)
window.geometry(windows_Size)
window.wm_iconbitmap("r.ico")

# entry widget
screen_value = StringVar()
screen_value.set("")
Entry_Widget = Entry(window, width = 55, font = "Akaya 35", textvar = screen_value )
Entry_Widget.pack()

# Frames and Buttons
first_frame = Frame(window, bg = "pink", height = 65)
first_frame.pack(fill = X, pady = 15)

btn_1 = Button(first_frame, text = "1", font = "Akaya 25 bold", padx = 28, pady = 12)
btn_1.pack(side = LEFT, padx = 10)
btn_1.bind("<Button-1>", click)

btn_2 = Button(first_frame, text = "3", font = "Akaya 25 bold", padx = 28, pady = 12)
btn_2.pack(side = RIGHT, padx = 10)
btn_2.bind("<Button-1>", click)

btn_3 = Button(first_frame, text = "2", font = "Akaya 25 bold", padx = 28, pady = 12)
btn_3.pack()
btn_3.bind("<Button-1>", click)

second_frame = Frame(window, bg = "pink", height = 65)
second_frame.pack(fill = X, pady = 45)

btn_4 = Button(second_frame, text = "4", font = "Akaya 25 bold", padx = 28, pady = 12)
btn_4.pack(side = LEFT, padx = 10)
btn_4.bind("<Button-1>", click)

btn_5 = Button(second_frame, text = "5", font = "Akaya 25 bold", padx = 28, pady = 12)
btn_5.pack(side = RIGHT, padx = 10)
btn_5.bind("<Button-1>", click)

btn_6 = Button(second_frame, text = "5", font = "Akaya 25 bold", padx = 28, pady = 12)
btn_6.pack()
btn_6.bind("<Button-1>", click)

third_frame = Frame(window, bg = "pink", height = 65)
third_frame.pack(fill = X, pady = 40)

btn_7 = Button(third_frame, text = "7", font = "Akaya 25 bold", padx = 28, pady = 12)
btn_7.pack(side = LEFT, padx = 10)
btn_7.bind("<Button-1>", click)

btn_8 = Button(third_frame, text = "9", font = "Akaya 25 bold", padx = 28, pady = 12)
btn_8.pack(side = RIGHT, padx = 10)
btn_8.bind("<Button-1>", click)

btn_9 = Button(third_frame, text = "8", font = "Akaya 25 bold", padx = 28, pady = 12)
btn_9.pack()
btn_9.bind("<Button-1>", click)

# equal to frame 

last_frame = Frame(window, bg = "red", height = 30)
last_frame.pack(fill = X, ipady = 3 )

btn_equal = Button(last_frame, text = "=", font = "Akaya 25 bold")
btn_equal.pack(fill = X, padx = 10, pady = 15)
btn_equal.bind("<Button-1>", click)

# new frame
last_frame = Frame(window, bg = "pink", height = 100)
last_frame.pack(fill = X, pady = 1)

btn_plus = Button(last_frame, text = "+", font = "Akaya 25 bold")
btn_plus.pack(side = LEFT, padx = 10)
btn_plus.bind("<Button-1>", click)

btn_minus = Button(last_frame, text = "-", font = "Akaya 25 bold")
btn_minus.pack(side = LEFT, padx = 10)
btn_minus.bind("<Button-1>", click)

btn_multiplication = Button(last_frame, text = "*", font = "Akaya 25 bold")
btn_multiplication.pack(side = LEFT, padx = 10)
btn_multiplication.bind("<Button-1>", click)

btn_division = Button(last_frame, text = "/", font = "Akaya 25 bold")
btn_division.pack(side = LEFT, padx = 10)
btn_division.bind("<Button-1>", click)

btn_modulus = Button(last_frame, text = "%", font = "Akaya 25 bold")
btn_modulus.pack(side = LEFT, padx = 10)
btn_modulus.bind("<Button-1>", click)

btn_square = Button(last_frame, text = "^", font = "Akaya 25 bold")
btn_square.pack(side = LEFT, padx = 3)
btn_square.bind("<Button-1>", click)

btn_squareRoot = Button(last_frame, text = "√", font = "Akaya 25 bold")
btn_squareRoot.pack(side = LEFT, padx = 3)
btn_squareRoot.bind("<Button-1>", click)

# 😂
btn_gift = Button(last_frame, text = "Gift", font = "Akaya 25 bold")
btn_gift.pack(side = LEFT, padx = 3)
btn_gift.bind("<Button-1>", click)

btn_Ce = Button(last_frame, text = "CA", font = "Akaya 17 bold")
btn_Ce.pack(side = LEFT, padx = 3)
btn_Ce.bind("<Button-1>", click)

btn_C = Button(last_frame, text = "C", font = "Akaya 17 bold")
btn_C.pack(side = LEFT, padx = 3)
btn_C.bind("<Button-1>", click)

btn_bracket = Button(last_frame, text = ")", font = "Akaya 17 bold")
btn_bracket.pack(side = LEFT)
btn_bracket.bind("<Button-1>", click)


window.mainloop()