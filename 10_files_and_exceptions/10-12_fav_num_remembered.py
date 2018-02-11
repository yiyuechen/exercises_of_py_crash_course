# favorite number
import json

filename = 'favorite_number_1.json'

try:
    with open(filename) as f_object:
        number = json.load(f_object)
except FileNotFoundError:
    number = input("What's your favorite number? ")
    with open(filename, 'w') as f_object:
        json.dump(number, f_object)
else:
    print("Your favorite number: " + number)
