q = float(input('Введите q: '))
w = float(input('Введите w: '))
e = float(input('Введите e: '))


if q > w:
    if q > e:
        print (f"{q} самое большое число q")
elif e > q:
    if e > w:
        print (f"{e} самое большое число f")
if w > q:
    if w > e:
        print (f"{w} самое большое число w ")
else:
    print ("ошибка")