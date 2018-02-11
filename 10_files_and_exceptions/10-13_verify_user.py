import json

filename = "username.json"

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    with open(filename, 'w') as f_obj:
        username = input("What's your name? ")
        json.dump(username, f_obj)
        print("We'll remember you the next time you are back, " + username)
else:
    print("Welcome back, " + username)
