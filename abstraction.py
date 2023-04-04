from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2
        
    @abstractmethod
    def area(self):
        pass
class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 *self.dim2
        print(area)

class recangle(Shape):
    def area(self):
        area = self.dim1 *self.dim2
        print(area)

t = Triangle(2, 3)
t.area()

r = recangle(5,2)
r.area()