# 9_3 Users

class User:
    def __init__(self, first_name, last_name, username, email):
        """Initialize attributes for a user"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email

    def describe_user(self):
        """Return neatly formatted information about a user"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
       
    
    def greet_user(self):
        """Greet the user personally."""
        print(f"Hello again, {self.first_name}!")
       
user_one = User('Jackie', 'Kennedy', 'JaKennedy35', 'J.Kennedy@firstlady.gov')
user_one.describe_user()
user_one.greet_user()

user_two = User('Barbara', 'Bush', 'BBush41', 'B.Bush@firstlady.gov')
user_two.describe_user()
user_two.greet_user()

user_three = User('Nancy', 'Reagan', 'NReagan40', 'N.Reagan@firstlady.gov')
user_three.describe_user()
user_three.greet_user()
