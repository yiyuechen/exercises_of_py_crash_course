# Make a list called sandwich_orders and fill it with the names of vari-
# ous sandwiches. Then make an empty list called finished_sandwiches . Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.
sandwich_orders = ['british sandwich', 'american sandwich', 'chinese sandwich']
finished_sandwiches = []

while sandwich_orders:
    current = sandwich_orders.pop()
    finished_sandwiches.append(current)
    print("I made your " + current + ".")

print("We made the following sandwiches:")
for finished_sandwich in finished_sandwiches:
    print("\t" + finished_sandwich)
