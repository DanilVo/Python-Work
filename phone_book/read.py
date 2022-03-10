

def book_open():
    data = open('book.csv', 'r')
    for line in data:
        print(line)
    data.close()

def book_write_list():
    data = open('book.csv', 'a')
    data.write(f"\nname: {input('enter name: ')}\n")
    data.write(f"last name :{input('enter last name: ')}\n")
    data.write(f"phone number: {input('enter phone number: ')}\n")
    data.write(f"status: {input('enter phone status: ')}\n")
    data.close()

def book_write_line():
    data = open('book.csv', 'a')
    data.write(f"\nname: {input('enter name: ')}")
    data.write(f" last name: {input('enter last name: ')}")
    data.write(f" phone number: {input('enter phone number: ')}")
    data.write(f" status: {input('enter phone status: ')}")
    data.close()