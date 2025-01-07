#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Задание 2.
# Создать класс Money для работы с денежными суммами. Сумма должна быть представлена списком,
# каждый элемент которого – десятичная цифра. Максимальная длина списка – 100 цифр, реальная
# длина задается конструктором. Младший индекс соответствует младшей цифре денежной суммы.
# Младшие две цифры – копейки. (Вариант 25 (4)).

class Money:
    MAX_SIZE = 100  # Максимальная длина списка

    def __init__(self, amount):
        """
        Инициализация денежной суммы.
        :param amount: список цифр, где младший индекс соответствует младшей цифре.
        """
        if len(amount) > Money.MAX_SIZE:
            raise ValueError(f"Длина списка не должна превышать {Money.MAX_SIZE}.")

        # Проверяем, что все элементы списка - цифры от 0 до 9
        if not all(isinstance(d, int) and 0 <= d <= 9 for d in amount):
            raise ValueError("Все элементы списка должны быть цифрами от 0 до 9.")

        self.amount = amount[:]
        self._size = len(amount)  # Максимальная длина для объекта
        self._count = len(amount)  # Текущее количество элементов

    def size(self):
        """
        Возвращает максимальную длину для данного объекта.
        """
        return self._size

    def __len__(self):
        """
        Возвращает текущее количество элементов списка.
        """
        return self._count

    def __getitem__(self, index):
        """
        Позволяет обращаться к элементам суммы по индексу.
        :param index: индекс элемента.
        """
        if not (0 <= index < self._count):
            raise IndexError("Индекс выходит за пределы текущего количества элементов.")
        return self.amount[index]

    def __setitem__(self, index, value):
        """
        Позволяет изменять элементы суммы по индексу.
        :param index: индекс элемента.
        :param value: новое значение (цифра от 0 до 9).
        """
        if not (0 <= index < self._count):
            raise IndexError("Индекс выходит за пределы текущего количества элементов.")
        if not isinstance(value, int) or not (0 <= value <= 9):
            raise ValueError("Значение должно быть цифрой от 0 до 9.")
        self.amount[index] = value

    def append(self, digit):
        """
        Добавляет новую цифру в сумму.
        :param digit: цифра от 0 до 9.
        """
        if self._count >= Money.MAX_SIZE:
            raise ValueError("Достигнута максимальная длина списка для данного объекта.")
        if not isinstance(digit, int) or not (0 <= digit <= 9):
            raise ValueError("Значение должно быть цифрой от 0 до 9.")
        self.amount.append(digit)
        self._count += 1

    def remove(self, index):
        """
        Удаляет элемент по индексу.
        :param index: индекс элемента.
        """
        if not (0 <= index < self._count):
            raise IndexError("Индекс выходит за пределы текущего количества элементов.")
        del self.amount[index]
        self._count -= 1

    def __str__(self):
        """
        Возвращает строковое представление денежной суммы в формате рублей и копеек.
        """
        if self._count < 2:
            return f"0.{''.join(map(str, self.amount[::-1]))} руб."

        rubles = ''.join(map(str, self.amount[2:][::-1])) or '0'
        kopecks = ''.join(map(str, self.amount[:2][::-1]))
        return f"{rubles}.{kopecks} руб."


# Пример использования
if __name__ == "__main__":
    money = Money([5, 0, 1])  # 105 рублей и 05 копеек
    print("Введенная сумма: ", money)  # Вывод: 1.05 руб.
    print("Размер:", money.size())  # Максимальная длина объекта
    print("Текущее количество элементов:", len(money))

    money.append(2)  # Добавляем цифру (увеличиваем сумму) и увеличиваем размер списка
    print("Увеличенная сумма: ", money)  # Вывод: 21.05 руб.
    print("Размер:", money.size())  # Максимальная длина объекта
    print("Текущее количество элементов:", len(money))

    print("Младшая цифра: ", money[0])  # Доступ к младшей цифре: 5
    money[0] = 9  # Изменяем младшую цифру
    print("Изменение младшей цифры: ", money)

    money.remove(0)  # Удаляем младшую цифру
    print("Удаление младшей цифры: ", money)

    print("Размер:", money.size())  # Максимальная длина объекта
    print("Текущее количество элементов:", len(money))
