# favorite number
import json

filename = 'favorite_number.json'

number=input("What's your favorite number? ")
with open(filename,'w') as f_object:
    json.dump(number,f_object)