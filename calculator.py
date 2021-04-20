from tkinter import *
import time

# Main Window
window = Tk()
window.title("Calculator")

image_1 = PhotoImage(file="buttons/1.png")
image_2 = PhotoImage(file="buttons/2.png")
image_3 = PhotoImage(file="buttons/3.png")
image_4 = PhotoImage(file="buttons/4.png")
image_5 = PhotoImage(file="buttons/5.png")
image_6 = PhotoImage(file="buttons/6.png")
image_7 = PhotoImage(file="buttons/7.png")
image_8 = PhotoImage(file="buttons/8.png")
image_9 = PhotoImage(file="buttons/9.png")
image_0 = PhotoImage(file="buttons/0.png")

image_AC = PhotoImage(file="buttons/AC.png")
image_sign = PhotoImage(file="buttons/+-.png")
image_back = PhotoImage(file="buttons/percent.png")
image_divide = PhotoImage(file="buttons/divide.png")
image_multipy = PhotoImage(file="buttons/multiply.png")
image_minus = PhotoImage(file="buttons/minus.png")
image_add = PhotoImage(file="buttons/plus.png")
image_equals = PhotoImage(file="buttons/equals.png")
image_dot = PhotoImage(file="buttons/dot.png")
# Display Tab
display = Entry(window, width="28", borderwidth=0)
display.grid(row=1, column=0, ipadx=30, ipady=10)

# creating a frame for all the number, and oberations button
numpad = Frame(window, bg="black")
numpad.grid(row=2, column=0)
history = open("history.txt", 'a')
view_history = open("history.txt", 'r')
# Functions
# number =11 for decimal values
# number =12 for negating the number
# refer button +/- and . for better understanding


def button_click(number):
    prev = display.get()
    try:
        prev.index(".")
        if number != 11:
            display.delete(0, END)
            display.insert(0, prev+str(number))
    except:
        display.delete(0, END)
        if number == 11:
            number = "."
        display.insert(0, prev+str(number))


def invert():
    number = display.get()
    display.delete(0, END)
    number = str(number)
    try:
        j = 0
        number2 = ""
        if number[0] != "-":
            number2 = "-"+str(number)
        else:
            number2 = number[1:]
        display.insert(0, number2)
    except:
        number2 = "-"
        display.insert(0, number2)


def plus():
    global first
    global operator
    first = display.get()
    operator = "addition"
    display.delete(0, END)


def minus():
    global first
    global operator
    first = display.get()
    operator = "subtraction"
    display.delete(0, END)


def multiply():
    global first
    global operator
    first = display.get()
    operator = "multiplication"
    display.delete(0, END)


def divide():
    global first
    global operator
    first = display.get()
    operator = "division"
    display.delete(0, END)

# first and second are obtained as string ,
# if first is decimal second is dont care, 1st nested try works successful
# if first is int and second is float, no . found , gives error , hence shifts to nested except , finds . and works succesful
# if none are float , hence both nested if and nested except gives error, hence moves to except statement , works succesfully


def equals():
    second = display.get()
    display.delete(0, END)
    try:
        try:
            index = first.index(".")
        except:
            index = second.index(".")
        if operator == "addition":
            result = float(second)+float(first)
            result = round(result, 3)
            history.write(f"{first}+{second}={result}\n")
        elif operator == "subtraction":
            result = float(first)-float(second)
            result = round(result, 3)
            history.write(f"{first}-{second}={result}\n")
        elif operator == "multiplication":
            result = float(second)*float(first)
            result = round(result, 3)
            history.write(f"{first}*{second}={result}\n")
        elif operator == "division":
            result = float(first)/float(second)
            result = round(result, 3)
            history.write(f"{first}/{second}={result}\n")
    except:
        if operator == "addition":
            result = int(second)+int(first)
            history.write(f"{first}+{second}={result}\n")
        elif operator == "subtraction":
            result = int(first)-int(second)
            history.write(f"{first}-{second}={result}\n")
        elif operator == "multiplication":
            result = int(second)*int(first)
            history.write(f"{first}*{second}={result}\n")
        elif operator == "division":
            result = int(first)/int(second)
            history.write(f"{first}/{second}={result}\n")
    display.insert(0, result)


def backspace():
    prev = display.get()
    display.delete(0, END)
    prev = prev[:-1]
    display.insert(0, prev)


def clear_all():
    first = None
    display.delete(0, END)


# buttons form 0 to 9
button_one = Button(numpad, image=image_1, borderwidth=0, bg="black",
                    command=lambda: button_click(1))
button_two = Button(numpad, image=image_2, borderwidth=0, bg="black",
                    command=lambda: button_click(2))
button_thr = Button(numpad, image=image_3,  borderwidth=0, bg="black",
                    command=lambda: button_click(3))
button_fou = Button(numpad, image=image_4, borderwidth=0, bg="black",
                    command=lambda: button_click(4))
button_fiv = Button(numpad, image=image_5, borderwidth=0, bg="black",
                    command=lambda: button_click(5))
button_six = Button(numpad, image=image_6, borderwidth=0, bg="black",
                    command=lambda: button_click(6))
button_sev = Button(numpad, image=image_7, borderwidth=0, bg="black",
                    command=lambda: button_click(7))
button_eig = Button(numpad, image=image_8, borderwidth=0, bg="black",
                    command=lambda: button_click(8))
button_nin = Button(numpad, image=image_9, borderwidth=0, bg="black",
                    command=lambda: button_click(9))
button_zer = Button(numpad, image=image_0, borderwidth=0, bg="black",
                    command=lambda: button_click(0))

# Operation buttons
plus = Button(numpad, image=image_add, borderwidth=0, bg="black", command=plus)
minus = Button(numpad, image=image_minus,
               borderwidth=0, bg="black", command=minus)
multiply = Button(numpad, image=image_multipy, borderwidth=0,
                  bg="black", command=multiply)
divide = Button(numpad, image=image_divide,
                borderwidth=0, bg="black", command=divide)
equals = Button(numpad, image=image_equals,
                borderwidth=0, bg="black", command=equals)
button_dot = Button(numpad, image=image_dot, borderwidth=0, bg="black",
                    command=lambda: button_click(11))
button_sig = Button(numpad, image=image_sign, borderwidth=0, bg="black",
                    command=invert)
button_bac = Button(numpad, image=image_back, borderwidth=0, bg="black",
                    command=backspace)
button_Alc = Button(numpad, image=image_AC, borderwidth=0, bg="black",
                    command=clear_all)

# packing buttons in screen


button_Alc.grid(row=0, column=0)
button_sig.grid(row=0, column=1)
button_bac.grid(row=0, column=2)
divide.grid(row=0, column=3)

button_sev.grid(row=1, column=0)
button_eig.grid(row=1, column=1)
button_nin.grid(row=1, column=2)
multiply.grid(row=1, column=3)

button_fou.grid(row=2, column=0)
button_fiv.grid(row=2, column=1)
button_six.grid(row=2, column=2)
minus.grid(row=2, column=3)

button_one.grid(row=3, column=0)
button_two.grid(row=3, column=1)
button_thr.grid(row=3, column=2)
plus.grid(row=3, column=3)

button_zer.grid(row=4, column=0, columnspan=2)
button_dot.grid(row=4, column=2)
equals.grid(row=4, column=3)

history.close
window.mainloop()
