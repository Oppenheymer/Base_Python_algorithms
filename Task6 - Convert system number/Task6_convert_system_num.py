# !/usr/bin/env python
# -- coding: utf-8 --
"""
@Filename:   Task6_convert_system_num.py
@Date:       01.05.2024
@Time:       10:11
@Author:     Mentor
@Software:   PyCharm
"""
# Добавление библиотеки случайных чисел
import random

def convert_system_num(number = random.randint(0, 9999),
                       base = random.randint(2, 50),
                       digits = '0123456789abcdefghijklmnopqrstuvwxyz'):
    """
    Функция позволяет преобразовать число из десятичной системы счисления
    в произвольную систему счисления.

    Входной параметр:
        1. number: произвольное целое число (integer)

        2. base: основание системы счисления (integer).
        Для адекватной работы алгоритма base >= 2.

        3. digits (Необязательный параметр): мощность алфавита;
        набор символов, применимый для преобразования в систему счисления
        По умолчанию digits = '0123456789abcdefghijklmnopqrstuvwxyz'

    Выходное значение:
        converted_num: преобразованное число в заданной системе счисления

    ! Примечание!
    Функция будет ограничена только наличием символов
    в переводимой системе счисления. Функция корректно работает для base[2:50].
    """

    # Отсеиваем случай, когда основание системы счисления меньше 2
    if base < 2:
        return 'Основание системы счисления < 2. Некорректный запрос'

    # Если преобразуемое число меньше основания СС,
    # то результат преобразования и будет заданным числом
    if number < base:
        return digits[number]
    # Иначе преобразуем число по правилу:
    else:
        return convert_system_num(number // base, base) + digits[number % base]

# Проверка работы функции
if __name__ == '__main__':

    # Блок работы программы с пользовательскими данными
    try:
        my_num  = int(input('\nВведите число в десятичной СС,'
                            '\nкоторое будет преобразовано'
                            'в выбранную СС:\n\t'))
        my_base = int(input('Введите основание выбранной СС,'
                            ' записанное в десятичном виде:\n\t'))
        # Запуск функции с пользовательскими данными
        print('Результат:\n\t', convert_system_num(my_num, my_base))

    # В случае ошибки ввода или отсутствия данных программа будет работать
    # с произвольными значениями, заданными по умолчанию для функции
    except ValueError:
        print('\nВведенные пользовательские данные не позволяют '
            'адекватно работать алгоритму программы.\n'
            'Пример работы функции с произвольными значениями:\n')

        print('Случайно сгенерированное число:\n\t',
            convert_system_num.__defaults__[0])
        print('Случайно сгенерированная СС:\n\t',
            convert_system_num.__defaults__[1])
        # Запуск функции с произвольными данными
        print('Результат:\n\t', convert_system_num())
