# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# (-0.56) -> 11

import math  # впервые воспользовался выражением import

def calc1():
    """
    Решение математическим методом
    """
    number = float(input('Введите вещественное число -> '))
    userNumber = number
    number = abs(number)
    sum = 0
    while number != int(number):
        number = round(number*10, 10)
    if number != 0:
        count = int(math.log10(number) + 1) # именно для логарифма использовал import
    for i in range(count):
        sum = sum + (number % (10**(i + 1)) - (number % (10**i))) / 10**i
    print(f'Сумма цифр в числе {userNumber} -> {int(sum)}')

    user_another_try()

def calc2():
    """
    Решение строковым методом
    """
    number = input('Введите вещественное число -> ')
    sum = 0
    for i in number:
        if i.isdigit():
            sum += int(i)
    print(f'Сумма цифр в числе {number} -> {int(sum)}')
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
        print('Программа выполнена в двух вариантах. Введите 1, если хотите решить задачу математически, либо введите 2, если хотите решить задачу строковым методом! Введите X, чтобы завершить программу')
        user_method = input('Ваше решение -> ')
        if user_method.lower() == 'x':
            print('Bye!')
        if user_method == '1':
            calc1()
        if user_method == '2':
            calc2()
    else:
        print('Bye!')

def user_method_choice():
    """
    Конкретно в данной программе - способ выбирать каким вариантом решать задачку
    """
    print('Программа выполнена в двух вариантах. Введите 1, если хотите решить задачу математически, либо введите 2, если хотите решить задачу строковым методом! Введите X, чтобы завершить программу')
    user_method = input('Ваше решение -> ')
    if user_method.lower() == 'x':
        print('Bye!')
    if user_method == '1':
        calc1()
    if user_method == '2':
        calc2()

print('Приветствую! Эта программа принимает на вход вещественное число и показывает сумму его цифр, учитывая, что число может быть отрицательным!')
user_method_choice()