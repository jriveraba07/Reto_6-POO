from package.Base.Pointed import Point
from package.Base.Line import Line
from .Rectangle import Rectangle 



class Square(Rectangle):
    def __init__(self, point_bt_sid: "Point", point_up_sid: "Point"):
        super().__init__(True, point_bt_sid, point_up_sid)