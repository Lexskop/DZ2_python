# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

def calc():
    """
    Метод расчета набора произведения чисел от 1 до N в список
    """
    user_number = input('Введите значение N -> ')
    if user_number.lower() == 'x':
            print('Bye!')
            return
    while user_number.isdigit() == False or int(user_number) <= 0:
        print('Вы ошиблись и ввели "не число" или число меньше 0!')
        user_number = input('Введите значение N -> ')
        if user_number.lower() == 'x':
            print('Bye!')
            return
    user_number = int(user_number)
    list = []
    sum = 1
    for i in range(user_number):
        list.append(i)
        sum *= i+1
        list[i] = sum
    print(list)
    user_another_try()


def user_another_try():
    """
    Метод для возможности не закрывая программу воспользоваться ею еще раз
    """
    user_choice = input(
        'Вы хотите продолжить работу с программой? Да - Y, Нет - N - > ')
    while user_choice.lower() != 'y' and user_choice.lower() != 'n' and user_choice.lower() != 'x':
        user_choice = input(
            'Пожалуйста, введите верное решение. Если хотите продолжить работу - введите Y, если желаете закрыть программу - введите N или X -> ')
    if user_choice.lower() == 'y':
        calc()
    else:
        print('Bye!')

print('Приветствую! Эта программа принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N, не используя функцию math.factorial!')
calc()
