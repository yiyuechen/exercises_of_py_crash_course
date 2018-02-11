def make_shirt(size='xxl', words='I love python'):
    print("The size is " + size + ". The words are \"" + words + "\".")


print("Default: ")
make_shirt()

print("Customized: ")
size = input("What size? ")
words = input("What to print? ")

make_shirt(size, words)
