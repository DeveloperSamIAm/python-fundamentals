class Horse:
    def __init__(self, coat_color, shoe_size, saddle_material):
        self._coat_color = coat_color
        self._shoe_size = shoe_size
        self._saddle_material = saddle_material

    def neigh(self):
        print(f"The {self._coat_color} horse neighs")

    @property
    def coat_color(self):
        return self._coat_color

    @coat_color.setter
    def coat_color(self, value):
        self._coat_color = value

    @property
    def shoe_size(self):
        return self._shoe_size

    @shoe_size.setter
    def shoe_size(self, num):
        self._shoe_size = num

    @property
    def saddle_material(self):
        return self._saddle_material

    @saddle_material.setter
    def saddle_material(self, material):
        self._saddle_material = material


my_horse = Horse("white", "large", "leather")
print(my_horse.coat_color)
print(my_horse.shoe_size)
print(my_horse.saddle_material)
my_horse.neigh()
