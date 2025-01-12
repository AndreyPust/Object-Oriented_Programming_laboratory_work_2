#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from src.individual_1 import Pair


class TestPair(unittest.TestCase):
    """Тесты для класса Pair и перегрузки операторов."""

    def test_initialization(self):
        """Проверка корректной инициализации объекта Pair."""
        pair = Pair(10.5, 3)
        self.assertEqual(pair.first, 10.5)
        self.assertEqual(pair.second, 3)

    def test_initialization_invalid_price(self):
        """Проверка выброса исключения при некорректной цене."""
        with self.assertRaises(ValueError):
            Pair(-10, 3)

    def test_initialization_invalid_quantity(self):
        """Проверка выброса исключения при некорректном количестве."""
        with self.assertRaises(ValueError):
            Pair(10, -3)

    def test_cost(self):
        """Проверка вычисления стоимости товара."""
        pair = Pair(20.0, 4)
        self.assertEqual(pair.cost(), 80.0)

    def test_add(self):
        """Проверка корректности перегрузки оператора сложения."""
        pair1 = Pair(20.0, 3)
        pair2 = Pair(10.0, 2)
        result = pair1 + pair2
        self.assertAlmostEqual(result.first, 16.0, places=1)
        self.assertEqual(result.second, 2)

    def test_sub(self):
        """Проверка корректности перегрузки оператора вычитания."""
        pair1 = Pair(20.0, 3)
        pair2 = Pair(10.0, 2)
        result = pair1 - pair2
        self.assertEqual(result.first, 20.0)
        self.assertEqual(result.second, 4)

    def test_mul(self):
        """Проверка корректности перегрузки оператора умножения."""
        pair = Pair(15.0, 2)
        result = pair * 2
        self.assertEqual(result.first, 15.0)
        self.assertEqual(result.second, 4)

    def test_div(self):
        """Проверка корректности перегрузки оператора деления."""
        pair = Pair(10.0, 4)
        result = pair / 2
        self.assertEqual(result.first, 10.0)
        self.assertEqual(result.second, 2)

    def test_eq(self):
        """Проверка перегрузки оператора равенства."""
        pair1 = Pair(10.0, 2)
        pair2 = Pair(20.0, 1)
        self.assertTrue(pair1 == pair2)

    def test_lt(self):
        """Проверка перегрузки оператора меньше."""
        pair1 = Pair(10.0, 1)
        pair2 = Pair(20.0, 2)
        self.assertTrue(pair1 < pair2)

    def test_le(self):
        """Проверка перегрузки оператора меньше или равно."""
        pair1 = Pair(10.0, 2)
        pair2 = Pair(20.0, 1)
        self.assertTrue(pair1 <= pair2)


if __name__ == "__main__":
    unittest.main()
