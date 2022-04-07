from command import *


pro = tk.Tk()
pro.geometry('300x400')
pro.title('Project to porfolio')

name = tk.Label(pro, text='enter you name').grid(sticky='w')
entry_name = tk.Entry().grid(row=0,column=1)
password = tk.Label(pro, text='enter you password').grid()
entry_passwork = tk.Entry().grid(row=1,column=1)

enter = tk.Button(pro,text='Enter').grid()  # add (login_enter command)
register = tk.Button(pro,text='Registration',command=new_user).grid()


pro.mainloop()

# add in additional file: registration data 