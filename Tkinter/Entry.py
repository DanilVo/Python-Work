import tkinter as tk

# printin terminal value that user entered
def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('empty entry')

# delet filled by user text (from index , to index)
# has to get at least one parameter
# (end) to delete whole input
def delete_entry():
    name.delete(0, 'end')

# return to terminal value of (name and password)
# and after delets it
def submite():
    print(name.get())
    print(password.get())
    name.delete(0, 'end')
    password.delete(0, 'end')


win = tk.Tk()
win.title("entry code")
win.geometry('400x300+100+200')

name = tk.Entry(win)
name.grid(row=0, column=1)
password = tk.Entry(win,show='*')
password.grid(row=1, column=1)

tk.Label(win, text='Name').grid(row=0, column=0, stick='w')

tk.Label(win, text='password').grid(row=1, column=0, stick='w')

tk.Button(win, text='get', command=get_entry).grid(row=0, column=2)

tk.Button(win, text='delete', command=delete_entry).grid(row=1, column=2)

tk.Button(win, text='insert', command=lambda: name.insert(1, 'hello'))\
    .grid(row=1, column=2, stick='we')

tk.Button(win, text='submite', command=submite).grid(row=2, column=0, stick='w')


win.grid_columnconfigure(0, minsize=200)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()
