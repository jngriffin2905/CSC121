favorite_places = {
    'joe' : ['gamestop', 'target', 'red lobster'],
    'zack' : ['the beach', 'best buy', 'gamestop'],
    'jessica' : ['panama city', 'red lobster', 'movies']
    }
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")

   
