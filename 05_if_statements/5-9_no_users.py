# create a user list including admin
users = ['admin', 'edward', 'jason', 'jack', 'darcy']


# 确定列表不是空的
def print_users():
    if users:
        for user in users:
            if user != 'admin':
                print("Hello " + user + ", Welcome again.")
            else:
                print("Hello admin. Want to check the status report?")
    else:
        print("We need users.")


print_users()

# delete all users
print("deleting all users...")

while users:
    del users[0]

print("Now the users list is:")
# print list users
print(users)
# print all users
print_users()
