
# Name Case
name="ada lovelace"
print(name.upper())
print(name.lower())

#Using Variables in Strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = (f"Hello, {full_name.title()}!")
print(message)

#Adding Whitespace
#Tab
print("Python")
print("\tPython")

#Newline
print("Languages:\nPython\nC\nJavascript")

#Combine New Line and Tab
print("Languages:\n\tPython\n\tC\n\tJavascript")

#Stripping Whitespace
favorite_language = 'python '
print(favorite_language)
favorite_language.rstrip()
print(favorite_language)
print(favorite_language)

#Removing Prefixes
nostarch_url = 'https://nostarch.com'
nostarch_url.removeprefix('https://')

