

# users = []
# data = open('book.csv', 'r')
# data.close()

def book_open():
    path = 'book.csv'
    data = open(path, 'r')
    for line in data:
        print(line)
    data.close()
