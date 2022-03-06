# Lab Exercise - Control Flow

# 5-3
alien_color = "green"


def alien_shot():
    if alien_color == "green":
        print("Player earned 5 points!")
    if alien_color == "red":
        print("Player missed!")
    if alien_color == "yellow":
        print("Player missed!")


def alien_shot2():
    if alien_color == "red":
        print("Player earned 5 points!")


alien_shot()
alien_shot2()

# 5-4


def alien_if_else():
    if alien_color == "green":
        print("Player earned 5 points!")
    else:
        print("Player earned 10 points!")


def alien_if_else2():
    alien_color = "yellow"
    if alien_color == "green":
        print("Player earned 5 points!")
    else:
        print("Player earned 10 points!")


alien_if_else()
alien_if_else2()

# 5-5


def alien_if_elif_else1():
    alien_color = "green"
    if alien_color == "green":
        print("Player earned 5 points!")
    elif alien_color == "yellow":
        print("Player earned 10 points!")
    else:
        print("Player earned 15 points!")


def alien_if_elif_else2():
    alien_color = "yellow"
    if alien_color == "green":
        print("Player earned 5 points!")
    elif alien_color == "yellow":
        print("Player earned 10 points!")
    else:
        print("Player earned 15 points!")


def alien_if_elif_else3():
    alien_color = "red"
    if alien_color == "green":
        print("Player earned 5 points!")
    elif alien_color == "yellow":
        print("Player earned 10 points!")
    else:
        print("Player earned 15 points!")


alien_if_elif_else1()
alien_if_elif_else2()
alien_if_elif_else3()


# 5-6
age = 3


def life_stage():
    if age < 2:
        print("You're a baby!")
    elif age < 4:
        print("You're a toddler!")
    elif age < 13:
        print("You're a kid!")
    elif age < 20:
        print("You're a teenager!")
    elif age < 65:
        print("You're an adult!")
    else:
        print("You're an elder!")


life_stage()


# Question 5: Write a function that takes and argument. Check this
# argument to see if it is a Boolean using  the bool method. Call the
# method and use the below values as your argument. Using comments,
# provide the name of the argument and if it was true or false from
# running the code.
def boolean_sample(arg):
    print(bool(arg))


boolean_sample(0.0)

# When the argument's value was 12 the result was true
# When the argument's value was 1.2 the result was true
# When the argument's value was 0 the result was false
# When the argument's value was 0.4 the result was true
# When the argument's value was 0.0 the result was false
