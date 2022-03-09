class Watch:
    def __init__(self, metal_type, strap_color, glass_type):
        self._metal_type = metal_type
        self._strap_color = strap_color
        self._glass_type = glass_type

    def alarm_on_off(self):
        print(f"The {self._metal_type} watch\'s alarm is on")

    @property
    def metal_type(self):
        return self._metal_type

    @metal_type.setter
    def metal_type(self, metal):
        self._metal_type = metal

    @property
    def strap_color(self):
        return self._strap_color

    @strap_color.setter
    def strap_color(self, value):
        self._strap_color = value

    @property
    def glass_type(self):
        return self._glass_type

    @glass_type.setter
    def glass_type(self, type):
        self._glass_type = type


my_watch = Watch("silver", "black", "sapphire crystal")
print(my_watch.metal_type)
print(my_watch.strap_color)
print(my_watch.glass_type)
my_watch.alarm_on_off()
