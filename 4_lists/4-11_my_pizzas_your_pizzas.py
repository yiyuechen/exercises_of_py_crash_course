# pizza
# think of three types of pizza. store them in a list
# print with for loop

pizzas = ['pizza a', 'pizza b', 'pizza c']
for pizza in pizzas:
    print("I like " + pizza.title())
print("I really like pizza")

# 创建一个披萨饼副本
friends_pizzas = pizzas[:]
friends_pizzas.append("New pizza")

print("My pizzas:")
for pizza in pizzas:
    print(pizza)

print("My friends' pizzas")
for pizza in friends_pizzas:
    print(pizza)
