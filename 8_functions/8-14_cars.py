# car_info receives key,value
def build_car_info(manufacturer, model, **other_car_info):
    car_info = {}
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    for key, info in other_car_info.items():
        car_info[key] = info
    return car_info


info = build_car_info('audi', '2017 summer', type='sport', speed='fast',
                      price='$850000', color='blue')
print("Here is your car:")
for key, value in info.items():
    print(key + "\n- " + value)
