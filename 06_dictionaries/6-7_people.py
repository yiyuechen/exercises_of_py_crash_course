jane = {
    'first_name': 'Jane',
    'last_name': 'Eyre',
    'age': '20',
    'city': 'england',
}

for key, value in jane.items():
    print(key + " - " + value)

jack = {
    'first_name': 'Jack',
    'last_name': 'Dawson',
    'age': '25',
}

rose = {
    'first_name': 'Rose',
    'last_name': 'Dawson',
    'age': 'unknown',
}

people = [jane, jack, rose]

for person in people:
    print(person)
