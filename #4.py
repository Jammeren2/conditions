x = float(input("X: "))
y = float(input("Y: "))

if x > 0 and y > 0:
    print("в первой четверти.")
elif x < 0 and y > 0:
    print("во второй четверти.")
elif x < 0 and y < 0:
    print("в третьей четверти.")
elif x > 0 and y < 0:
    print("в четвертой четверти.")
else:
    print("Ошибка")
