# 创建多个字典，表示多个宠物
kitty = {
    'type': 'cat',
    'master': 'victor',
}

betty = {
    'type': 'dog',
    'master': 'romeo',
}

pets = [kitty, betty]

for pet in pets:
    print(pet)
