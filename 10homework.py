coins = int(input("Введите количество монеток: "))
up = 0
down = 0
while coins != 0:
    coins-=1
    if int(input("Сторона: ")) == 1:
        up+=1
    else:
        down+=1
if up > down:
    print(down)
else:
    print(up)