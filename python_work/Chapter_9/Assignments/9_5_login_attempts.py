class User:
    def __init__(self, first_name, last_name, username, email):
        """Initialize attributes for a user"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """Return neatly formatted information about a user"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
       
    def greet_user(self):
        """Greet the user personally."""
        print(f"Hello again, {self.first_name}!")

    def increment_login_attempts(self):
        """Count login attempts by one"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0  
       
user_one = User('Jackie', 'Kennedy', 'JaKennedy35', 'J.Kennedy@firstlady.gov')
user_one.describe_user()
user_one.greet_user()

print("\nMaking 3 login attempts...")
user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()
print(f" Login attempts: {user_one.login_attempts}")

print("Resetting login attempts...")
user_one.reset_login_attempts()
print(f"  Login attempts: {user_one.login_attempts}")

user_two = User('Barbara', 'Bush', 'BBush41', 'B.Bush@firstlady.gov')
user_two.describe_user()
user_two.greet_user()

print("\nMaking 3 login attempts...")
user_two.increment_login_attempts()
user_two.increment_login_attempts()
user_two.increment_login_attempts()
print(f" Login attempts: {user_two.login_attempts}")

print("Resetting login attempts...")
user_two.reset_login_attempts()
print(f"  Login attempts: {user_two.login_attempts}")

user_three = User('Nancy', 'Reagan', 'NReagan40', 'N.Reagan@firstlady.gov')
user_three.describe_user()
user_three.greet_user()

print("\nMaking 3 login attempts...")
user_three.increment_login_attempts()
user_three.increment_login_attempts()
user_three.increment_login_attempts()
print(f" Login attempts: {user_three.login_attempts}")

print("Resetting login attempts...")
user_three.reset_login_attempts()
print(f"  Login attempts: {user_three.login_attempts}")
