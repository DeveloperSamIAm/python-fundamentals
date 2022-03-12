# Lab Exercise 12 Exception Handling

# 10-6
def sample_addition():
    print("Let\'s add two numbers")
    try:
        first = input("The first number is...")
        second = input("The second number is...")
        answer = int(first) + int(second)
        print(answer)
    except ValueError:
        print("Please use an integer instead of text")


sample_addition()


# 10-7
def sample_addition2():
    print("Let\'s add two numbers")
    while True:
        try:
            first = input("The first number is...")
            second = input("The second number is...")
            answer = int(first) + int(second)
            print(answer)
        except ValueError:
            print("Please use an integer instead of text")


sample_addition2()

# 10-8
filenames = ["cats.txt", "dogs.txt"]


def find_file():
    for filename in filenames:
        print(f"Reading {filename}...")
        try:
            with open(filename) as f:
                contents = f.read()
                print(contents)
        except FileNotFoundError:
            print(f"Sorry the {filename} could not be found.")


find_file()

# 10-9
filenames2 = ["cats.txt", "dogs.txt"]


def find_file2():
    for filename2 in filenames2:
        try:
            with open(filename2) as f:
                contents = f.read()
        except FileNotFoundError:
            pass
        else:
            print(f"Reading {filename2}...")
            print(contents)


find_file2()
