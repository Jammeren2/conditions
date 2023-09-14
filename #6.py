x = float(input("X: "))
y = float(input("Y: "))
radius = float(input("радиус: "))

distance = (x**2 + y**2)**0.5

if distance <= radius:
    print("принадлежит кругу.")
else:
    print("не принадлежит кругу.")
