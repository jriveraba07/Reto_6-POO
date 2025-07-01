from package.Base.Pointed import Point

class Line:
    def __init__(self, start: "Point", end: "Point"):
        self.start = start
        self.end = end
        self.length = self.compute_length()
        self.slope = self.compute_slope()
    
    def compute_length(self)-> float:
        return self.start.compute_distance(self.end)
