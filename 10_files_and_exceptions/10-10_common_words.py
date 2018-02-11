filename = 'war_and_peace.txt'

try:
    with open(filename) as filename_object:
        contents = filename_object.read()
except FileNotFoundError:
    print(filename + " was not found.")
else:
    # analyze how many words there are in the book
    words = contents.split()
    num_words = len(words)
    print("There are approximately " + str(num_words) + " words in " + filename)

    # count how many times a word appears in the book
    times = contents.lower().count('love')
    print("word 'love' appears "+ str(times)+" times in the book.")
