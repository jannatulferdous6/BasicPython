def maximum(a, b):
    if a >= b:
        return a
    else:
        return b
    
a = 2
b = 4
print(maximum(a, b))

maximum = max(a, b)
print(maximum)

print(a if a>= b else b)

maximum = lambda a, b: a if a>=b else b
print(f'{maximum (a, b)} is a maximum number')

x = [a if a>b else b]
print("maximum number is: " ,x)

x = [a, b]
x.sort()
print(x[-1])