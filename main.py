from tkinter import *

name = Tk()
name.title('Calculator')

def add_digit(digit):
    value = entry.get()
    if value[0] == '0':
        value = value[1:]
    entry.delete(0, END)
    entry.insert(0, value+digit)

def add_operation(operation):
    value = entry.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+' or '-' or '*' or '/' in value:
        calculate()
        value = entry.get()
    entry.delete(0, END)
    entry.insert(0, value+operation)

def calculate():
    value = entry.get()
    if value in '+-*/':
        value = value + value[1:]
    entry.delete(0, END)
    entry.insert(0, eval(value))

