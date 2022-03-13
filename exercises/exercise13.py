# Lab Exercise 13
# 8-15
import printing_functions as pf

unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)

# 8-16
# import module_name
import separatefile
separatefile.favorite_book("The Count of Monte Cristo")

# from module_name import function_name
from separatefile import favorite_book
favorite_book("Crime and Punishment")

# from module_name import function_name as fn
from separatefile import favorite_book as fb
fb("Pride and Prejudice")

# import module_name as mn
import separatefile as sepfile
sepfile.favorite_book("The Science of Interstellar")

# from module_name import *
from separatefile import *
favorite_book("The Hobbit")

# 8-17
# Choose any 3 programs you wrote for this chapter, and make sure they follow the styling
# guidelines described in this section.


# 1
def make_shirt(size, text):
    """Prints a statement with the size and text on a shirt."""
    print(f"{size} shirt")
    print(f"The shirt will say {text}")


make_shirt("medium", "Coding is awesome!")
make_shirt(size="large", text="Coding is cool when you are part of a team")


# 2
def describe_city(city_name, city_country="united states"):
    """Prints a statement with the name of a city and which country it is located in."""
    print(f"{city_name.title()} is in {city_country.title()}")


describe_city("Wichita")
describe_city("Denver")
describe_city("Berlin", "Germany")


# 3
messages = ["hey how are you today?", "want to play video games?", "pizza for dinner tonight", "omw home"]


def show_messages():
    """Prints a list of text messages."""
    for message in messages:
        print(message)


show_messages()

# 9-10
from separatefile import Restaurant

restaurant1 = Restaurant("Sushi Time", "sushi")
restaurant1.describe_restaurant()


# 9-11
from separatefile import Admin

samiam = Admin("sami", "king", "30", "female", "sking10@wsutech.edu",
               ["can add post", "can delete post", "can ban user",
                "can host server", "can use command prompt"])
samiam.describe_user()
samiam.privileges.show_privileges()

# 9-12
from adminprivilegeclass import Admin2


bob = Admin2("Bob", "Barker", "98", "male", "bob.barker@thepriceisright.com",
            ["can add post", "can delete post", "can ban user",
             "can host server", "can use command prompt"])

bob.describe_user()
bob.privileges.show_privileges()

# 9-16
from random import randint
print(randint(2, 9))

import datetime
t = datetime.time(1, 2, 3)
print(t)
print("hour       :", t.hour)
print("minute     :", t.minute)
print("second     :", t.second)
print("microsecond:", t.microsecond)
print("tzinfo     :", t.tzinfo)

# From the Python standard library I chose to explore the random integer
# and date and time value manipulation modules. For the random module
# I specifically imported the randint function to show that it will print
# a random integer, and I set the range to be between 2 and 9. For the
# datetime module I used a series of print statements to show the hour,
# minute, second, microsecond, and tzinfo. 
