
from package.Base.Pointed import Point
from package.Base.Line import Line
from package.Shape.Shape_e import Shape


class Rectangle(Shape):
    def __init__(self, is_regular: bool, point_bt_sid: "Point", point_up_sid: "Point"):
        super().__init__(is_regular)
        self.__ver1 = point_bt_sid
        self.__ver2 = Point(point_up_sid.x, point_bt_sid.y)
        self.__ver3 = point_up_sid
        self.__ver4 = Point(point_bt_sid.x, point_up_sid.y)

    def get_ver1(self):
        return self.__ver1
    
    def get_ver2(self):
        return self.__ver2
    
    def get_ver3(self):
        return self.__ver3
    
    def get_ver4(self):
        return self.__ver4
    
    def vertices(self):
        v = [self.get_ver1(), self.get_ver2(), self.get_ver3(), self.get_ver4()]
        return v
    
    def edges(self):
        line_1 = Line(self.get_ver1(), self.get_ver2())
        line_2 = Line(self.get_ver2(), self.get_ver3())
        line_3 = Line(self.get_ver3(), self.get_ver4())
        line_4 = Line(self.get_ver4(), self.get_ver1())
        d = [line_1, line_2, line_3, line_4]
        return d
    
    def compute_inner_angles(self):
        angle = [90, 90, 90, 90]
        return angle

    def inner_angles(self):
        d = self.vertices()
        angles = self.compute_inner_angles()
        for i in range(len(d)):
            print(f"{chr(97 + i)}: {d[i]} = {angles[i]}")  
        return ""
    
    def compute_perimeter(self):
        s = 0
        for i in self.edges():
            s += i.compute_length()
        return round(s, 3)
    
    def compute_area(self):
        base: float = abs(self.get_ver1().x - self.get_ver3().x)
        altura: float = abs(self.get_ver1().y - self.get_ver3().y)
        return base * altura
    


        