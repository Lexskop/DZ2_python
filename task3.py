# 3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.
# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

def calc():
    """
    Метод для создания искомого массива
    """
    count = 0
    list = []
    for i in input('Введите числа через пробел -> ').split():
        list.append(i)
    for i in range(len(list)):
        if int(list[i]) < 0:
            count += 1
    print('Вы ввели числа -> ', list)
    for i in range(len(list) + count):
        if int(list[i]) < 0:
            i += 1
            list.insert(i, 0)
    print('Ответ -> ', list)
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

print('Приветствую! Эта программа принимает на вход массив и после каждого отрицательного элемента массива вставляет элемент с нулевым значением.')
calc()