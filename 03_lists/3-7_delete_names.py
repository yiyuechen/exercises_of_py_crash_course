# invite friends to dinner
# create a list to store friends' names
# then print their names

# add 3 people. one at the beginning of the list,one in the middle, and one at rear.

# pop people till there are merely 2 left. One pop one appology. And tell the left 2 they are still invited.
# delete the last 2 from the list

names = ['Xiu', 'Fei', 'Yong']
print("I'd like to invite ")
for name in names:
    print(name)
print(" to dinner")
print("But Yong won't come")

# to change list value Yong to PanChao
names[2] = "Chao"
print("So I will invite ")
print(names)

# to add members
names.insert(0, 'Marxist')
names.insert(3, 'Linus')
names.append('Bill')
print(names)

# pop till 2 left
print(
    "sorry " + names.pop() + ". I cannot invite you tonight. Maybe next time.")
print("sorry " + names.pop())
print("sorry " + names.pop())
print("sorry " + names.pop())

print(names)

print("Dear " + names[0] + ", do come please.")
print("Dear " + names[1] + ", do come please.")

# del all member of names list
del names[0]

# WARNING
# After the del above, there is only one element in the list
del names[0]

print(names)
