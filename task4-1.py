# 4 - По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого.
# При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, остальные получили по две монеты.
# Далее человек, на котором остановился счет, отдает все свои монеты следующему по счету человеку, а сам выбывает из круга.
# Процесс продолжается с места остановки аналогичным образом до последнего человека в круге. Составьте алгоритм, который проводит эту игру.
# Если хотите делать паузы, то импортируйте библиотеку time и используйте оттуда функцию sleep.
# Определите номер этого человека и количество монет, которые оказались у него в конце игры.

import random


def game():
    """
    Непосредственно метод игры
    """
    N = random.randint(2, 10)
    list_of_coins = [0 for i in range(N)]
    list_of_players = [i+1 for i in range(len(list_of_coins))]
    count = 1
    print('Стартовое количество монет ->', list_of_coins)
    print('Стартовые порядковые номера участников ->', list_of_players)
    while len(list_of_coins) != 1:
        print('------ROUND ->', count, '------')
        roll_of_master_of_dice = random.randint(0, len(list_of_coins)-1)
        print('Ведущий случайно выбирает число -> ', roll_of_master_of_dice+1)
        for i in range(len(list_of_coins)):
            if i <= roll_of_master_of_dice:
                list_of_coins[i] += 1
            if i == roll_of_master_of_dice:
                if i != len(list_of_coins):
                    try:
                        list_of_coins[i + 1] += list_of_coins[roll_of_master_of_dice]
                    except:
                        None
                if roll_of_master_of_dice == len(list_of_coins)-1:
                    list_of_coins[0] += list_of_coins[roll_of_master_of_dice]
            if i > roll_of_master_of_dice:
                list_of_coins[i] += 2
        # print('plus ', list_of_coins) # отладка правильного сложения монет
        del list_of_coins[roll_of_master_of_dice]
        del list_of_players[roll_of_master_of_dice]
        
        # print('delete ', list_of_coins) # отладка правильного удаления игрока
        if roll_of_master_of_dice != len(list_of_coins)+1:
            temp_coins = list_of_coins[roll_of_master_of_dice:len(list_of_coins)+1]
            temp_players = list_of_players[roll_of_master_of_dice:len(list_of_players)+1]
            # print('temp1 ', temp_coins) # отладка правильного выделения монет игроков для переноса в левую часть
            # print('temp2 ', temp_players) # отладка правильного выделения игроков для переноса в левую часть
            list_of_coins[roll_of_master_of_dice:len(list_of_coins)+1] = list_of_coins[0:roll_of_master_of_dice]
            list_of_coins[0:roll_of_master_of_dice] = temp_coins
            list_of_players[roll_of_master_of_dice:len(list_of_players)+1] = list_of_players[0:roll_of_master_of_dice]
            list_of_players[0:roll_of_master_of_dice] = temp_players
        if len(list_of_players) != 1:
            print('Количество монет по результату',count,'раунда ->', list_of_coins)
            print('Место игроков по результату',count,'раунда ->', list_of_players)
        count += 1
    print('Финальная сумма -> ', list_of_coins)
    print('Победитель под номером -> ', list_of_players)
    user_another_try()

def user_another_try():
    """
    Метод для возможности не закрывая программу воспользоваться ею еще раз
    """
    user_choice = input('Вы хотите продолжить работу с программой? Да - Y, Нет - N - > ')
    while user_choice.lower() != 'y' and user_choice.lower() != 'n' and user_choice.lower() != 'x':
        user_choice = input('Пожалуйста, введите верное решение. Если хотите продолжить работу - введите Y, если желаете закрыть программу - введите N или X -> ')
    if user_choice.lower() == 'y':
        game()
    else:
        print('Bye!')

print('Приветствую! Правила игры: По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого.')
print('При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, остальные получили по две монеты.')
print('Далее человек, на котором остановился счет, отдает все свои монеты следующему по счету человеку, а сам выбывает из круга.')
print('Процесс продолжается с места остановки аналогичным образом до последнего человека в круге.')
print('Игра определит номер этого человека и количество монет, которые оказались у него в конце игры.')

game()
