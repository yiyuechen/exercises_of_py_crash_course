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


# def make_great(list):
#     while list:
#         name = list.pop()
#         name = "the great " + name
#         namelist.append(name)
#         #上面一行 BIG MISTAKE. 这样的话，相当于直接把great后的魔术师加到namelist中了，
#         #而原来里面就有三个魔术师
#         #而且还有一个错误：函数中的形参没有传入namelist，这是有问题的！

def make_great(list, namelist):
    namelist = []
    while list:
        name = list.pop()
        name = "the great " + name
        namelist.append(name)
        # 其实不传namelist进来namelist.append也能正常用全局变量工作，传进来是传了他的shadows进来
    return namelist
    # 必须返回，不然是shadows，只在函数内起作用


namelist = ['david', 'criss', 'qian']

show_magicians(namelist)

copiedlist = namelist[:]
namelist = make_great(copiedlist, namelist)
# make_great_0(namelist)

show_magicians(namelist)
