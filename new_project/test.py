def swap(n):
    ls =[]
    x = n.split()    

    print(n)
    print(x)
    print(sorted([x[i][len(x[i])-1] for i in range(len(x))]))
swap("man i need a taxi up to ubud")

# def swap(n):
#     x = n.split()
#     for i in x:
#         print(i[len(i)-1])
# swap("man i need a taxi up to ubud")