motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#Change the name of an item in the list
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding an item to the list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# adding to an empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Adding new element at any position
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing elements from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# Removing an item using pop
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned= motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Popping from any position
motorcycles = ['honda', 'yamaha', 'suzuki']


# Removing a value from the list
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# Removing then explaining
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# Avoiding Index errors when workig with lists
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])

motorcycles = []
print(motorcycles[-1])