def histogram(lis):
    for i in range(len(lis)):
        print("*"*lis[i])

l = []
num = int(input("Введи количество слов в списке: "))
for i in range(num):
    n = int(input())
    l.append(n)

histogram(l)