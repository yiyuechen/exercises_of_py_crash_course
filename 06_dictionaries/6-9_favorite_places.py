# create a dictionary
favorite_places = {
    'I': ['Shanghai', 'Beijing', 'Nanjing'],
    'James': ['Nanjing', 'Changsha', 'Tianjing'],
    'Claire': ['Beijing', "Xi'an", 'Nanjing'],
}

# 在字典中添加一个人物和她喜欢的多个地方（列表）
favorite_places['Alice'] = []
value = input("Hey Alice, what's your favorite places?" +
              " Tell me one by one: ")
favorite_places['Alice'].append(value)
more_flag = 1
while more_flag:
    value = input("And more? Type n to cancel. ")
    if value == 'n':
        more_flag = 0
    else:
        favorite_places['Alice'].append(value)

# 打印所有人，以及他们喜欢的位置
for person, fav_places in favorite_places.items():
    print(person + "'s favorite places are: ")
    for place in fav_places:
        print("-:" + place)
