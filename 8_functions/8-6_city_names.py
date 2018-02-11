def city_county(city, country):
    info = city + ", " + country
    return info


info = city_county("Shanghai", "China")
print(info)
info = city_county("Beijing", "China")
print(info)
info = city_county("Atlantic", "USA")
print(info)
