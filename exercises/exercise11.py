# 9-6
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = f"{self.name} has {self.cuisine_type} on the menu tonight!"
        print(msg)

    def open_restaurant(self):
        msg2 = f"{self.name} is open!"
        print(msg2)


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type="icecream"):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("We have the following flavors:")
        for flavor in self.flavors:
            print(f"{flavor.title()}")


icecream = IceCreamStand("IceCream Dream")
icecream.flavors = ["chocolate chip", "mint", "vanilla"]

icecream.describe_restaurant()
icecream.show_flavors()


# 9-7
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


class Admin(User):
    def __init__(self, first_name, last_name, age, gender, email):
        super().__init__(first_name, last_name, age, gender, email)
        self.privileges = ["can add post", "can delete post", "can ban user",
                           "can host server", "can use command prompt"]

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"{privilege}")


admin1 = Admin("sami", "king", "30", "female", "sking10@wsutech.edu")
admin1.describe_user()
admin1.show_privileges()


# 9-8
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


admin2 = Admin("sami", "king", "30", "female", "sking10@wsutech.edu",
               ["can add post", "can delete post", "can ban user",
                "can host server", "can use command prompt"])

admin2.privileges.show_privileges()


# Question 4: using your Horse objects from the encapsulation exercise, create
# your 2 child objects from the OOP section of the previous class. Use the property
# decorator for your child objects. Put both children objects inside your horse.py file
# See horse.py file
