sandwich_orders = [
    'pastrami', 'british sandwich',
    'pastrami', 'american sandwich',
    'pastrami', 'chinese sandwich'
]

print("pastrami are sold over.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
