from magician_def import show_magicians as sm, make_great as mg

namelist = ['david', 'criss', 'qian']

sm(namelist)

copiedlist = namelist[:]
namelist = mg(copiedlist, namelist)
# magician_def.make_great_0(namelist)

sm(namelist)
