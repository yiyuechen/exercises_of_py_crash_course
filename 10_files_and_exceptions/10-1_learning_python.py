filename='readme'

with open(filename) as file_object:
    content = file_object.read()


print(content)
print("-------------------------")

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

print("-------------------------")
with open(filename) as file_object:
    for value in file_object:
        print(value)
