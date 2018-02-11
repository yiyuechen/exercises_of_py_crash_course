string1 = 'c'
string2 = 'python'
print("Is string1 == string2?")
print(string1 == string2)
print('\n')

number1 = 4
number2 = 6
print("is num1 == num2 or what?")
print(number1 == number2)
print("\n")

# 判断一个值在不在列表里
langs = ['c', 'python', 'java', 'cpp']
lang = 'c'

if lang in langs:
    print(lang.title() + " is in langs")

lang1 = 'php'
if lang1 not in langs:
    print(lang.title() + " is not in langs")

# 测试字典在不在里面
'''
users={'jane':18,'claire':20,'mary':21}
user=jane
if user in users:
    print("In")
有问题，编译错误
'''
