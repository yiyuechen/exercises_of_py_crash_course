# create user profile, with a parameter
# that can receive as many piece of info as you want
# return a dictionary


def build_profile(first_name, last_name, **info):
    profile = {}
    profile['first name'] = first_name
    profile['last name'] = last_name
    for key, value in info.items():
        profile[key] = value
    return profile


profile = build_profile("jane", "eyre", age="20", location="england",
                        gender='female')
print("Here is the infomation:")
for key, value in profile.items():
    print(key.title() + "\n- " + value.title())
