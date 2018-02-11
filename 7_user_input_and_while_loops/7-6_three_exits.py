# 对于7_5,用active来控制循环

active = 1
while active:
    age = input("How old are you? ")
    if age == 'quit':
        active = 0
    else:
        age = int(age)

        if age < 3:
            print("Free")
        elif age <= 12:
            print("You should pay $10.")
        else:
            print("You should pay $15.")
