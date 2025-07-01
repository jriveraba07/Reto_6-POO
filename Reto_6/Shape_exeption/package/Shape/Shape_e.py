#* Base shape for others class

class Shape:
    def __init__(self, is_regular: bool):
        self.regular = is_regular
    
    def vertices(self):
        pass
    
    def edges(self):
        pass
    
    def inner_angles(self):
        pass
    
    def compute_area(self):
        pass
   
    def compute_perimeter(self):
        pass
    
    def compute_inner_angles(self):
        pass

