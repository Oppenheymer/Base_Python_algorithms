# !/usr/bin/env python
# -- coding: utf-8 --
"""
@Filename:   Task_2_test_rle_compression.py
@Date:       06.04.2024
@Time:       20:44
@Author:     Mentor
@Software:   PyCharm
"""
# Добавляем модуль тестирования функции
import unittest
# Из нашего файла с функцией импортируем саму функцию для кодирования строки
from Task_2_rle_compression import encode_message


class EncodeTestCase(unittest.TestCase):
    """
    Класс для тестирования функции encode_message Task_2_rle_compression.py
    (преобразование сообщения по алгоритму RLE)
    """

    def test_encode_message(self):
        """
        Тест-функция проверяет, преобразовываются ли строки к формату RLE.
        Пример входной строки:
            ABCABCABCDDDFFFFFF
        Пример выходной строки:
            1A1B1C1A1B1C1A1B1C3D6F
        """
        # Задаем пример тестируемой функции и даем на вход тестовую последоват.
        encoded_string = encode_message('ABCABCABCDDDFFFFFF')
        # Проверяем равенство выходного значения функции
        # с заданным выходным значением
        self.assertEqual(encoded_string, '1A1B1C1A1B1C1A1B1C3D6F')


# Проверка теста
if __name__ == '__main__':
    unittest.main()
