# !/usr/bin/env python
# -- coding: utf-8 --
"""
@Filename:   Task3_palindrome.py
@Date:       07.04.2024
@Time:       13:58
@Author:     Mentor
@Software:   PyCharm
"""

"""
Справка!
Палиндром — это последовательность символов, 
которая одинаково читается в обоих направлениях.

Пример:
шалаш, КАЗАК, п0т0п, иЩи, МадаМ, radar, qqrthmhtrqq, 11422411 и т.д.
"""


class Palindrome():
    """ Класс создания атрибутов для проверки на палиндром"""

    def __init__(self, message):
        """
        Функция инициализирует атрибут message - слово,
        которое необходимо проверить на палиндром
        """
        self.message = message

    def mirror_index(self):
        """
        1 метод. Использование зеркальной индексации массива в Python

        Входной параметр:
            message: последовательность символов (слово).
        Выходное значение:
            is_palindrome: логическое утверждение (True или False)
        """
        # По умолчанию задаем переменную-флаг, имеющую истинное значение
        is_palindrome = True
        # Делаем проверку на полиндром,
        # используя зеркальную строку и сравнения с исходной
        if self.message != self.message[::-1]:
            # Если строка не отвечает условию,
            # то присваиваем переменной-флагу значение на ложное
            is_palindrome = False

        # Результат функции - это логическое утверждение (Правда или ложь)
        return is_palindrome

    def cycle(self):
        """
        2 метод. Использование цикла и сравнивание символы на симметричных поз.

        Входной параметр:
            message: последовательность символов (слово).
        Выходное значение:
            is_palindrome: логическое утверждение (True или False)
        """

        # По умолчанию задаем переменную-флаг, имеющую истинное значение
        is_palindrome = True

        # Задаем цикл перебора символов в слове.
        # Перебор от первого символа до середины
        for i in range(0, len(self.message) // 2):
            # Если символ с индексом i от начала строки не равен символу i
            # от конца строки (-i -1), переменная-флаг меняет знач на ложь
            if self.message[i] != self.message[-i - 1]:
                is_palindrome = False
                # Прерываем работу программы
                break

        # Результат функции - это логическое утверждение (Правда или ложь)
        return is_palindrome

    def only_text_symbols(self):
        """
        3 метод. Определение палиндрома с учетом пробелов и знаков препинания

        Входной параметр:
            message: последовательность символов (слово).
        Выходное значение:
            is_palindrome: логическое утверждение (True или False)
        """
        # Задаем цикл перебора символов в заданной строке
        for char in self.message:
            # Посимвольно удаляем все небуквенные символы функцией isalnum
            char.isalnum()
            # Переприсваиваем значение строки только буквенные символы
            self.message = ''.join(char).lower()

        # Результат функции - это логическое утверждение (Правда или ложь)
        return self.message == self.message[::-1]

    def half_stack_method(self):
        """
        4 метод. Определение палиндрома при помощи стека.
        Сначала обрабатываем первую половину слова,
        затем сравниваем ее со второй половиной.

        Входной параметр:
            message: последовательность символов (слово).
        Выходное значение:
            is_palindrome: логическое утверждение (True или False)
        """
        # Задаем цикл перебора символов в заданной строке
        for char in self.message:
            # Посимвольно удаляем все небуквенные символы функцией isalnum
            char.isalnum()
            # Задаем пустой стек. В последствии будем добавлять туда 1 половину
            stack = list()
            # Добавляем в стек текущий символ в исследуемом слове message
            stack.append(char)
            # Проверяем, если текущий символ не равен последнему в стеке
            if char != stack.pop():
                return False

            return True


def palindrome_recursion(message):
    """
    5 метод. Использование рекурсивной функции

    Входной параметр:
        message: последовательность символов (слово).
    Выходное значение:
        palindrome_recursion: логическое утверждение (True или False)
    """

    # Учитываем случай, когда в проверяемом слове 1 буква
    if len(message) < 2:
        # В рассматриваемом случае слово из 1 буквы всегда палиндром
        return True
    # Рассматриваем первый и последний элемент строки.
    if message[0] != message[-1]:
        # Если элементы не равны, то слово не является палиндромом
        return False
    # Возвращаем логическое значение рекурсивной функции.
    # Проходим слово от 1 до последнего символа
    return palindrome_recursion(message[1:-1])


# Проверка работы описанных функций на определение палиндрома
if __name__ == '__main__':

    # Пример слова, которое будем проверять на палиндром.
    word = 'radar'
    palindrome = Palindrome(word)

    # Пример для 1 метода:
    example_palindrome_mirror_index = Palindrome.mirror_index(palindrome)
    if example_palindrome_mirror_index == True:
        print(f'Строка {word} является палиндромом.')
    else:
        print(f'Строка {word} не является палиндромом.')

    # Пример для 2 метода:
    example_palindrome_cycle = Palindrome.cycle(palindrome)
    if example_palindrome_cycle == True:
        print(f'Строка {word} является палиндромом.')
    else:
        print(f'Строка {word} не является палиндромом.')

    # Пример для 3 метода:
    example_palindrome_only_text_symbols = Palindrome.only_text_symbols(
        palindrome)
    if example_palindrome_only_text_symbols == True:
        print(f'Строка {word} является палиндромом.')
    else:
        print(f'Строка {word} не является палиндромом.')

    # Пример для 4 метода:
    example_palindrome_half_stack_method = Palindrome.half_stack_method(
        palindrome)
    if example_palindrome_half_stack_method == True:
        print(f'Строка {word} является палиндромом.')
    else:
        print(f'Строка {word} не является палиндромом.')

    # Пример для 5 метода:
    example_palindrome_recursion = palindrome_recursion(word)
    if example_palindrome_recursion == True:
        print(f'Строка {word} является палиндромом.')
    else:
        print(f'Строка {word} не является палиндромом.')

    # Пример проверки на палиндром с учетом всех методов проверки
    if (example_palindrome_mirror_index == True) and \
            (example_palindrome_cycle == True) and \
            (example_palindrome_only_text_symbols == True) and \
            (example_palindrome_half_stack_method == True) and \
            (example_palindrome_recursion == True):
        print(f'Строка {word} является палиндромом. Проверено 5 методами')
