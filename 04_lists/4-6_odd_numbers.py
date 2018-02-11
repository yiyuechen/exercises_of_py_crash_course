# create a list with odd numbers
# 通过指定range()函数的第三个参数

# 列表解析创建list
odds = [number for number in range(1, 21, 2)]
for odd in odds:
    print(odd)
