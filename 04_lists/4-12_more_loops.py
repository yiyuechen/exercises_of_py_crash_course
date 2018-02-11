# 使用多个for循环

mine = ['pizza', 'falafel', 'carrot cake']
friends = mine[:]

for m in mine:
    for f in friends:
        print(m + " versus " + f)
