print(10 > 9)
print(10 ==9)
print(10 < 9)

#Second example.txt
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#Bool
print(bool("Hello"))
print(bool(15))
#Bool exp. 2
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#Most Values are True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#Some Values are False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})