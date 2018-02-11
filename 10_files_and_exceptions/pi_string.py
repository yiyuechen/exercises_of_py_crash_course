# specify which file to open
file = 'pi_million_digits'

# open file as an object, then store all lines in an list, and assign the whole list to the 'lines' list
with open(file) as file_object:
    lines = file_object.readlines()

# create an empty string
pi_string = ''

# append each line to the empty string, but strip the space first
for line in lines:
    pi_string += line.strip()

# print the first ten chars
print(pi_string[:10])
# print the length of the whole string
print(len(pi_string))

birthday = input("Your birthday(e.g.20170101):")
if birthday in pi_string:
    print("It's in pi.")
else:
    print("Not in pi.")
