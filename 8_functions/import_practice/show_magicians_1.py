import magician_def as md

namelist = ['david', 'criss', 'qian']

md.show_magicians(namelist)

copiedlist = namelist[:]
namelist = md.make_great(copiedlist, namelist)
# magician_def.make_great_0(namelist)

md.show_magicians(namelist)
