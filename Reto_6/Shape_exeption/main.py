from package.Base.Pointed import Point
from package.Figures.Rectangle import Rectangle 
from package.Figures.Square import Square
from package.Figures.Triangles import (Equilateral, Scalene, Isosceles)

#! cabe aclarrar que las pocas exepciones que hay estan en los modulos.
#! Lo anterior es por el hecho de que en las mismas funciones tienen condiciones
if __name__ == '__main__':
    # Triángulo escaleno (todos los lados diferentes)
    ver = Point(0, 1)
    ver2= Point(2, 2)
    ver3 = Point(2, 4)

    rectangulo = Rectangle(False, ver, ver2)
    cuadrado = Square(ver3, Point(4 , 6))

    print("                           |rectangulo|")
    print("")
    print("estos son los vertices del rectangulo:")
    print(rectangulo.vertices()) 
    print("estos son los lados del rectangulo:" ,rectangulo.edges()) 
    print("estos son los angulos del rectangulo:")
    print(rectangulo.inner_angles())

    print("este es el perimetro del rectangulo:" ,rectangulo.compute_perimeter())
    print("este es el area del rectangulo:" ,rectangulo.compute_area())   

    print("")

    print("                           |cuadrado|")
    print("")
    print("estos son los vertices del cuadrado:")
    print(cuadrado.vertices()) 
    print("estos son los lados del cuadrado:" ,cuadrado.edges()) 
    print("estos son los angulos del cuadrado:")
    print(cuadrado.inner_angles())

    print("este es el perimetro del cuadrado:" ,cuadrado.compute_perimeter())
    print("este es el area del cuadrado:" ,cuadrado.compute_area())   

    print("")



    print(                              "|Triangulos - prueba|")

    # Triángulo equilátero 
    A = Point(0, 0)
    B = Point(1, 0)
    C = Point(0.5, 0.866)  

    triangulo_equilatero = Equilateral(point_1=A, point_2=B, point_3=C)

    # Triángulo isósceles (dos lados iguales)
    D = Point(0, 0)
    E = Point(2, 0)
    F = Point(1, 2)

    triangulo_isosceles = Isosceles(point_1=D, point_2=E, point_3=F)

    # Triángulo escaleno (todos los lados diferentes)
    G = Point(0, 1)
    H = Point(2, 1)
    I = Point(2, 4)

    triangulo_escaleno = Scalene(point_1=G, point_2=H, point_3=I)

    print("                           |triángulo escaleno|")
    print("")
    print("estos son los vertices del triángulo:")
    print(triangulo_escaleno.vertices()) 
    print("estos son los lados del triángulo:" ,triangulo_escaleno.edges()) 
    print("estos son los angulos del triángulo:")
    print(triangulo_escaleno.inner_angles())

    print("este es el perimetro del triángulo:" ,triangulo_escaleno.compute_perimeter())
    print("este es el area del triángulo:" ,triangulo_escaleno.compute_area())   

    print("")

    print("                           |triángulo isoceles|")

    print("")
    print("estos son los vertices del triángulo:")
    print(triangulo_isosceles.vertices()) 
    print("estos son los lados del triángulo:" ,triangulo_isosceles.edges()) 
    print("estos son los angulos del triángulo:")
    print(triangulo_isosceles.inner_angles())
    print("este es el perimetro del triángulo:" ,triangulo_isosceles.compute_perimeter())
    print("este es el area del triángulo:", triangulo_isosceles.compute_area())
      
    print("")

    print("                           |triángulo equilatero|")

    print("")
    
    print("estos son los vertices del triángulo:")
    print(triangulo_equilatero.vertices()) 
    print("estos son los lados del triángulo:" ,triangulo_equilatero.edges()) 
    print("estos son los angulos del triángulo:")
    print(triangulo_equilatero.inner_angles())
    print("este es el perimetro del triángulo:" ,triangulo_equilatero.compute_perimeter())
    print("este es el area del triángulo:", triangulo_equilatero.compute_area() )

