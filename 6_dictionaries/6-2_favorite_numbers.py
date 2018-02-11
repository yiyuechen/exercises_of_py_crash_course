# favoirte number
names = {'jane': 1, 'lara': 4, 'camilla': 2}
for name, num in names.items():
    check = input("Is " + name + " your name? y/n ")
    if check == 'y':
        print(name + "'s number is " + str(num))
