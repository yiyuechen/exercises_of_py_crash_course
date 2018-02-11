import magician_def

namelist = ['david', 'criss', 'qian']

magician_def.show_magicians(namelist)

copiedlist = namelist[:]
namelist = magician_def.make_great(copiedlist, namelist)
# magician_def.make_great_0(namelist)

magician_def.show_magicians(namelist)
