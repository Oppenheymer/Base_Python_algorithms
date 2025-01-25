# !/usr/bin/env python
# -- coding: utf-8 --
"""
@Filename:   Task1_binary_search.py
@Date:       25.01.2025
@Time:       18:51
@Author:     Mentor
@Software:   PyCharm
"""

"""
Справка!
Бинарный поиск — это алгоритм, используемый для поиска элемента 
в отсортированном массиве путем многократного деления интервала поиска пополам.
"""


def binary_search_func(data_list, desire_value):
    """
    Функция, реализующая бинарный поиск в упорядоченном по возрастанию массиве
    целочисленных значений.

    По умолчанию входной список (массив данных) считаем упорядоченным
    по возрастанию, то есть data_list[0] <= data_list[1] <= data_list[N]

    Входные параметры:
        1. data_list: список данных (integer), упорядоченный по возрастанию
        2. desire_value: заданное значение. По умолчанию считаем,
        что оно встречается в массиве данных
    Выходное значение:
        index: номер элемента, значение которого совпадает с заданным значением
    """
    # Задаем первый и последний элементы массива данных.
    # Первый элемент с индексом first = 0
    first_index_element = 0

    # Последний элемент с индексом last = длина массива - 1
    last_index_element = len(data_list) - 1

    # Задаем начальное значение искомого индекса. В последствии будет меняться
    # Значение -1 - это переменная-флаг. Начальное значение может быть любым.
    index = - 1

    # Цикл перебора всех элементов массива от первого до последнего
    while ((first_index_element <= last_index_element) and (index == -1)):
        # Задаем индекс среднего элемента массива, как среднее арифметич.
        mid_index_element = (first_index_element + last_index_element) // 2
        # Если значение элемента с заданным индексом равняется искомому знач.
        # то определяем искомый индекс, как заданный средний элемент массива
        if data_list[mid_index_element] == desire_value:
            index = mid_index_element
        # Иначе делаем перебор значений массива
        else:
            # Если искомое значение меньше среднего элемента массива,
            # то переприсваиваем последний элемент = средний элемент массива -1
            # (отбрасываем все значения больше среднего (справа))
            if desire_value < data_list[mid_index_element]:
                last_index_element = mid_index_element - 1
            # Иначе переприсваиваем первый элемент = средний элемент массива -1
            # (отбрасываем все значения меньше среднего (слева))
            else:
                first_index_element = mid_index_element + 1

    # После выполнения цикла получаем индекс элемента массива с заданным знач.
    if index != -1:
        return index
    # Если index == -1 (невозможное начальное значение) - элемент не найден
    else:
        print('В заданном массиве не найден элемент с искомым значением.')


if __name__ == '__main__':
    # Блок работы программы с пользовательскими данными
    try:
        # Задаем пользовательский список
        my_list = []
        for num_element in input('\nВведите элементы числового массива, '
                                'в котором будет производиться бинарный поиск,'
                                ' через "пробел":\n\t').split():
            my_list.append(int(num_element))
            # Сортируем массив по возрастанию
            my_list.sort()

        # Задаем пользовательское значение
        my_value = int(input('\nВведите число, '
                            'которое необходимо найти в массиве:\n\t'))

        print('\nМой список для бинарного поиска\n', my_list)
        print('\nМое число для поиска в массиве \n', my_value)
        # Задаем функцию бинарного поиска
        my_binary_search = binary_search_func(my_list, my_value)

        if ((my_binary_search != -1) and (my_binary_search != None)):
            print(
                f'\nЭлемент списка с индексом {my_binary_search} '
                f'соответствует заданному значению  {my_value}.')

    # В случае ошибки ввода или отсутствия данных программа будет работать
    # с произвольными значениями, заданными по умолчанию для функции
    except ValueError:
        # Запуск функции с произвольными данными
        print('\nВведенные пользовательские данные не позволяют '
            'адекватно работать алгоритму программы.\n'
            'Пример работы функции с произвольными значениями:\n')

        # Пример списка для выполнения функции бинарного поиска
        example_list = random_array_func()
        print('\nПример сгенерированного списка\n', example_list)

        # Пример для выполнения функции бинарного поиска (входит в список)
        example_value = example_list[random.randint(0, len(example_list)-1)]
        print('\nПример числа из сгенерированного списка\n', example_value)

        example_binary_search = binary_search_func(example_list, example_value)

        if ((example_binary_search != -1) and (example_binary_search != None)):
            print(
                f'\nЭлемент списка с индексом {example_binary_search} '
                f'соответствует заданному значению  {example_value}.')
