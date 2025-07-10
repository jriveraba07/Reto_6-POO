
class Point:
    definition: str = "Entidad geometrica abstracta que representa un punto en el espacio"
    #* atributos que tiene la clase ^
    #* la funcion inicializadora
    def __init__(self, x : float = 0, y : float = 0):
        self.x = x 
        self.y = y
    
    # metodos
    def move(self, new_x : float, new_y : float):
        self.x = new_x
        self.y = new_y
        
    def reset(self):
        self.x = 0 
        self.y = 0   

    def prod_punto(self, point: "Point"):
        return self.x * point.x + self.y * point.y
    
    def compute_distance(self, point: "Point")-> float:
        distance = ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5 
        return distance
    
    def __sub__(self, point2: "Point")-> "Point":
        vec_x = self.x - point2.x
        vec_y = self.y - point2.y
        return Point(vec_x, vec_y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"({self.x}, {self.y})"