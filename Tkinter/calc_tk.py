
import tkinter as tk
from tkinter import messagebox

def add_digit(digit):
    value = calc.get()
    if value[0]=='0' and len(value) == 1:
        value = value[1:]
    calc.delete(0,tk.END)
    calc.insert(0,value+digit)

def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc.delete(0,tk.END)
    calc.insert(0,value+operation)


# try(will check if this operation is possible) except(will show us a warnning message)
# 'attention' is head title 'enter only digits' is the message
# errors that could appear (NameError,SyntaxError, ZeroDivisionError)
def calculate():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value+value[:-1]
    calc.delete(0,tk.END)
    try:
        calc.insert(0,eval(value))
    except (NameError,SyntaxError, ZeroDivisionError):
        messagebox.showinfo('attention', 'enter only digits')
    calc.insert(0,' ')
    

def clear():
    calc.delete(0,'end')
    calc.insert(0,'0')



def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('arial', 13), command=lambda: add_digit(digit))

def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('arial', 13), bg='red', command=lambda: add_operation(operation))

def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('arial', 13), bg='red', command=calculate)

def press_key(event):
    print(event.char)
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()
    elif not event.char.isdigit():
        clear()


win = tk.Tk()
win.title('calculator')
win.geometry('250x270+100+200')
win['bg'] = '#33ffe6'

win.bind('<Key>', press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('arial',15), width=15)
calc.insert(0,'0')
calc.grid(row=0,column=0,columnspan=4,sticky='we', padx=5)
make_digit_button('1').grid(row=1,column=0,stick='wens',pady=5,)
make_digit_button('2').grid(row=1,column=1,stick='wens',pady=5,)
make_digit_button('3').grid(row=1,column=2,stick='wens',pady=5,)
make_digit_button('4').grid(row=2,column=0,stick='wens',pady=5,)
make_digit_button('5').grid(row=2,column=1,stick='wens',pady=5,)
make_digit_button('6').grid(row=2,column=2,stick='wens',pady=5,)
make_digit_button('7').grid(row=3,column=0,stick='wens',pady=5,)
make_digit_button('8').grid(row=3,column=1,stick='wens',pady=5,)
make_digit_button('9').grid(row=3,column=2,stick='wens',pady=5,)
make_digit_button('0').grid(row=4,column=0,stick='wens',pady=5,)

make_operation_button('+').grid(row=1,column=3,stick='wens',pady=5,)
make_operation_button('-').grid(row=2,column=3,stick='wens',pady=5,)
make_operation_button('/').grid(row=3,column=3,stick='wens',pady=5,)
make_operation_button('*').grid(row=4,column=3,stick='wens',pady=5,)

tk.Button(text='C', bd=5, font=('arial', 13), bg='blue',fg = 'white', command=clear).grid(row=4,column=1,stick='wens',pady=5)

make_calc_button('=').grid(row=4,column=2,stick='wens',pady=5)


win.grid_columnconfigure(0,minsize=60)  
win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)
win.grid_columnconfigure(3,minsize=60)

win.grid_rowconfigure(1,minsize=60)
win.grid_rowconfigure(2,minsize=60)
win.grid_rowconfigure(3,minsize=60)
win.grid_rowconfigure(4,minsize=60)

win.resizable(False,False)
win.mainloop()
































# result1 = tk.Entry(calc).grid(row=0,column=1,command=result)
# enter = tk.Button(calc,text='first number').grid(row=0,column=2,command=enter)
# labe = tk.Label(calc,text='firstnumber').grid(row=0,column=0,stick='w')
# zero = tk.Button(calc,text='0').grid(row=2,column=0, stick='w',command=zero)
# one = tk.Button(calc,text='1').grid(row=2,column=1, stick='w',command=onee)
# two = tk.Button(calc,text='2').grid(row=2,column=2, stick='w', command=two)
# three = tk.Button(calc,text='3').grid(row=3,column=0, stick='w',command=three)
# four = tk.Button(calc,text='4').grid(row=3,column=1, stick='w',command=four)
# five = tk.Button(calc,text='5').grid(row=3,column=2, stick='w',command=five)
# six = tk.Button(calc,text='6').grid(row=4,column=0, stick='w',command=six)
# seven = tk.Button(calc,text='7').grid(row=4,column=1, stick='w',command=seven)
# eight = tk.Button(calc,text='8').grid(row=4,column=2, stick='w',command=eight)
# nine = tk.Button(calc,text='9').grid(row=5,column=0, stick='w',command=nine)
# plus = tk.Button(calc,text='+').grid(row=6,column=0, stick='w',command=plus)
# minus = tk.Button(calc,text='-').grid(row=6,column=1, stick='w',command=minus)
# devide = tk.Button(calc,text='/').grid(row=6,column=2, stick='w',command=devide)
# multyply = tk.Button(calc,text='*').grid(row=6,column=3, stick='w',command=multyply)