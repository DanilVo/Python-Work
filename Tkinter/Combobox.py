from calendar import weekday
import tkinter as tk
from tkinter import ttk

def show_day():
    print(f'{combo.get()},\n{combo_int.get()}')

weekdays = ("sunday", "monday", "thusday", "wednesday", "thurday", "friday", "saturday")
nums = [1,2,3,4,5]
win = tk.Tk()
win.geometry('300x400+800+150')
win.title('combobox')


combo = ttk.Combobox(win,values=weekdays)
# combo.set(weekdays[0])
combo.current(0)
combo.pack()

combo_int = ttk.Combobox(win,values=nums)
combo_int.pack()

ttk.Button(win,text='day name', command=show_day).pack()
combo_int.current(0)


win.mainloop()