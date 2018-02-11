# 元组的练习

foods = ('rice', 'chicken', 'cake', 'juice', 'water')
print("original:")
for food in foods:
    print(food)
# foods[0]='fish'    不可行


# 给存储元组的变量重新赋值
foods = ('rice', 'chicken', 'water')
print("modified:")
for food in foods:
    print(food)
