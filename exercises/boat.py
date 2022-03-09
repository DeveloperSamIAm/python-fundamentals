class Boat:
    def __init__(self, hull_color, helm_size, sail_mat_type):
        self._hull_color = hull_color
        self._helm_size = helm_size
        self._sail_mat_type = sail_mat_type

    def propeller_for_back(self):
        print(f"The propeller on the {self._hull_color} boat goes forward")

    @property
    def hull_color(self):
        return self._hull_color

    @hull_color.setter
    def hull_color(self, value):
        self._hull_color = value

    @property
    def helm_size(self):
        return self._helm_size

    @helm_size.setter
    def helm_size(self, num):
        self._helm_size = num

    @property
    def sail_mat_type(self):
        return self._sail_mat_type

    @sail_mat_type.setter
    def sail_mat_type(self, material):
        self._sail_mat_type = material


my_boat = Boat("blue", 13, "polyester")
print(my_boat.hull_color)
print(my_boat.helm_size)
print(my_boat.sail_mat_type)
my_boat.propeller_for_back()
