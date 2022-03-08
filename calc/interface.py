import mathematical

# a = 0
# b = 0

oper = input('chose operation:+,-,*,/ \n')
while oper != '+' and oper != '-' and oper != '*' and oper != '/':
    print('please enter operation!')
    oper = input('chose operation:+,-,*,/ \n')
a = int(input('enter first number: '))
b = int(input('enter second number: '))
if oper == '-':
    print(mathematical.minus(a, b))
elif oper == '+':
    print(mathematical.plus(a, b))
elif oper =='/':
    print(mathematical.division(a, b))
elif oper == '*':
    print(mathematical.multiply(a, b))



# if oper is not '+' or '-' or '*' or '/':
#     print('please enter operation!')
#     print('chose operation:+,-,*,/ ')
#     oper = input()
# a = int(input())
# b = int(input())