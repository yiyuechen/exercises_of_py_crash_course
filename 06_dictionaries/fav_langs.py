# 用嵌套在字典中的列表来表示一个人喜欢的不同的编程语言


fav_langs = {
    'jane': ['c', 'java'],
    'john': 'c',
    'joy': ['python', 'c'],
}

for name, lang in fav_langs.items():
    print(name + ' likes ' + str(lang))
