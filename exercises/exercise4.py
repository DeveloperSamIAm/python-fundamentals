# Question 1
# On page 29 of your book, in the Try it Yourself section do the
# following tasks. Put all your code in your exercise4.py file.

# 2-8 Number Eight
# Write addition, subtraction, multiplication, and division operations
# that each result in the number 8. Be sure to enclose your operations
# in print() calls to see the results. You should create four lines that
# look like this: print(5+3). Your output should simply be four lines
# with the number 8 appearing once on each line.

print(2 + 6)
print(10 - 2)
print(2 * 4)
print(16 / 2)

# 2-9 Favorite Number
# Use a variable to represent your favorite number. Then, using that
# variable, create a message that reveals your favorite number. Print
# that message.

favorite_number = "3"
message = f"My favorite number is {favorite_number}!"
print(message)

# Question 2
# Assign variables to the following sets of numbers. Use underscores
# to make them more readable. Write a function called number_sets
# and print each variable inside the function. Call all the function
# to verify your results.

var1 = 456_234
var2 = 68_423_791
var3 = 13_794_628
var4 = 96_374


def number_sets():
    """Print a set of numbers as variables."""
    print(f"{var1}, {var2}, {var3}, {var4}")


number_sets()


# Question 3
# Write a function that will take 2 arguments. Using Type conversion,
# convert the first argument from int to float. Convert the second
# argument from float to int. Call the function and provide the correct
# values for each argument to verify your results. One argument should
# be a float and the other an int.

def conversion(value1, value2):
    print(float(value1))
    print(int(value2))


conversion(8, 26.5)

# Question 4
# Write a function that will have two inputs. The first input method should
# ask "what is your favorite movie" the second input method should ask
# "How many times have you seen it?" The second input should be inside an
# int function. Each input method should be assigned to a variable. In a
# print statement using placeholders, the output should be "I have seen
# {favorite movie}{number of times} times."

movie = input("What is your favorite movie? ")
times = int(input("How many times have you seen it? "))

message = "I have seen {0} {1} times."
print(message.format(movie, times))
