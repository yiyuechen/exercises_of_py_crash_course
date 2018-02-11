filename = 'guest_book.txt'
active = 1

while active:
    name = input("Enter your name: ")
    if name != 'quit':
        print("Welcome, " + name)
        with open(filename, 'a') as file_object:
            info = name + " visited.\n"
            file_object.write(info)
    else:
        active = 0
