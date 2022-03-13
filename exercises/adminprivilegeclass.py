from userclass import User


class Admin2(User):
    def __init__(self, first_name, last_name, age, gender, email, privileges):
        super().__init__(first_name, last_name, age, gender, email)
        self.privileges = Privileges(privileges)


class Privileges:
    def __init__(self, privileges):
        self.privileges = ["can add post", "can delete post", "can ban user",
                           "can host server", "can use command prompt"]

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"{privilege}")

