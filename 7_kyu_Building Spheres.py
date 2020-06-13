import math
class Sphere(object):
    def __init__(self, r, m): 
        self.r = r
        self.m = m
    def get_radius(self): return self.r
    def get_mass(self): return self.m
    def get_volume(self): 
        # 4/3 * pi *r^3         
        return float('{:.5f}'.format(4/3 *math.pi*self.get_radius()**3))
    def get_surface_area(self):
        #4 pi r^2
        return float('{:.5f}'.format(4 * math.pi * self.get_radius()**2))    
    def get_density(self): 
        #3m/4πr³)
        return float('{:.5f}'.format(3*self.get_mass()/(4*math.pi * self.get_radius()**3)))
