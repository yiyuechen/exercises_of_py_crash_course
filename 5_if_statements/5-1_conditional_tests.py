# 条件测试

name = 'Jenny'
print("Is name == 'jenny' I predict true.")

# 注意下面这种表达，+和==，==的优先级更高，如果我直接写成
# print("The result:"  + name.lower() == 'jenny')
# 那么The result会先和name.lower()结合，再去判断和jenny等不等
# print("The result:"  + str(name.lower() == 'jenny'))

print(name.lower() == 'jenny')
