# Working with loops
# for magicians(variable) in magicians(list name)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# Printing a message 
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I cant wait to see your next trick, {magician.title()}.\n")

# Multiple lines
magicians = ['alice', 'davud', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I cant wait to see your next trick, {magician.title()}.\n")
# all indented print statements aree in the loop

# Doing something after a for loop
magicians = ['alice', 'davud', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I cant wait to see your next trick, {magician.title()}.\n")
    
print("Thank you, evreyone. That was a great magic show!")

