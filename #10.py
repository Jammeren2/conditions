import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Корни: x1 = {x1}, x2 = {x2}")
elif D == 0:
    x1 = -b / (2*a)
    print(f"Корень: x1 = {x1}")
else:
    print("не имеет корней.")
