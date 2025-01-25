# !/usr/bin/env python
# -- coding: utf-8 --
"""
@Filename:   Task_1_test_binary_search.py
@Date:       07.04.2024
@Time:       12:55
@Author:     Mentor
@Software:   PyCharm
"""
import random
# Добавляем модуль для тестирования функции
import unittest
# Из нашего файла с функцией импортируем саму функцию для бинарного поиска
from Task1_binary_search import binary_search_func
# Импортируем функцию для создания произвольных массивов
from Task1_random_array_generator import random_array_func

class BinarySearchTestCase(unittest.TestCase):
    """
    Класс для тестирования функции binary_search_func Task_1_binary_search.py
    (бинарный поиск элемента в отсортированном массиве)
    """

    def test_binary_search(self):
        """
        Тест-функция проверяет, как реализуется бинарный поиск
        в упорядоченном по возрастанию массиве целочисленных значений.

        Пример входных данных:
            1. Массив упорядоченных по возрастанию целочисленных значений
            2. Значения для выполнения функции бинарного поиска
        Пример выходных данных:
            index: номер элемента, значение которого совпадает с заданным знач.
        """
        # Пример списка для выполнения функции бинарного поиска
        test_list = random_array_func()

        # Пример значения для выполнения функции бинарного поиска
        test_value = test_list[random.randint(0, len(test_list)-1)]

        # Задаем тест-функцию, реализующую бинарный поиск
        test_binary_search = binary_search_func(test_list, test_value)

        # Сравниваем результат работы алгоритма с выходным значением
        self.assertEqual(test_list[test_binary_search],
                        test_list[test_list.index(test_value)])


# Проверка теста
if __name__ == '__main__':
    unittest.main()
