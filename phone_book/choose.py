import read

print('what you want to do?\n1:read\n2:write')
j = input()
while j != 1 and j != 2 and j != '1' and j != '2':
    print('please enter correct operation!')
    j = input()
if j == 1 or j =='1':
    print(read.book_open())
elif j == 2 or j == '2':
    q = input('wich way you want to add?\n1:list\n2:line\n')
    while q != 1 and q != '1' and q != 2 and q != '2':
        print('please enter correct operation!')
        q = input('enter operation: ')
    if q == 1 or q == '1':
        print(read.book_write_list())
    elif q == 2 or q == '2':
        print(read.book_write_line())
