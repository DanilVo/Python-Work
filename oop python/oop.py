
# class Point:
#     color = 'red'
#     circle = 2

#     def set_cords(self,x,y):
#         self.x = x
#         self.y = y

#     def get_cords(self):
#         return (self.x,self.y)

# pt = Point()
# # pt2 = Point()

# pt.set_cords(1,2)
# print(pt.__dict__)
# # pt2.set_cords(10,20)

# f = getattr(pt, 'get_cords')
# print(f())

# # class Point:
# #     pass

# #     def set_cord(self):
# #         print("hello world")

# # pt = Point()
# # pt.set_cord()
# # Point.set_cord(pt)

# class MediaPlayer:
    
#     def open(self, file):
#         self.file = file

#     def play(self):
#         print("Воспроизведение " + str(self.file))

# media1 = MediaPlayer()
# media2 = MediaPlayer()

# media1.open("filemedia1")
# media2.open("filemedia2")

# media1.play()


# class Graph:

#     LIMIT_Y = [0,10]

#     def set_data(self,data):
#         self.data = data

#     def draw(self):
#         ls = []
#         for i in self.data:
#             if self.LIMIT_Y[0] <= i <= self.LIMIT_Y[1]:
#                 ls.append(i)
#         mystr = " ".join(map(str,ls))
#         print(mystr)        

# graph_1 = Graph()

# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# graph_1.draw()
# -----------------------------------------------------------------------------------------#
# import sys

# class StreamData:
    
#     def create(self, fields, lst_values):
#         if len(fields) != len(lst_values):
#             return False
        
#         for i, key in enumerate(fields):
#             setattr(self, key, lst_values[i])
#         return True
    

# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')

#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res

# sr = StreamReader()
# data, result = sr.readlines()
# -----------------------------------------------------------------------------------------#
# import sys

# # программу не менять, только добавить два метода
# sys.stdin = open('text.txt', 'r', encoding='utf-8')
# lst_in = list(map(str.strip, sys.stdin.readlines()))   # считывание списка строк из входного потока


# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')

#     def insert(self, data):
#         spl = [i.split() for i in data]
#         for i in range(len(spl)):
#             for j in range(len(self.FIELDS)):
#                 self.lst_data.append(dict({f"{self.FIELDS[j]}":f"{spl[i][j]}"}))
#             self.lst_data.append(dict)

#     def select(self,a,b):
#         if b > len(self.lst_data):
#             print(self.lst_data[a:len(self.lst_data)])
#         else:
#             print(self.lst_data[a:b + 1])

# db = DataBase()
# db.insert(lst_in)
# db.select(1,4)
# -----------------------------------------------------------------------------------------#


# class Translator:

#     def add(self, eng, rus):
#         if hasattr(self,eng) == True:
#             a = getattr(self,eng)
#             setattr(self,eng,f'{rus} {a}')
#         else:
#             setattr(self,eng,rus)

        
#     def remove(self,eng):
#         delattr(self,eng)


#     def __str__(self):
#         obj = getattr(self)
#         li = list(obj.split(" "))
#         return li
        

# tr = Translator()

# # tr+("tree", "дерево")

# tr.add("tree", "дерево")
# tr.add("car", "машина")
# tr.add("car", "автомобиль")
# tr.add("leaf", "лист")
# tr.add("river", "река")
# tr.add("go", "идти")
# tr.add("go", "ехать")
# tr.add("go", "ходить")
# tr.add("milk", "молоко")
# tr.remove("car")
# print(tr)

# ls = list()
          #-----------------------------------------------------------------------------------------#
# class Point:
#     color = 'red'
#     circle = 2

#     def __init__(self,a,b):
#         print("call __init__")
#         self.x = a
#         self.y = b
        

#     def set_cords(self,x,y):
#         self.x = x
#         self.y = y

#     def get_cords(self):
#         return self.x,self.y


from random import randint


class Line:
    def __init__(self,a,b,c,d):
        self.sp = (a,b)
        self.ep = (c,d)

class Rect:
    def __init__(self,a,b,c,d):
        self.sp = (a,b)
        self.ep = (c,d)

class Ellipse:
    def __init__(self,a,b,c,d):
        self.sp = (a,b)
        self.ep = (c,d)
        

elements = [(Line,Rect,Ellipse)[randint(0,2)](1,2,3,4) for n in range(217)]
for obj in elements:
    if isinstance(obj,Line):
        obj.sp = obj.ep =0,0
        print(elements)