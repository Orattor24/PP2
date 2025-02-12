def deg(n):
    for i in range(n, -1 , -1):
        yield i

n = int(input())

for i in deg(n):
    print(i, end=' ')