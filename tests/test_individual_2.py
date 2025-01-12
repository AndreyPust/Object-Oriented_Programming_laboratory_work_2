#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from src.individual_2 import Money


class TestMoney(unittest.TestCase):
    """Тесты для класса Money."""

    def test_initialization_valid(self):
        """Проверка корректной инициализации объекта Money."""
        money = Money([5, 0, 1])  # 105 рублей и 05 копеек
        self.assertEqual(money.amount, [5, 0, 1])
        self.assertEqual(len(money), 3)

    def test_initialization_invalid_length(self):
        """Проверка выброса исключения при превышении максимальной длины списка."""
        with self.assertRaises(ValueError):
            Money([1] * 101)  # Превышение длины

    def test_initialization_invalid_elements(self):
        """Проверка выброса исключения при наличии некорректных элементов в списке."""
        with self.assertRaises(ValueError):
            Money([5, 10, 1])  # Неверное значение 10

    def test_size(self):
        """Проверка метода size."""
        money = Money([1, 2, 3])
        self.assertEqual(money.size(), 3)

    def test_getitem_valid(self):
        """Проверка получения элемента по индексу."""
        money = Money([5, 0, 1])
        self.assertEqual(money[0], 5)

    def test_getitem_invalid_index(self):
        """Проверка выброса исключения при некорректном индексе."""
        money = Money([5, 0, 1])
        with self.assertRaises(IndexError):
            _ = money[10]

    def test_setitem_valid(self):
        """Проверка установки значения по индексу."""
        money = Money([5, 0, 1])
        money[0] = 7
        self.assertEqual(money[0], 7)

    def test_setitem_invalid_value(self):
        """Проверка выброса исключения при некорректном значении."""
        money = Money([5, 0, 1])
        with self.assertRaises(ValueError):
            money[0] = 10

    def test_append_valid(self):
        """Проверка добавления нового элемента."""
        money = Money([5, 0, 1])
        money.append(2)
        self.assertEqual(money.amount, [5, 0, 1, 2])

    def test_append_invalid(self):
        """Проверка выброса исключения при добавлении некорректного значения."""
        money = Money([5, 0, 1])
        with self.assertRaises(ValueError):
            money.append(12)

    def test_remove_valid(self):
        """Проверка удаления элемента по индексу."""
        money = Money([5, 0, 1])
        money.remove(0)
        self.assertEqual(money.amount, [0, 1])

    def test_remove_invalid_index(self):
        """Проверка выброса исключения при некорректном индексе удаления."""
        money = Money([5, 0, 1])
        with self.assertRaises(IndexError):
            money.remove(10)

    def test_str(self):
        """Проверка строкового представления объекта Money."""
        money = Money([5, 0, 1])  # 105 рублей и 05 копеек
        self.assertEqual(str(money), "1.05 руб.")


if __name__ == "__main__":
    unittest.main()
