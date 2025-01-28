a = 33
b = 200
if b > a:
  print("b is greater than a")

#elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  #short hand if
if a > b: print("a is greater than b")
#short if_else
a = 2
b = 330
print("A") if a > b else print("B")
#and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
#not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")