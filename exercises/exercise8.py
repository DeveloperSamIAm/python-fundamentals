# Lab Exercise 8 Collections

# 5-8
usernames = ["spongebob", "patrick", "squidward", "sandy", "admin"]


def username_login():
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again!")


username_login()


# 5-9
usernames2 = []


def username_login2():
    if usernames2:
        for username in usernames2:
            if username == "admin":
                print("Hello admin, would you like to see a status report?")
            else:
                print(f"Hello {username}, thank you for logging in again!")
    else:
        print("We need to find some users!")


username_login2()


# 5-10
current_users = ["spongebob", "patrick", "squidward", "sandy", "larry"]
new_users = ["SpongeBob", "PATRICK", "crabs", "pearl", "plankton"]

current_users_lower = [user.lower() for user in current_users]


def checking_usernames():
    for new_user in new_users:
        if new_user.lower() in current_users_lower:
            print(f"Sorry {new_user}, that name has already been used.")
        else:
            print(f"Awesome {new_user}, that name is available!")


checking_usernames()


# 5-11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def ordinal_numbers():
    for number in numbers:
        if number == 1:
            print("1st")
        elif number == 2:
            print("2nd")
        elif number == 3:
            print("3rd")
        else:
            print(f"{number}th")


ordinal_numbers()


# 6-1
person = {"first name": "spongebob", "last name": "squarepants", "age": "12", "city": "bikini bottom"}
print(person["first name"])
print(person["last name"])
print(person["age"])
print(person["city"])


# 6-7
person1 = {"first name": "spongebob", "last name": "squarepants", "age": "12", "city": "bikini bottom"}
person2 = {"first name": "patrick", "last name": "star", "age": "13", "city": "bikini bottom"}
person3 = {"first name": "squidward", "last name": "tentacles", "age": "30", "city": "bikini bottom"}

people = [person1, person2, person3]


def people_example():
    for persons in people:
        print(persons["first name"])
        print(persons["last name"])
        print(persons["age"])
        print(persons["city"])


people_example()
