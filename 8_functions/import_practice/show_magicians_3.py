from magician_def import *

namelist = ['david', 'criss', 'qian']

show_magicians(namelist)

copiedlist = namelist[:]
namelist = make_great(copiedlist, namelist)
# magician_def.make_great_0(namelist)

show_magicians(namelist)
