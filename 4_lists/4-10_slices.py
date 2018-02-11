# 练习切片

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The first three are:")
for num in nums[:3]:
    print(num)

print("Three items from the middle of the list are:")
for num in nums[4:7]:
    print(num)

print("The last three items in the list are:")
for num in nums[-3:]:
    print(num)
