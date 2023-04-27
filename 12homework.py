from math import sqrt
c = int(input("Введите сумму: "))
d = int(input("Введите их произведение: "))
squaresum = c*c
squaremin = c*c - 4 * d
num1 = (sqrt(squaresum)+sqrt(squaremin))/2
num2 = (sqrt(squaresum)- sqrt(squaremin))/2
print(num1, num2)