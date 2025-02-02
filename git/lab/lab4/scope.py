#local scope
def myfunc():
    x= 300
    print(x)

myfunc()

#function inside function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#global scope
x = 290

def myfunc():
  print(x)

myfunc()

print(x)

#naming variables
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

#global keyword
def myfunc():
  global x
  x = 300

myfunc()

print(x)
#nonlocal keyword

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())