# 80

class Potion:

    def __init__(self, color, volume):
        self.color = color
        self.volume = volume
    
    def mix(self, other):
        print(f"Volume: {self.volume} - other.volume: {other.volume}")
        a = (other.color[0] + self.color[0]) / 2
        b = (other.color[1] + self.color[1]) / 2
        c = (other.color[2] + self.color[2]) / 2
        return Potion([a, b, c], self.volume + other.volume)