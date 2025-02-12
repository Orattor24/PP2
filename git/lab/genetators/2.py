n = int(input())
a = []
for i in range(0, n+1, 2):
    a.append(i)
s = ','.join([str(x) for x in a])
print(s)