a = float(input())
b = float(input())
c = float(input())
if a == b or a == c or b == c:
    print("Ошибка")
else:
    if (a < b < c) or (c < b < a):
        print(b)
    elif (b < a < c) or (c < a < b):
        print(a)
    else:
        print(c)
