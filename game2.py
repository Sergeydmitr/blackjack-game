from random import shuffle

def diler(i):
    count = 0
    current = koloda.pop()
    count += current
    current = koloda.pop()
    count += current
    while count < 21 and count < i:
        current = koloda.pop()
        count += current
    print("Счёт дилера: ", count)
    return count

def game():
    count = 0
    current = koloda.pop()
    count += current

    current = koloda.pop()
    count += current

    print("Ваш счёт: ", count)
    while count < 21:
        k = input("Тянуть карту? 0 - да, 1 - нет ")
        if k == '0':
            current = koloda.pop()
            count += current
            print("Ваш счёт: ", count)
    
        elif k == '1':
            count_diler = diler(count)
            if count > count_diler or count_diler > 21:
                print("Поздравляем! Вы выиграли!")
            elif count == count_diler:
                print("Ничья!")
            else:
                print("Вы проиграли!")
            break
        else:
            print("Я вас не понимаю")
            continue
    else:
        if count < 22:
            count_diler = diler(count)
            if count > count_diler or count_diler > 21:
                print("Поздравляем! Вы выиграли!")
            elif count == count_diler:
                print("Ничья!")
            else:
                print("Вы проиграли!")
        else:
            print("Вы проиграли!")

v = '0'
while v == '0':
    koloda = [6,7,8,9,10,2,3,4,11] * 4
    shuffle(koloda)
    game()
    v = input("Новая игра? 0 - да, 1 - нет ")