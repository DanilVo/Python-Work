from operator import truediv
import re

# class Braces:
    
#     def brace(a):
#         count = 0
#         dic = {
#             "(":")",
#             "[":"]",
#             "{":"}",
#             "<":">"
#         }
#         ls = list()
#         x = "".join(a)
#         for i in x:
#             if i == "(" or i == ")" or i == "[" or i == "]" or i == "[" or i == "]" or i == "{" or i == "}" or i == "<" or i == ">":
#                 ls.append(i) 
#         if len(ls) % 2 == 1:
#             return False
#         res = 0
#         while count <= len(ls):
#             if ls[count] in dic:
#                 return True
#             else:
#                 count += 1
# print(Braces.brace("<}a{+}(d*3)}>"))


def unique_in_order(l):
    if l == []:
        return l
    else:
        ret = [i for i in l]
        res = [ret[0]]
        count = 0
        for i in range(1,len(ret)):
            if res[count] == ret[i]:
                pass
            else:
                res.append(ret[i])
                count += 1
        return res
print(unique_in_order([]))