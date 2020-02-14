# 80

class Potion:

    def __init__(self, color, volume):
        self.color = color
        self.volume = volume
    
    def mix(self, other):
        self.volume += other.volume
        return self