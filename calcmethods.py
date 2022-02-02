from tkinter import *


exp = ""
equation = StringVar()


def press(num):
    global exp

    exp = exp + str(num)

    equation.set(exp)


def equalpress():
    try:
        global exp

        total = str(eval(exp))

        equation.set(total)

        exp = ""

    except:

        equation.set(" error ")
        expression = ""


def clear():
    global exp
    exp = ""
    equation.set("0")


def inv():
    global exp
    num = int(equation.get())
    exp = ""
    if num == 0:
        equation.set("Cannot divide by zero")
    else:
        equation.set(1 / num)


def negate():
    global exp
    num = str(equation.get())
    exp = ""
    if num[0] == "-":
        equation.set(num[1:])
    else:
        equation.set("-" + num)

def square():
    global exp
    num = int(equation.get())
    exp = ""
    equation.set(num ** 2)
def sqrt():
    global exp
    num = int(equation.get())
    exp = ""
    equation.set(num ** 0.5)

def factorial():
    global exp
    num = int(equation.get())
    fact = 1
    for n in range(2, num + 1):
        fact *= n
    equation.set(fact)
def mod():
    #write a function to find absolute value
    global exp
    num = int(equation.get())
    exp = ""
    equation.set(num[1:])
#add a cuberoot buttton
def cube():
    global exp
    num = int(equation.get())
    exp = ""
    equation.set(num ** 3)
def cube_root():
    global exp
    num = int(equation.get())
    exp = ""
    equation.set(num ** (1/3))
    