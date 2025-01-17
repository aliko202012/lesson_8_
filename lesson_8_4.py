class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


circle = Circle(5)
print("Площадь круга:", circle.area())
print("Периметр круга:", circle.perimeter())

rectangle = Rectangle(4, 7)
print("Площадь прямоугольника:", rectangle.area())
print("Периметр прямоугольника:", rectangle.perimeter())