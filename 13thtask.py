days = int(input("Введите количество дней:"))
hotdaysmax = 0
count = 0
temp = None
while days != 0:
    days -= 1
    temp = int(input("Среднесуточная температура: "))
    if temp > 0:
        count+=1

        if hotdaysmax < count:
            hotdaysmax = count
    else:
        count = 0
print("Самая длинная оттепель:", hotdaysmax)