from math import sqrt
a = int(input("Value of a"))
b = int(input("Value of b"))
c = int(input("Value of c"))
disc = b**2 - 4*a*c
x1 = (-b + sqrt(disc)) / (2*a)
x2 = (-b - sqrt(disc)) / (2*a)
print(f"The roots are {x1} and {x2}")