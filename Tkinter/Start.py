import tkinter as tk

win = tk.Tk() # start working at tk
win.title('first run') # program name (at title)
win.geometry('500x600+100+200')  # Size of our window (+= is where to locate the window)
# win.minsize(300,400)  # Minimum size of the window
# win.maxsize(600,800)  # Maximum size of the window
win.resizable(True,True)  # allows us to resize widow (hight,width)
win.mainloop() # loop in order to run our program