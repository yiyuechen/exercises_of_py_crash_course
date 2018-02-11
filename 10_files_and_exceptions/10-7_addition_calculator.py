active = 1

while active:
    a = input("Enter a number: ")
    if a != 'q':
        b = input("Enter another number: ")
        if b != 'q':
            try:
                sum = int(a) + int(b)
                print("The summary is " + str(sum))
            except ValueError:
                print("You didn't enter a number")
        else:
            active = 0
    else:
        active = 0
