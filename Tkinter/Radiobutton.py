import tkinter as tk

levels = {
    1: 'easy',
    2: 'medium',
    3: 'hard'
}

def select_lable():
    level = level_var.get()
    level_text.set(f'you choose {level} parametr')
    print(levels[level])

win = tk.Tk()
win.geometry('300x400')
win.title('RadioButton')

level_var = tk.IntVar()
level_text = tk.StringVar()

tk.Label(win,text="choose hardines").pack()
for level in levels:
    tk.Radiobutton(win,text=levels[level],variable=level_var,value=level,command=select_lable).pack()
tk.Label(win,textvariable=level_text).pack()


win.mainloop()



# nation_var = tk.IntVar()

# tk.Label(win,text="choose rase").pack()
# tk.Radiobutton(win,text='elf',variable=nation_var,value=4,command=select_lable).pack()
# tk.Radiobutton(win,text='human',variable=nation_var,value=5,command=select_lable).pack()
# tk.Radiobutton(win,text='ogre',variable=nation_var,value=6,command=select_lable).pack()