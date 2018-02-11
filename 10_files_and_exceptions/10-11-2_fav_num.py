# favorite number
import json

filename = 'favorite_number.json'

with open(filename) as f_object:
    number=json.load(f_object)
    print("Your favorite number: "+number)