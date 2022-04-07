from distutils.errors import CompileError
import tkinter as tk


def select_all():
    for check in [over_18, commercial, follow]:
        check.select()


def deselect_all():
    for check in [over_18, commercial, follow]:
        check.deselect()


def switch_all():
    for check in [over_18, commercial, follow]:
        check.toggle()

def show():
    print('flag 18', over_18_value.get())
    print('commercial', commercial_value.get())

win = tk.Tk()
win.title("check")

over_18_value = tk.StringVar()
over_18_value.set('No')
over_18 = tk.Checkbutton(win, text='are you over 18?',
                         variable=over_18_value,
                         offvalue='No', 
                         onvalue="yes"
                         )

commercial_value = tk.IntVar()
commercial = tk.Checkbutton(win, text='adds?',
                         variable=commercial_value,
                         offvalue=0, 
                         onvalue=1
                         )

follow = tk.Checkbutton(win, text='foolow channel?', indicatoron=0)
over_18.pack()
commercial.pack()
follow.pack()

tk.Button(win, text='select_all', command=select_all).pack()
tk.Button(win, text='deselect_all', command=deselect_all).pack()
tk.Button(win, text='switch', command=switch_all).pack()
tk.Button(win, text='show', command=show).pack()


win.geometry('300x400')
win.mainloop()
