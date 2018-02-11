# think of 5 places to go
places = ["Xi'an", "QingYang", "Lanzhou", "Beijing", "Shanghai"]

# print original list
print("Here is the original list:")
print(places)
print("\n")

# print using sorted() function
print("After using sorted() function:")
print(sorted(places))
print("\n")

# print original list to check if the sequence is changed
print("Here is the original list:")
print(places)
print("\n")

# print using sorted() function, but reversing
print("After using sorted() function, reversed:")
print(sorted(places, reverse=True))
print("\n")

# print original list
print("Here is the original list:")
print(places)
print("\n")

# using reverse() method to reverse
print("After reverse() method:")
places.reverse()
print(places)
# WRONG#
# print(places.reverse())
# END#
print("\n")

# print list, we will discover the list order has changed.
print("Here is the original list:")
print(places)
print("\n")

# using reverse() method to reverse back to original list
print("After reverse() method, to reverse back:")
places.reverse()
print(places)
print("\n")

# we will discover the list order has changed back to original.
print("check if it's reversed back:")
print(places)
print("\n")

# change the sequence using sort() method then print
print("Original list after sort() method:")
places.sort()
print(places)
print("\n")

# change the sequence using sort() method but reverse
print("Original list after sort() method, reverse:")
places.sort(reverse=True)
print(places)
print("\n")
