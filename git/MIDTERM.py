import math
def find_ceil_floor(help):
    a= []
    x = math.ceil(help)
    y = math.floor(help)



    a.append(x)
    a.append(y)
    return a
a = float(input())
print(find_ceil_floor(a))