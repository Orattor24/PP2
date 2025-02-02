import math

n = int(input("Number of sides: "))
l = int(input("Length: "))

area = (n*l**2)/(4*math.tan(math.pi/n))

area = math.floor(area)
print(area)
