def show_magicians(namelist):
    for name in namelist:
        print(name)


# namelist on the next line is shadow, not the real one from outer space
def make_great(namelist):
    templist = namelist[:]
    while namelist:
        namelist.pop()
    while templist:
        name = templist.pop()
        name = "the great " + name
        namelist.append(name)
    return namelist


namelist = ['david', 'criss', 'qian']

print(namelist)  # print original

new_namelist = make_great(
    namelist[:])  # When we copy, should be "new = old[:]". What about here?

print(namelist)  # print again, should be the same

print(new_namelist)
