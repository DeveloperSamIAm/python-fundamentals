print("Hello World")

# Make a typo somewhere in the line and run the program and run
# the program again.
# Can you make a typo that generates an error?
# Yes, by leaving off the second quotation mark (") at the end of
# Hello World, I was able to get the error "SyntaxError: unterminated
# during string literal (detected at line 1)"

# Can you make sense of the error message?
# Yes, the syntax error message is notifying me that on line 1 there
# is a problem where the string is missing the second (or terminal)
# quotation mark.

# Can you make a typo that doesn't generate an error?
# Misspelling the phrase "Hello World" as "Hello Word" does not create
# an error.

# Why do you think it didn't make an error?
# I think it doesn't create an error because the characters within
# the quotes could say anything and do not have an impact on what
# the function is trying to perform, only what it ends up saying.

# Exercise 2-11
# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

message = "Pi is good!"
print(message)

# In this exercise (2-1) I am introducing a variable named message
# and I am telling it that the value connected to it is the
# "Pi is good!" text. So when the code is run using the terminal
# pycharm will look at the second line that says print(message)
# and then see that the associated message equals what I have
# in quotation marks.

message = "Pi is good!"
print(message)

message = "What is the animal of the day in programming? A Pi-thon"
print(message)


# In this exercise (2-2) I am assigning a message to a variable and
# on the second print function I have changed the value of the
# message to say something else. So when the code is run the
# first message will print and then the second message will print
# based on the new information the print function was given.

def display_message():
    """Display a message about what I am learning."""
    message = "I am learning how to insert values for code functions."
    print(message)

display_message()

# For exercise 8-1 I am defining a function named display_message
# and then using a function call to tell python to execute the
# code in the function. The triple quotes indicate a docstring
# that tells what the function does. So on the last line when
# I call for display_message() it is calling the function to
# print the message that I have defined above.

def favorite_book(title):
    """Display the users favorite book."""
    print(f"{title} is one of my favorite books.")

favorite_book("The Great Gatsby")

# For exercise 8-2 I am defining a favorite_book function and
# by adding title I can then define any book title name for
# the function to reference. When the function print is used
# I can use that title reference to insert any book title,
# but in this case I have defined favorite_book as The
# Great Gatsby because it is an American classic and one
# of my favorite books. This is similar to the exercise for
# 8-1 but the difference being that I can pass information
# into a function by using the title.
