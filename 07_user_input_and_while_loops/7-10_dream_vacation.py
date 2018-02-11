investigation = {}
active = 1

# investigating
while active == 1:
    name = input("What's your name? ")
    if name == 'quit':
        active = 0
    else:
        place = input(
            "If you could visit one place in the world, where would you go? ")
        if place == 'quit':
            active = 0
        else:
            investigation[name] = place

# print the result
if investigation:
    for name, place in investigation.items():
        print(name.title() + " wants to visit " + place.title() + ".")
else:
    print("No one accepted the investigation.")
