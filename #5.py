a = float(input("1: "))
b = float(input("2: "))
c = float(input("3: "))

if a + b > c and a + c > b and b + c > a:
    print("существует.")
else:
    print("не существует.")
