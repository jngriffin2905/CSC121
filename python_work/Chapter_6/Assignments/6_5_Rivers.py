# Assignment: 6-5 Rivers
# Author:Jessica Griffin
# Date: February 23, 2025 
print()

# A message for all rivers 
rivers = {'nile' : 'egypt', 'mississippi' : 'eastern united states', 'volga' : 'russia'}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

print()

# Each river in dictionary
for river in rivers.keys():
    print(river.title())

print()

# Each Country in dictionary
for river in rivers. values():
    print(river.title())




