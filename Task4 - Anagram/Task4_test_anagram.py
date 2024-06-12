# !/usr/bin/env python
# -- coding: utf-8 --
"""
@Filename:   Task4_test_anagram.py
@Date:       29.04.2024
@Time:       15:40
@Author:     Mentor
@Software:   PyCharm
"""
# Импортируем модуль для тестирования функций
import unittest

# Импортируем модуль для генерации входных значений
from Task4_anagram_generator import (random_string_func,
                                    anagrama_string_gen)
# Из файла импортируем саму функцию для проверки на анаграмму
from Task4_anagram import AnagramaWords

class AnagramaTestCase(unittest.TestCase):
    """
    Класс для тестирования функции anagrama_func класса AnagramaWords
    (Проверка, являются ли 2 слова анаграммами методом сравнивания словарей,
    полученных из этих двух слов)

    В тестируемом классе будет взят 1 метод проверки на анаграмму
    (функция anagram_func) - использование словарей для записи в них
    всех символов 2 слов. В последствии будут сравниваться между собой 2 словаря.

    Исходной последовательностью будет случайное слово,
    сгенерированное с помощью функции random_string_func().
    При помощи функции anagrama_string_gen() будет вычислено зеркальное слово.
    Эти два слова ьудут проверяться на анаграмму.
    """

    def test_anagrama_func(self):
        """
        Тест-функция проверяет, являются ли 2 слова анаграммами или нет.

        Пример входной строки:
            JsYqHNY (Случайно сгенерированное слово)
            YNHqYsJ (Зеркалированное случайное слово)
        Выходное значение:
            логическое утверждение (True или False)
        """

        # Задаем слово, заданное случайным образом
        test_first_word = random_string_func()
        # Создаем второе слово при помощи метода зеркалирования 1 слова
        test_second_word = anagrama_string_gen(test_first_word)[0]

        # Создаем кортеж из 2 знач, как элемент класса AnagramaWords
        tuple_words = AnagramaWords(test_first_word, test_second_word)

        # Проверяем сгенерированный кортеж на анаграмму 1 методом
        # Результат - логическое утверждение (True или False)
        is_anagrama = AnagramaWords.anagrama_func(tuple_words)

        # Проверяем истинность значения
        self.assertTrue(is_anagrama)

# Проверка теста
if __name__ == '__main__':
    unittest.main()