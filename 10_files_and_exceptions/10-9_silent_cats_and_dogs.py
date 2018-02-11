def read_pets(filename='cats.txt'):
    try:
        with open(filename) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        pass
    else:
        for line in lines:
            print(line.rstrip())


read_pets('dogs.txt')
read_pets('horse.txt')
