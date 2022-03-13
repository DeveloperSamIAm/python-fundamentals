# separate import file for Lab Exercise 13

def favorite_book(title):
    """Display the users favorite book."""
    print(f"{title} is one of my favorite books.")


class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = f"{self.name} has {self.cuisine_type} on the menu tonight!"
        print(msg)


class User:
    def __init__(self, first_name, last_name, age, gender, email):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.age = age
        self.gender = gender
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")
        print(f"Age:{self.age}")
        print(f"Gender:{self.gender}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, this is your personalized greeting!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"{privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, gender, email, privileges):
        super().__init__(first_name, last_name, age, gender, email)
        self.privileges = Privileges(privileges)
