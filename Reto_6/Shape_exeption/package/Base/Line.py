from package.Base.Pointed import Point

class Line:
    def __init__(self, start: "Point", end: "Point"):
        self.start = start
        self.end = end
        self.length = self.compute_length()
        self.slope = self.compute_slope()
    
    def compute_length(self)-> float:
        return self.start.compute_distance(self.end)

    def compute_slope(self)-> float:
        if self.end.x != self.start.x:     
            delta_y = self.end.y - self.start.y
            delta_x = self.end.x - self.start.x
            return delta_y / delta_x
        else:
            return None
    
    def __str__(self):
        return f"star: {self.start} , end: {self.end}"
    
    def __repr__(self):
        return f"[{self.start} , {self.end}]"
