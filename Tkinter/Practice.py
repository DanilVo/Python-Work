from cProfile import label
import tkinter as tk
# def counter():
#     global count
#     count+=1
#     btn1['text'] = f'count: {count}'
#     if count % 5 == 0:
#         btn2['bg'] = 'red'
#     else:
#         btn2['bg'] = 'green'

# def counter1():
#     global count1
#     count1+=1
#     btn2['text'] = f'count: {count1}'
#     lable = tk.Label(win,text=f'count: {count1}')
#     lable.pack()


# # def disable():
#     # global count1
#     # count1+=1
#     # if count1 % 5 == 0:
#     #     btn2['state'] = tk.DISABLED
#     # else:
#     #     btn2['state'] = tk.ACTIVE

# count = 0
# count1 = 0


# win = tk.Tk()
# win.geometry('300x400+200+300')

# btn1 = tk.Button(win,text=f'count: {count}',
# command=counter)

# btn2 = tk.Button(win,text=f'count: {count1}',
# command=counter1)

# btn1.pack()
# btn2.pack()
# win.mainloop()





open = tk.Tk()
open.title('rows and columns')
open.geometry('400x300+100+200')

# btn1 = tk.Button(open,text='hello 1')
# btn2 = tk.Button(open,text='hello 2')
# btn3 = tk.Button(open,text='hello 3')
# btn4 = tk.Button(open,text='hello 4')
# btn5 = tk.Button(open,text='hello 5')
# btn6 = tk.Button(open,text='hello 6')
# btn7 = tk.Button(open,text='hello 7')

for i in range (5):
    for j in range(2):
        tk.Button(open,text=f'{i}{j}').grid(row=i,column=j)


# btn1.grid(row=0,column=0,stick='we')
# btn2.grid(row=0,column=1,stick='we')
# btn3.grid(row=1,column=0,stick='we')
# btn4.grid(row=1,column=1)
# btn5.grid(row=2,column=0,stick='we')
# btn6.grid(row=2,column=1)
# btn7.grid(row=3,column=0,columnspan=2,stick='we')

# open.grid_columnconfigure(0,minsize=200)

open.mainloop()