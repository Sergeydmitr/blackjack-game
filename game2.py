from random import shuffle

def dealer(player_score):
    count = 0
    current = deck.pop()
    count += current
    current = deck.pop()
    count += current

    while count < 21 and count < player_score:
        current = deck.pop()
        count += current
    print("Счёт дилера: ", count)
    return count

def game():
    count = 0
    current = deck.pop()
    count += current
    current = deck.pop()
    count += current
    print("Ваш счёт: ", count)

    while count < 21:
        k = input("Тянуть карту? 0 - да, 1 - нет ")
        if k == '0':
            current = deck.pop()
            count += current
            print("Ваш счёт: ", count)
    
        elif k == '1':
            count_dealer = dealer(count)
            if count > count_dealer or count_dealer > 21:
                print("Поздравляем! Вы выиграли!")
            elif count == count_dealer:
                print("Ничья!")
            else:
                print("Вы проиграли!")
            break
        else:
            print("Я вас не понимаю")
            continue
    else:
        if count < 22:
            count_dealer = dealer(count)
            if count > count_dealer or count_dealer > 21:
                print("Поздравляем! Вы выиграли!")
            elif count == count_dealer:
                print("Ничья!")
            else:
                print("Вы проиграли!")
        else:
            print("Вы проиграли!")

play = '0'
while play = '0':
    deck = [6,7,8,9,10,2,3,4,11] * 4
    shuffle(deck)
    game()
    play = input("Новая игра? 0 - да, 1 - нет ")