# 先创一个列表
current_users = ['Victor', 'edward', 'joy', 'priscilla']
# 创建另一个，确保其中有两个在上面的列表中
new_users = ['VICTOR', 'claire', 'Joy', 'jane', 'jack']

print("--------------------------")
# 传统方法
# 尚未解决
for new_user in new_users:
    for current_user in current_users:
        if (new_user.lower() == current_user.lower()):
            print("Sorry, but " + new_user + " is registered.")
            break
    print(new_user + " is available.")
    # 上面这一行显然是不对的，因为不管里面的for循环是break出来还是自然结束，
    # 都会执行这句print，这就导致了既提示registered，又提示available

print("--------------------------")

# 下面使用标志法
for new_user in new_users:
    is_registered = 0
    for current_user in current_users:
        if (new_user.lower() == current_user.lower()):
            is_registered = 1
    if (is_registered == 1):
        print("Sorry, but " + new_user + " is registered.")
    else:
        print(new_user + " is available.")

print("--------------------------")
# 另一种方法，暂时有问题。因为current_users里的不能转化为小写。
# 这就是我一开始不使用此方法的原因。
for new_user in new_users:
    if new_user.lower() in current_users:
        print("Sorry, but " + new_user + " is registered.")
    else:
        print(new_user + " is available.")
