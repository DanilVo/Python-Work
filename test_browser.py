# from colorama import Fore, Back, Style


# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')


# import webbrowser
# j = int(input())
# if j == 1:
#     webbrowser.open('http://net-informations.com/python/net/browser.htm#:~:text=Using%20the%20web%20browser%20in,and%20use%20open()%20function.')
# else:
#     print('no')



# def lengh(a):
#     return len(a)
# # b = ['a','b','c','d','e','f']
# f = map(lengh,('aeg','vdfvb','svfc','werfgwrfbvd','fve','af'))
# print(list(f))



# a = [1,2,3,4,5,6]
# c = list(filter(a,b))


def myfunc(a, b):
  return a+b

x = map(myfunc, ('apple', 'banana', 'cherry'),'apple', 'banana', 'cherry')
print(x)