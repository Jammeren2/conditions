b = int(input())
s = int(input())
if b % s == 0:
    print(f"{b} кратно {s}.")
else:
    r = b % s
    print(f"{b} не кратно {s}. Остаток от деления: {r}")
