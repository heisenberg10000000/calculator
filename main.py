from tkinter import *
from tkinter import ttk

calculator = Tk()
calculator.title('Calculator')


def add_digit(digit):
    value = display.get()
    if value[0] == '0':
        value = value[1:]
    display.delete(0, END)
    display.insert(0, value + digit)


def add_operation(operation):
    value = display.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+' or '-' or '*' or '/' in value:
        calculate()
        value = display.get()
    display.delete(0, END)
    display.insert(0, value + operation)


def calculate():
    value = display.get()
    if value in '+-*/':
        value = value + value
    display.delete(0, END)
    display.insert(0, eval(value))


def create_button(title, width=5):
    return Button(text=title, bd=5, font=('Calibri', 15), command=lambda: add_digit(title), width=width)

def create_operation_button(operation, width=5):
    return Button(text=operation, bd=5, font=('Calibri', 15), command=lambda: add_operation(operation), width=width)

def create_equels_button(operation, width=5):
    return Button(text=operation, bd=5, font=('Calibri', 15), command=lambda: calculate(), width=width)

def create_clear_button(operation, width=5):
    return Button(text=operation, bd=5, font=('Calibri', 15), command=clear, width=width)

def delete():
    display.delete(0, END)
    display.insert(0, '0')
def clear():
    display.delete(0, END)
    display.insert(0, 0)

def set_output():
    display.configure(command=calculate())

def press_key(event):

    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-/*':
        add_operation(event.char)
    elif event.char == '\r' or '=' or 'q':
        calculate()



calculator.bind("<Key>", press_key)




display = Entry(calculator, justify=RIGHT, font=('Calibri'))
display.insert(0, '0')

display.grid(columnspan=4, stick='we')


create_button('0').grid(row=5, column=0, columnspan=2, stick='we')
create_button('1').grid(row=4, column=0)
create_button('2').grid(row=4, column=1)
create_button('3').grid(row=4, column=2)
create_button('4').grid(row=3, column=0)
create_button('5').grid(row=3, column=1)
create_button('6').grid(row=3, column=2)
create_button('7').grid(row=2, column=0)
create_button('8').grid(row=2, column=1)
create_button('9').grid(row=2, column=2)

create_operation_button('+').grid(row=2, column=3)
create_operation_button('-').grid(row=3, column=3)
create_operation_button('*').grid(row=4, column=3)
create_operation_button('/').grid(row=5, column=3)

create_equels_button('=').grid(row=5, column=2)
create_clear_button('CE').grid(row=1, column=0)


calculator.mainloop()