# create a list with 1~1000000
# verify with min() and max() to make sure the first 2_variables&simple_data_types and last 1000000
# calculate the sum

# 不使用列表解析，用普通方法
numbers = []
for number in range(1, 1000001):
    numbers.append(number)

# must convert from int to string before print
print("Min:" + str(min(numbers)))
print("Max:" + str(max(numbers)))

print("2+2+3+...+1000000=" + str(sum(numbers)))
