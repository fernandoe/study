import math

class Potion:

    def __init__(self, color, volume):
        self.color = color
        self.volume = volume
    
    def mix(self, other):
        vol = self.volume + other.volume
        color_1 = self._color_resultant_calculation(other.color[0], other.volume, self.color[0], self.volume)
        color_2 = self._color_resultant_calculation(other.color[1], other.volume, self.color[1], self.volume)
        color_3 = self._color_resultant_calculation(other.color[2], other.volume, self.color[2], self.volume)
        return Potion((color_1, color_2, color_3), vol)

    def _color_resultant_calculation(self, color1, vol1, color2, vol2):
        return math.ceil(((color1 * vol1) + (color2 * vol2)) / (vol1 + vol2))
