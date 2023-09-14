distance = float(input("дальность выстрела: "))

if 28 <= distance <= 30:
    print("ПОПАЛ")
elif distance >= 30:
    print("ПЕРЕЛЕТ")
elif 0 < distance < 28:
    print("НЕДОЛЕТ")
else:
    print("НЕ БЕЙ ПО СВОИМ")
