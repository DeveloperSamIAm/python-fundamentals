# Lab Exercise 9 Functions and Classes

# 8-3
def make_shirt(size, text):
    print(f"{size} shirt")
    print(f"The shirt will say {text}")


make_shirt("medium", "Coding is awesome!")
make_shirt(size="large", text="Coding is cool when you are part of a team")


# 8-4
def make_shirt2(size="large", text="I love Python"):
    print(f"{size} shirt")
    print(f"The shirt will say {text}")


make_shirt2()
make_shirt2(size="medium")
make_shirt2(size="small", text="Coding is cool when you are part of a team")


# 8-5
def describe_city(city_name, city_country="united states"):
    print(f"{city_name.title()} is in {city_country.title()}")


describe_city("Wichita")
describe_city("Denver")
describe_city("Berlin", "Germany")


# 8-9
messages1 = ["hey how are you today?", "want to play video games?", "pizza for dinner tonight", "omw home"]


def show_messages1():
    for message in messages1:
        print(message)


show_messages1()


# 8-10
messages2 = ["hey how are you today?", "want to play video games?", "pizza for dinner tonight", "omw home"]
sent_messages2 = []


def show_messages2():
    while messages2:
        unsent_messages = messages2.pop()
        print(f"Sending message: {unsent_messages}")
        sent_messages2.append(unsent_messages)

    print("The following text messages have been sent:")
    for sent_message in sent_messages2:
        print(sent_message)


show_messages2()


# 8-11

messages3 = ["hey how are you today?", "want to play video games?", "pizza for dinner tonight", "omw home"]
sent_messages3 = []


def show_messages3(messages3, sent_messages3):
    while messages3:
        unsent_messages = messages3.pop()
        print(f"Sending message: {unsent_messages}")
        sent_messages3.append(unsent_messages)

    print("The following text messages have been sent:")
    for sent_message in sent_messages3:
        print(sent_message)


show_messages3(messages3[:], sent_messages3)
print(messages3)
print(sent_messages3)


# 9-1
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


restaurant = Restaurant("Send Noodles", "noodles")
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9-2
class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = f"{self.name} has {self.cuisine_type} on the menu tonight!"
        print(msg)


restaurant1 = Restaurant("Sushi Time", "sushi")
restaurant2 = Restaurant("Pasta Mama", "italian")
restaurant3 = Restaurant("Juicy Lucy", "burgers")


restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


# 9-3
class User:
    def __init__(self, first_name, last_name, age, gender, email):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.age = age
        self.gender = gender
        self.email = email

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")
        print(f"Age:{self.age}")
        print(f"Gender:{self.gender}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, this is your personalized greeting!")


user1 = User("mary", "berry", "86", "female", "mrsmaryberry@yahoo.com")
user2 = User("paul", "hollywood", "56", "male", "paul.hollywood@gmail.com")
user3 = User("noel", "fielding", "48", "male", "fieldingnoel@gmail.com")


user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()


# 9-4
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = f"{self.name} has {self.cuisine_type} on the menu tonight!"
        print(msg)

    def open_restaurant(self):
        msg2 = f"{self.name} is open!"
        print(msg2)

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, more_served):
        self.number_served += more_served


restaurant4 = Restaurant("Send Noodles", "noodles")
restaurant4.describe_restaurant()
print(f"Number served: {restaurant4.number_served}")

restaurant4.number_served = 145
print(f"Number served: {restaurant4.number_served}")

restaurant4.set_number_served(456)
print(f"Number served: {restaurant4.number_served}")

restaurant4.increment_number_served(987)
print(f"Number served: {restaurant4.number_served}")


# 9-5
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


user = User("mary", "berry", "86", "female", "mrsmaryberry@yahoo.com")
user.describe_user()
user.greet_user()

print("Logging in: 3 attempts")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")

print("Reset login attempts.")
user.reset_login_attempts()
print(f"Login attempts: {user.login_attempts}")
