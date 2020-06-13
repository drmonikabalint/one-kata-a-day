class Block:
    def __init__(self, b):
        self.b = b
    def get_width(self): 
        return (self.b[0])
    def get_length(self): 
        return self.b[1]
    def get_height(self): 
        return self.b[2]
    def get_volume(self):
        return self.b[0]*self.b[1]*self.b[2]
    def get_surface_area(self):
        #Surface area of a prism: 2ab + 2bc + 2ac
        return 2*(self.b[0]*self.b[1] + self.b[0]* self.b[2] + self.b[1]*self.b[2])
