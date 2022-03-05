# Lab Exercise - Operators

# Question 1: On page 78 of your book, do 5-1 of the Try it Yourself.
# Put all your code in exercise5.py file.

# 5-1
# Create at least ten tests. Have at least 5 tests evaluate to true
# and another 5 tests evaluate to false.
# 1
dessert = 'cake'
print("Is dessert == 'cake'? I predict True.")
print(dessert == 'cake')

print("\nIs dessert == 'eclair'? I predict False.")
print(dessert == 'eclair')

# 2
phone = 'oneplus'
print("Is phone == 'oneplus'? I predict True.")
print(phone == 'oneplus')

print("\nIs phone == 'iphone'? I predict False.")
print(phone == 'iphone')

# 3
laptop = 'asus'
print("Is laptop == 'asus'? I predict True.")
print(laptop == 'asus')

print("\nIs laptop == 'mac'? I predict False.")
print(laptop == 'mac')

# 4
coffee = 'starbucks'
print("Is coffee == 'starbucks'? I predict True.")
print(coffee == 'starbucks')

print("\nIs coffee == 'dunkin'? I predict False.")
print(coffee == 'dunkin')

# 5
pillow = 'fluffy'
print("Is pillow == 'fluffy'? I predict True.")
print(pillow == 'fluffy')

print("\nIs pillow == 'hard'? I predict False.")
print(pillow == 'hard')

# Question 2: On page 78 of your book, create new examples that meet
# the bullet points of 5-2. Put your code for this in your exercise5.py
# file.

# 5-2
# Test for equality and inequality with strings


def compare_strings(val1, val2):
    result_equal = val1 == val2
    result_not = val1 != val2
    print(result_equal)
    print(result_not)


compare_strings("monster energy", "caramel macchiato")


# Tests using the lower(method)
name1 = 'SamIAm'
name2 = 'samiam'
print(name1.lower() == name2.lower())
print(name1.lower() != name2.lower())

# Numerical tests involving equality and inequality, greater than and
# less than, greater  than or equal to, and less than or equal to.

num1 = 10
num2 = 20
num3 = 30


def equality():
    result_true = num1 * 2 == num2
    result_false = num1 == num2
    print(result_true)
    print(result_false)


equality()


def inequality():
    result_true = num1 != num2
    result_false = num1 + num2 != num3
    print(result_true)
    print(result_false)


inequality()

def greater():
    result_true = num2 > num1
    result_false = num1 > num2
    print(result_true)
    print(result_false)


greater()

def less():
    result_true = num1 < num2
    result_false = num2 < num1
    print(result_true)
    print(result_false)


less()


def great_equal():
    result_true = num1 + num2 >= num3
    result_false = num1 >= num2 + num3
    print(result_true)
    print(result_false)


great_equal()

def less_equal():
    result_true = num1 <= num2
    result_false = num2 <= num1
    print(result_true)
    print(result_false)


less_equal()


# using the and keyword and the or keyword
def logical_and():
    result_true = num1 > 5 and num1 < 20
    result_false = num1 > 5 and num1 < 7
    print(result_true)
    print(result_false)


logical_and()


def logical_or():
    result_true = num3 == 30 or num1 < num3
    result_false = num2 > num3 or num2 < num1
    print(result_true)
    print(result_false)


logical_or()


# test whether an item is in a list
# test whether an item is not in a list
def icecream():
    toppings = ['sprinkles', 'whipped cream', 'fudge', 'cherry']
    order1 = 'sprinkles' in toppings
    order2 = 'anchovies' in toppings
    order3 = 'soy sauce' not in toppings
    order4 = 'cherry' not in toppings
    print(order1)
    print(order2)
    print(order3)
    print(order4)


icecream()


# Question 3: Write a function that will take 2 arguments. Inside
# the function provide examples of all the arithmetic operators.
# Provide a variable for each solution and print the results of each.


def arithmetic_example(arg1, arg2):
    addition = arg1 + arg2
    print(addition)
    subtraction = arg2 - arg1
    print(subtraction)
    multiplication = arg2 * arg1
    print(multiplication)
    division = 12 / arg2
    print(division)
    modulus = 12 % arg1
    print(modulus)
    exponent = arg2 ** arg1
    print(exponent)
    floor_division = 64 // arg1
    print(floor_division)


arithmetic_example(3, 4)

# Question 4: Write a function that takes only 1 argument. Inside
# the function provide examples of Assignment operators:
# modulus equals, minus equals, exponent equals & plus equals
# Provide a variable for each solution and print the results of each

def assignment(value):
    value += 4
    print(value)
    value -= 4
    print(value)
    value *= 100
    print(value)
    value /= 20
    print(value)
    value %= 15
    print(value)
    value **= 2
    print(value)
    value //= 10
    print(value)


assignment(100)
