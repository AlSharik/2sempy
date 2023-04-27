num = int(input("Введите факториал:"))
factorial = 1
while num != 0:
    factorial *= num
    num -= 1
print(factorial)