import json


def get_username():
    with open(filename) as f_obj:
        username = json.load(f_obj)
        return username


def get_new_username():
    with open(filename, 'w') as f_obj:
        username = input("What's your name? ")
        json.dump(username, f_obj)
        print("We'll remember you the next time you are back, " + username)


def greet_user():
    try:
        username = get_username()
    except FileNotFoundError:
        get_new_username()
    else:
        print("Welcome back, " + username)


filename = "username1.json"
greet_user()
