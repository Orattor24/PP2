num = []
unique = []
size = int(input())
for i in range(size):
    znachenie = int(input())
    num.append(znachenie)
num.sort()
for i in range(len(num)):
    if i == 0 or num[i] != num[i - 1]:
        unique.append(num[i])

print(unique)
