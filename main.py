"""This project has been my first try on GUI programming.
    Its made using tkinter and it is a simple calculator.
    It has a few functions that can be used to calculate
    the result of the expression.
    I have used the eval() function to calculate the result.
    PS:the calculator cannot store the result of the expression.


"""


# import tkinter
from tkinter import *

#intialize the window
app = Tk()
from calcmethods import * #this line is here and not above beacuse we cannot declare a function before setting the root window

app.resizable(height = None, width = None)

app.title("Calculator")
app.geometry("500x350")
app.configure(background='#202020')



# creating the text entry box
text_entry = Entry(app, width=60, borderwidth=0,textvariable=equation)
text_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=20)
# creating the buttons


c = Button(app, text="C", fg="white", bg="#313131", height=1, width=7, font=23,command=clear)
c.grid(row=1, column=2, sticky="nsew")
ce = Button(app, text="CE", fg="white", bg="#313131", height=1, width=7, font=25,command=clear)
ce.grid(row=1, column=1, sticky="nsew")
c1 = Button(app, text="⌫", fg="white", bg="#313131", height=1, width=7, font=25,command=clear)
c1.grid(row=1, column=3, sticky="nsew")
percent = Button(app, text="%", fg="white", bg="#313131", height=1, width=7, font=23)
percent.grid(row=1, column=0, sticky="nsew")
inv = Button(app, text="1/x", fg="white", bg="#313131", height=1, width=7, font=25,command=inv)
inv.grid(row=2, column=0, sticky="nsew")
sqrt = Button(app, text="√x", fg="white", bg="#313131", height=1, width=7, font=25,command=sqrt)
sqrt.grid(row=2, column=2, sticky="nsew")
sqr = Button(app, text="x^2", fg="white", bg="#313131", height=1, width=7, font=25,command=square)
sqr.grid(row=2, column=1, sticky="nsew")
divide = Button(app, text="÷", fg="white", bg="#313131", height=1, width=7, font=25, command=lambda: press("/"))
divide.grid(row=2, column=3, sticky="nsew")
multiply = Button(app, text="×", fg="white", bg="#313131", height=1, width=7, font=25, command=lambda: press("*"))
multiply.grid(row=3, column=3, sticky="nsew")
minus = Button(app, text="-", fg="white", bg="#313131", height=1, width=7, font=25, command=lambda: press("-"))
minus.grid(row=4, column=3, sticky="nsew")
plus = Button(app, text="+", fg="white", bg="#313131", height=1, width=7, font=25, command=lambda: press("+"))
plus.grid(row=5, column=3, sticky="nsew")
# numeric buttons

one = Button(app, text="1", fg="white", bg="#313131", height=1, width=7, font=25,command=lambda: press(1))
one.grid(row=5, column=0, sticky="nsew")
two = Button(app, text="2", fg="white", bg="#313131", height=1, width=7, font=25,command=lambda: press(2))
two.grid(row=5, column=1, sticky="nsew")
three = Button(app, text="3", fg="white", bg="#313131", height=1, width=7, font=25,command=lambda: press(3))
three.grid(row=5, column=2, sticky="nsew")
four = Button(app, text="4", fg="white", bg="#313131", height=1, width=7, font=25,command=lambda: press(4))
four.grid(row=4, column=0, sticky="nsew")
five = Button(app, text="5", fg="white", bg="#313131", height=1, width=7, font=25,command=lambda: press(5))
five.grid(row=4, column=1, sticky="nsew")
six = Button(app, text="6", fg="white", bg="#313131", height=1, width=7, font=25,command=lambda: press(6))
six.grid(row=4, column=2, sticky="nsew")
seven = Button(app, text="7", fg="white", bg="#313131", height=1, width=7, font=25,command=lambda: press(7))
seven.grid(row=3, column=0, sticky="nsew")
eight = Button(app, text="8", fg="white", bg="#313131", height=1, width=7, font=25,command=lambda: press(8))
eight.grid(row=3, column=1, sticky="nsew")
nine = Button(app, text="9", fg="white", bg="#313131", height=1, width=7, font=25,command=lambda: press(9))
nine.grid(row=3, column=2, sticky="nsew")
zero = Button(app, text="0", fg="white", bg="#313131", height=1, width=7, font=25,command=lambda: press(0))
zero.grid(row=6, column=2, sticky="nsew")
equal = Button(app, text="=", fg="white", bg="#313131", height=1, width=7, font=25,command=equalpress)
equal.grid(row=6, column=3, sticky="nsew")
# other buttons
plusminus = Button(app, text="+/-", fg="white", bg="#313131", height=1, width=7, font=25,command=negate)
plusminus.grid(row=6, column=0, sticky="nsew")
decimal = Button(app, text=".", fg="white", bg="#313131", height=1, width=7, font=25,command=lambda: press("."))
decimal.grid(row=6, column=1, sticky="nsew")

# start the application
app.mainloop()
