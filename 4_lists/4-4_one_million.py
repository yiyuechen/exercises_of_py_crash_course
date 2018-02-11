# create a list storing 1~1000000
# print with for loop

# 使用列表解析创建，注意这里for循环之前有一个number
# 如果要平方的话，那就是
# numbers=[number**2 for number in range(2_variables&simple_data_types,1000001)]

numbers = [number for number in range(1, 1000001)]
for number in numbers:
    print(number)
