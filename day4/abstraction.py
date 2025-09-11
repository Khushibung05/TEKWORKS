from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r**2
RectangleArea=Rectangle(10,20)
CircleArea=Circle(7)
print("Area of Rectangle:",RectangleArea.area())
print("Area of Circle:",CircleArea.area())