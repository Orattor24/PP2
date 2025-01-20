class Shape:
    def area(self):
        return 0
class Square(Shape):

    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length**2
a = int(input())
area = Shape()
square = Square(a)
print(area.area())
print((square.area()))