def calculate(a, b):
     return a*a+ 2*a*b + b*b
print(calculate(2, 3))

x = lambda a, b : a + b
print(x(5, 9))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def myfunc(n):
   return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))