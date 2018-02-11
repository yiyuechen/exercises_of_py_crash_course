# favoirte number
names = {
    'jane': [1, 2, 5],
    'lara': [4, 2, 1],
    'camilla': [2, 1, 7],
}
for name, nums in names.items():
    check = input("Is " + name + " your name? y/n ")
    if check == 'y':
        print(name + "'s numbers are ")
        for num in nums:
            print(str(num))
