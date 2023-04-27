from math import sqrt
num = float(input("Введите проверяемое число:"))
a = 0
b = 1
change = None
count = 2
check1 = sqrt((num**2)*5 - 4)
check2 = sqrt((num**2)*5 + 4)

if check1 % 1 == 0 or check2 % 1 == 0:
    if num == 0:
        print("1")
    else:
        while num != b :
            change = b
            b = a + b
            a = change
            count+=1
        print(count)
else:
    print("-1")