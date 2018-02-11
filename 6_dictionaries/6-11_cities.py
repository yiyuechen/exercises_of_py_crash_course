cities = {
    'Wuhan': {
        'country': 'china',
        'population': '1000',
        'description': 'beautiful',
    },
    'Beijing': {
        'country': 'china',
        'population': '10000',
        'description': 'cosmopolitan',
    },
    'Shanghai': {
        'country': 'china',
        'population': '200',
        'description': 'prosperous'
    },
}

print(cities)

for city, info in cities.items():
    print(city.title() + " is in " + info['country'] + ". " +
          "Population: " + info['population'] +
          ". It's " + info['description'] + ".")
