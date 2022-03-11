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


class Donkey(Horse):
    def __init__(self, coat_color, shoe_size, saddle_material, teeth_number):
        super().__init__(coat_color, shoe_size, saddle_material)
        self._teeth_number = teeth_number

    @property
    def teeth_number(self):
        return self._teeth_number

    @teeth_number.setter
    def teeth_number(self, teeth_number):
        self._teeth_number = teeth_number

    def carry_basket(self):
        print(f"The donkey with {self.teeth_number} teeth needs to carry the basket")


my_donkey = Donkey("brown", "small", "polyester", "30")
print(my_donkey.teeth_number)
my_donkey.carry_basket()


class Zebra(Horse):
    def __init__(self, coat_color, shoe_size, saddle_material, stripe_number):
        super().__init__(coat_color, shoe_size, saddle_material)
        self._stripe_number = stripe_number

    @property
    def stripe_number(self):
        return self._stripe_number

    @stripe_number.setter
    def stripe_number(self, stripe_number):
        self._stripe_number = stripe_number

    def bray(self):
        print(f"Zebra with {self.stripe_number} stripes does a bray")


my_zebra = Zebra("black and white", "medium", "none", "26")
print(my_zebra.stripe_number)
my_zebra.bray()
