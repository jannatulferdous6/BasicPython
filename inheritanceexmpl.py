class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print("Areaa of a shape")

class triangle(Shape):
    def area(self):
        area = 0.5 * self.width *self.height
        print(area)

class recangle(Shape):
    def area(self):
        area = self.width *self.height
        print(area)

t = triangle(2, 3)
t.area()

r = recangle(5,2)
r.area()