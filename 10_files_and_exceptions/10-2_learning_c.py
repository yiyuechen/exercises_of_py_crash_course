filename = 'readme'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.replace('，', '...')
    print(line)
