def get_city(city, country, population=''):
    """return a string containing 'city name comma country'"""
    if population:
        city_info = city + ', ' + country + ' - population ' + str(population)
    else:
        city_info = city + ', ' + country
    return city_info
