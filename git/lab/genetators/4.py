def squares_range(a, b):
    for i in range(a, b + 1):
        yield i * i


a = int(input())
b = int(input())

for num in squares_range(a, b):
    print(num, end=" ")
print()
