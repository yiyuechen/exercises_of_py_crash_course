def show_magicians(namelist):
    for name in namelist:
        print(name)


# namelist is shadow, not the real one from outer space
def make_great_0(namelist):
    templist = namelist[:]
    while namelist:  # here namelist is not shadow
        namelist.pop()
    while templist:
        name = templist.pop()
        name = "the great " + name
        namelist.append(name)  # here namelist doing append is not shadow!


def make_great(list, namelist):
    namelist = []
    while list:
        name = list.pop()
        name = "the great " + name
        namelist.append(name)
        # 不传namelist进来namelist.append也能正常用全局变量工作，之所以传是为了传他的shadows进来
        # 不传的话，就会显示namelist未定义，因为namelist不在这个文件，而是在show_magician.py中
    return namelist
    # 必须返回，不然是shadows，只在函数内起作用
