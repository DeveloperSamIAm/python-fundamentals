# Question 1: Write a function called simple(). Assign a different
# message to 5 variables and print each message.

def simple():
    """Display a simple message."""
    print(f"{simple} are delicious!")


simple()

msg1 = "cupcakes"
print(msg1)
msg2 = "cookies"
print(msg2)
msg3 = "parfaits"
print(msg3)
msg4 = "eclairs"
print(msg4)
msg5 = "waffles"
print(msg5)


# Question 2: Write a function called simple2(). Assign a message
# to a variable, then print out that variable. Change the message
# and assign it to the variable again, but after the first print
# statement. Print the second message. Do these steps 2 more times.
# You should have 4 messages assigned to the same variable and 4
# print functions showing results.

def simple2():
    """Display a simple message."""
    print(f"{simple2} are super delicious!")
    msg = "cupcakes"
    print(msg)
    msg = "cookies"
    print(msg)
    msg = "parfaits"
    print(msg)
    msg = "eclairs"
    print(msg)


simple2()


# Question 3: Write a function called message that takes 1 argument. Inside
# that function, write a print function that takes the argument.

def message(arg1):
    """Display a message with argument."""
    print(arg1)


message('SamIAm')

