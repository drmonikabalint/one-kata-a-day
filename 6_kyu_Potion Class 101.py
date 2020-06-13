import math
class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume
    
    def mix(self, other):
        self.other = other      
        self.totalvolume = self.other.volume + self.volume
        
        x = self.volume/self.totalvolume
        y = self.other.volume/self.totalvolume
        
        self.new_color1 =  math.ceil(x*self.color[0] + y*self.other.color[0])
        self.new_color2 =  math.ceil(x*self.color[1] + y*self.other.color[1])
        self.new_color3 =  math.ceil(x*self.color[2] + y*self.other.color[2])

        return Potion((self.new_color1, self.new_color2, self.new_color3), self.totalvolume)
