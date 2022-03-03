# Lab Exercise- Strings

# On page 25 of your book, In the Try it Yourself section do the
# following tasks. Put all your code in your exercise3.py file.

# 2-3 Personal Message
# Use a variable to represent a person's name, and print a message
# to that person. Your message should be simple, such as, "Hello
# Eric, would you like to learn some Python today?"

full_name = "betty white"
message = f"Goodbye, {full_name.title()} you were an amazing woman."
print(message)


# 2-4 Name Cases
# Use a variable to represent a person's name, and then print that person's name
# in lowercase, uppercase, and title case.

name = "betty white"
print(name.lower())
print(name.upper())
print(name.title())

# 2-5 Famous Quotes
# Find a quote from a famous person you admire. Print the quote and the name of its
# author. Your output should look something like the following, including the
# quotation marks.

print("Betty White once said,\"Everybody needs a passion. That\'s what keeps life interesting."
      "If you live without passion, you can go through life without leaving any footprints.\"")

# 2-6 Famous Quotes 2
# Repeat exercise 2-5, but this time, represent the famous person's name using a variable called
# famous_person. Then compose your message and represent it with a new variable called message.
# Print your message.

famous_person = "betty white"
quote = "Everybody needs a passion. That\'s what keeps life interesting. " \
        "If you live without passion, you can go through life without leaving any footprints."
message = f"{famous_person.title()} once said, \"{quote}\""
print(message)

# 2-7 String Names
# Use a variable to represent a person's name, and include some whitespace characters at the
# beginning and end of the name. Make sure you use each character combination, "\t" and
# "\n" at least once. Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions lstrip(), rstrip(), and
# strip().

name = "\tbetty white\n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
