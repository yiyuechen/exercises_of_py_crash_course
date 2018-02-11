# invite friends to dinner
# create a list to store friends' names
# then print their names

# add 3 people. one at the beginning of the list,one in the middle, and one at rear.

names = ['Xiu', 'Fei', 'Yong']
print("I'd like to invite ")
for name in names:
    print(name)
print(" to dinner")
print("But Yong won't come")
names[2] = "Chao"
print("So I will invite ")
print(names)

names.insert(0, 'Marxist')
names.insert(3, 'Linus')
names.append('Bill')
print(names)
