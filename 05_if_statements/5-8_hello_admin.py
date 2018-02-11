# create a user list including admin
users = ['admin', 'edward', 'jason', 'jack', 'darcy']

for user in users:
    if user != 'admin':
        print("Hello " + user + ", Welcome again.")
    else:
        print("Hello admin. Want to check the status report?")
