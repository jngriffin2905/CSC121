def make_car(man_name, model_name, **car_info):
    """Build a dictionary of information about a car"""
    car_info['manufacturer'] = man_name
    car_info['model_name'] = model_name
    return car_info

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print()
print(car)
print()
    
    