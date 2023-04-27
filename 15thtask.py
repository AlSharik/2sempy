num = int(input(" Введите количество: "))
now = int(input("Вес current арбуза: "))
min = now
max = now
while num - 1 != 0:
    num -= 1
    now = int(input("Вес current арбуза: "))
    if min > now:
        min = now
    if max < now:
        max = now

print(min, max)