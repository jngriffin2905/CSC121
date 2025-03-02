# Writing clear prompts

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you tell me your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")