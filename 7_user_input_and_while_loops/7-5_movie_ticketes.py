while (1):
    age = input("How old are you? ")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Free")
    elif age <= 12:
        print("You should pay $10.")
    else:
        print("You should pay $15.")
