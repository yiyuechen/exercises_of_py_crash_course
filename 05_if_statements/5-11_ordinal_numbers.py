# 序数位置

# 创建一个包含十个数字的列表
nums = []
for num in range(1, 10):
    nums.append(num)

for num in nums:
    print(num)

for num in nums:
    if (num == 1):
        print("1st")
    elif (num == 2):
        print("2nd")
    else:
        print(str(num) + "th")
