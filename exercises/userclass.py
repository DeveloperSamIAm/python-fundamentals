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

