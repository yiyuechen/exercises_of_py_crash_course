def make_sandwich(*ingredients):
    print("You want to add:")
    for ingredient in ingredients:
        print("- " + ingredient)


make_sandwich('hotdog', 'paper', 'orange', 'beauty')
