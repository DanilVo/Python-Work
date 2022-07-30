from command import *
from work_page import *



def entery():
    win = open('registration_data.csv', 'r')
    for line in win:
        line.split(' ')
        print(line.split([1]))
    

pro = tk.Tk()
pro.geometry('300x400')
pro.title('Project to porfolio')

name = tk.Label(pro, text='enter you name').grid(sticky='w')
entry_name = tk.Entry()
entry_name.grid(row=0,column=1)
password = tk.Label(pro, text='enter you password').grid()
entry_passwork = tk.Entry()
entry_passwork.grid(row=1,column=1)

enter = tk.Button(pro,text='Enter', command=entery).grid()  # add (login_enter command)
register = tk.Button(pro,text='Registration',command=new_user).grid()
tk.Button(pro, text="close", command=pro.quit).grid(row=4,column=0)



pro.mainloop()

# add in additional file: registration data 