from tkinter import *
import time
# Main Window
window = Tk()
window.title("Calculator")

# Display Tab
display = Entry(window, width="28", borderwidth=0)
display.grid(row=1, column=0, ipadx=30, ipady=10)

# creating a frame for all the number, and oberations button
numpad = Frame(window)
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
button_one = Button(numpad, text="1", padx=20, pady=20,
                    command=lambda: button_click(1))
button_two = Button(numpad, text="2", padx=20, pady=20,
                    command=lambda: button_click(2))
button_thr = Button(numpad, text="3", padx=20, pady=20,
                    command=lambda: button_click(3))
button_fou = Button(numpad, text="4", padx=20, pady=20,
                    command=lambda: button_click(4))
button_fiv = Button(numpad, text="5", padx=20, pady=20,
                    command=lambda: button_click(5))
button_six = Button(numpad, text="6", padx=20, pady=20,
                    command=lambda: button_click(6))
button_sev = Button(numpad, text="7", padx=20, pady=20,
                    command=lambda: button_click(7))
button_eig = Button(numpad, text="8", padx=20, pady=20,
                    command=lambda: button_click(8))
button_nin = Button(numpad, text="9", padx=20, pady=20,
                    command=lambda: button_click(9))
button_zer = Button(numpad, text="0", padx=20, pady=20,
                    command=lambda: button_click(0))

# Operation buttons
plus = Button(numpad, text="+", padx=19, pady=20, command=plus)
minus = Button(numpad, text="-", padx=20, pady=20, command=minus)
multiply = Button(numpad, text="*", padx=20, pady=20, command=multiply)
divide = Button(numpad, text="/", padx=20, pady=20, command=divide)
equals = Button(numpad, text="=", padx=20, pady=52, command=equals)
button_dot = Button(numpad, text=".", padx=22, pady=20,
                    command=lambda: button_click(11))
button_sig = Button(numpad, text="+/-", padx=12, pady=20,
                    command=invert)
button_bac = Button(numpad, text="<-", padx=17, pady=20,
                    command=backspace)
button_Alc = Button(numpad, text="AC", padx=15, pady=20,
                    command=clear_all)


# packing buttons in screen
button_one.grid(row=4, column=0)
button_two.grid(row=4, column=1)
button_thr.grid(row=4, column=2)
button_fou.grid(row=3, column=0)
button_fiv.grid(row=3, column=1)
button_six.grid(row=3, column=2)
button_sev.grid(row=2, column=0)
button_eig.grid(row=2, column=1)
button_nin.grid(row=2, column=2)
button_zer.grid(row=5, column=1)
button_dot.grid(row=5, column=2)
plus.grid(row=2, column=3)
minus.grid(row=3, column=3)
multiply.grid(row=4, column=3)
divide.grid(row=5, column=3)
button_sig.grid(row=5, column=0)
button_bac.grid(row=3, column=4)
button_Alc.grid(row=2, column=4)
equals.grid(row=4, column=4, rowspan=2)

history.close
window.mainloop()
