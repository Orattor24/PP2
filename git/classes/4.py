import math



class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Координаты точки в :  ({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, dist):
        return  math.sqrt((self.x - dist.x)**2 + (self.y - dist.y)**2)

a = int(input())
b = int(input())
p = Point(a, b)

a1 = int(input())
b1 = int(input())
p1 = Point(a1, b1)

p.show()
p1.show()
print(p.dist(p1))