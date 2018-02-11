import json


def get_stored_username():
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    with open(filename, 'w') as f_obj:
        username = input("What's your name? ")
        json.dump(username, f_obj)
        print("We'll remember you the next time you are back, " + username)


def check_username():
    # ask the current user to offer its name, if the name equals to the name
    # stored in json,
    # we know it's the same person; if not, we'll know it's a new user
    with open(filename, 'r') as f_obj:
        stored_username = json.load(f_obj)
        current_username = input("What's your name? "
                                 "We already have a user now. ")
        if stored_username == current_username:
            print("Welcome back, " + stored_username)
        else:
            with open(filename, 'w') as f_obj:
                json.dump(current_username, f_obj)
                print("We'll remember you the next time you are back, "
                      + current_username)


def greet_user():
    username = get_stored_username()
    # if we have username stored in json
    if username:
        # call check_username
        check_username()
    # if there are no username in json file, this is the first time a user shows up
    else:
        get_new_username()


filename = "username1.json"
greet_user()
