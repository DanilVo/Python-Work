import tkinter as tk
from turtle import left

win = tk.Tk()
win.geometry(f"300x400+100+200")
win.title("First widget")

label_1 =tk.Label(win, text='''Hello!
world!''',
bg='red',  # change background color
fg='white',  # change words (front) color
font=('Arial',15,'bold'),  # set words size and text type
# padx=20, # size of label (the colored part) by X
# pady=40,  # size of label (the colored part) by y
width=20,  # same as (pad) but in chars
height=10,  # same as (pad) but in chars
anchor='s', # where text will be showed (north, east,west,south (by first letter))
relief=tk.RAISED,  #  will show lable borders
bd=10,  # size of the borders
justify=tk. RIGHT # set placement of text
)
label_1.pack() # adds information to display

win.mainloop()