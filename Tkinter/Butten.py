
from sre_parse import State
import tkinter as tk



def say_hello():
    print('hello')

def add_lable():
    lable = tk.Label(win,text='new')
    lable.pack()

def counter():
    global count
    count+=1
    btn4['text'] = f'count: {count}'
    if count % 5 == 0:
        btn4['activebackgound']='green'

def disable():
    lable = tk.Label(win,text='new new')
    lable.pack()

count = 0

win = tk.Tk()
win.geometry('300x400+100+200')
win.title('Button test')

btn1 = tk.Button(win,text='hello',    # shows button that displays 'hello'
command=say_hello)                    # and returns 'hello' in console as written in function

btn2 = tk.Button(win,text='Add new lable',  # shows button that displays 'add new lable'
command=add_lable)                          # and returns 'new' in program as 'lable' as written in function

btn3 = tk.Button(win,text='Add new lambda',
command=lambda: tk.Label(win,text='new lambda')
)

btn4 = tk.Button(win,text=f'count: {count}',
command=counter,
bg='red',
# activebackground ='blue'
)

btn5 = tk.Button(win,text='new lable',
command=disable)


btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()

win.mainloop()

#.grid() allows us to use variables as table
# columnspan= / rowspan=  how many columns or rows will element take(grid)
#stick= with side to pin our object(n,s,w,e)