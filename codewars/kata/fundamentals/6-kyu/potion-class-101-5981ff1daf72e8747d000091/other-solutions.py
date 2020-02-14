# -------------------------------------------------------------------------------------------------

from math import ceil

class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume
    
    def mix(self, other):
        full_volume = self.volume + other.volume
        x, y = self.volume / full_volume, other.volume / full_volume
        red, green, blue = [ceil(a * x + b * y) for a, b in zip(self.color, other.color)]
        return Potion((red, green, blue), full_volume)

# -------------------------------------------------------------------------------------------------

from math import ceil
class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume
    
    def mix(self, other):
    
        ratio1 = self.volume / (self.volume + other.volume) 
        ratio2 = other.volume / (self.volume + other.volume) 

        r = ceil(self.color[0] * ratio1 + other.color[0] * ratio2)
        g = ceil(self.color[1] * ratio1 + other.color[1] * ratio2)
        b = ceil(self.color[2] * ratio1 + other.color[2] * ratio2)
        
        volume = self.volume + other.volume
        
        return Potion((r, g, b), volume)

# -------------------------------------------------------------------------------------------------

from operator import attrgetter
from numpy import average
from math import ceil

class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume
    
    # Works for more than 2 potions
    def mix(*potions):
        colors = list(map(attrgetter("color"), potions))
        volumes = list(map(attrgetter("volume"), potions))
        return Potion(tuple(map(ceil, average(colors, 0, volumes))), sum(volumes))

# -------------------------------------------------------------------------------------------------

import math

class Potion:
    def __init__(self, color, vol):
        self.color, self.volume = color, vol

    def mix(self, other):
        v1, v2 = self.volume, other.volume
        return  Potion(tuple([math.ceil((n*v1 + m*v2)/(v1 + v2)) for n, m in zip(self.color, other.color)]), 
            self.volume + other.volume)

# -------------------------------------------------------------------------------------------------

import math

class Potion:
  def __init__(self, color, volume):
    self.color = color
    self.volume = volume

  def mix(self, other):
    resVol = self.volume + other.volume
    resCol = tuple([math.ceil((self.color[i] * self.volume + other.color[i] * other.volume) / resVol) for i in [0, 1, 2]])
    return Potion(resCol, resVol)

# -------------------------------------------------------------------------------------------------
