a = input("Enter a number: ")
b = input("Enter another number: ")

try:
    sum = int(a) + int(b)
    print("The summary is " + str(sum))
except ValueError:
    print("You didn't enter a number")


