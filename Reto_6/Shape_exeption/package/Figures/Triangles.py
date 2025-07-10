
from math import (degrees, acos)
from package.Base.Pointed import Point
from package.Base.Line import Line
from package.Shape.Shape_e import Shape


class Triangle(Shape):
    def __init__(self, is_regular: bool, point_1: "Point" , point_2: "Point" , point_3: "Point"):
        super().__init__(is_regular)
        self.__Point_1 = point_1
        self.__Point_2 = point_2
        self.__Point_3 = point_3
    
    def get_Point_1(self):
        return self.__Point_1
    
    def get_Point_2(self):
        return self.__Point_2
    
    def get_Point_3(self):
        return self.__Point_3
    
    def vertices(self):
        v = [self.get_Point_1(), self.get_Point_2(), self.get_Point_3()]
        for i in range(len(v)):
            print(f"vertice {chr(97 + i)} =  {v[i]}")
        return ""

    def edges(self):
        line_1 = Line(self.get_Point_1(), self.get_Point_2())
        line_2 = Line(self.get_Point_2(), self.get_Point_3())
        line_3 = Line(self.get_Point_3(), self.get_Point_1())
        d = [line_1, line_2, line_3]
        return d
    
    def compute_inner_angles(self):
        d = [self.get_Point_1(), self.get_Point_2(), self.get_Point_3()]
        angle = []
        for i in range(3):
            try:    
                vec1 = d[i] - d[(i + 1) % 3]
                vec2 = d[i] - d[(i + 2) % 3]
                a = vec1.prod_punto(vec2)
                b = vec1.compute_distance(Point(0, 0)) * vec2.compute_distance(Point(0, 0))
                angle.append(round(degrees(acos(a / b)), 2))
            
            #! Aqui puede se error del usuario al poner una linea mal haciendo que se defina sobre un mismo punto
            except Exception as e:
                return f"error tipo {e}, un lado tiene el final igual que el inicio, porfavor corregir eso"
        return angle

    def inner_angles(self):
        vertices = [self.get_Point_1(), self.get_Point_2(), self.get_Point_3()]
        angles = self.compute_inner_angles()
        for i in range(len(vertices)):
            print(f"{chr(97 + i)}: {vertices[i]} = {angles[i]}")  
        return ""
    
    def compute_perimeter(self):
        s = 0
        for i in self.edges():
            s += i.compute_length()
        return round(s, 3)
    
    def compute_area(self):
        # lo que voy a poner es una formula general de cualquier triangulo
        edges = self.edges()
        a: float = edges[0].compute_length()
        b: float = edges[1].compute_length()
        c: float = edges[2].compute_length()
        #* s es el semiperimetro, osea que es la mitad del perimetro
        s: float = self.compute_perimeter() / 2
        return round((s * (s - a) * (s- b) * (s - c)) ** 0.5, 2)

class Equilateral(Triangle):
    def __init__(self, point_1: "Point" , point_2: "Point" , point_3: "Point"):
        super().__init__(True, point_1, point_2, point_3 )
    

class Scalene(Triangle):
    def __init__(self, point_1: "Point" , point_2: "Point" , point_3: "Point"):
        super().__init__(False, point_1, point_2, point_3 )


class Isosceles(Triangle):
    def __init__(self, point_1: "Point" , point_2: "Point" , point_3: "Point"):
        super().__init__(True, point_1, point_2, point_3 )