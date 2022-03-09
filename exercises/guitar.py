class Guitar:
    def __init__(self, string_size, body_material, pickguard_color):
        self._string_size = string_size
        self._body_material = body_material
        self._pickguard_color = pickguard_color

    def play_note_a(self):
        print(f"The {self._body_material} guitar plays the A note")

    @property
    def string_size(self):
        return self._string_size

    @string_size.setter
    def string_size(self, size):
        self._string_size = size

    @property
    def body_material(self):
        return self._body_material

    @body_material.setter
    def body_material(self, material):
        self._body_material = material

    @property
    def pickguard_color(self):
        return self._pickguard_color

    @pickguard_color.setter
    def pickguard_color(self, value):
        self._pickguard_color = value


my_guitar = Guitar("heavy", "mahogany", "cream")
print(my_guitar.string_size)
print(my_guitar.body_material)
print(my_guitar.pickguard_color)
my_guitar.play_note_a()
