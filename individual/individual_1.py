#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Задание 1.
# Поле «first» – дробное положительное число, цена товара;
# Поле «second» – целое положительное число, количество единиц товара.
# Реализовать метод «cost()» — вычисление стоимости товара (Вариант 25(5)).
# Также необходимо максимально задействовать средства перегрузки операторов.

class Pair:
    def __init__(self, first, second):
        """
        Метод инициализации, проверяет аргументы на корректность.
        """
        if not isinstance(first, (int, float)) or first <= 0:
            raise ValueError("Цена товара должна быть положительным дробным числом!")
        if not isinstance(second, int) or second <= 0:
            raise ValueError("Количество товара должно быть положительным целым числом!")

        self.first = float(first)  # Цена товара
        self.second = int(second)  # Количество товара

    def read(self):
        """
        Ввод значений с клавиатуры.
        """
        try:
            self.first = float(input("Введите цену товара (положительное дробное число): "))
            if self.first <= 0:
                raise ValueError("Цена должна быть положительным числом!")

            self.second = int(input("Введите количество товара (положительное целое число): "))
            if self.second <= 0:
                raise ValueError("Количество должно быть положительным целым числом!")
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
            return False
        return True

    def display(self):
        """
        Вывод информации о товаре.
        """
        print(f"Цена товара: {self.first}, Количество: {self.second}")

    def cost(self):
        """
        Метод для вычисления стоимости товара.
        """
        return self.first * self.second

    # Перегрузка оператора сложения
    def __add__(self, other):
        """
        Переопределим метод для получения товара со средними характеристиками двух товаров.
        """
        if not isinstance(other, Pair):
            raise TypeError("Сложение возможно только между товарами!")

        # Общее количество товаров
        total_quantity = self.second + other.second

        # Общая стоимость всех товаров
        total_cost = (self.first * self.second) + (other.first * other.second)

        # Среднее количество товара
        average_quantity = total_quantity / 2

        # Средняя стоимость единицы товара
        average_price = total_cost / total_quantity

        # Создание нового объекта со "средними" характеристиками
        return Pair(average_price, round(average_quantity))

    # Перегрузка оператора вычитания
    def __sub__(self, other):
        """
        Теперь логика вычитания такова, что вычисляется количество первого товара со своей стоимостью такая,
        как если бы не существовало второго товара (перераспределение всех денег на первый товар).
        self - это товар, на который уйдут все деньги второго товара other.
        """
        if not isinstance(other, Pair):
            raise ValueError("Вычитать можно только товары!")

        # Общая стоимость обоих товаров
        total_cost = (self.first * self.second) + (other.first * other.second)

        # Новое количество первого товара
        new_quantity = int(total_cost / self.first)

        # Создание нового объекта с вычисленным количеством
        return Pair(self.first, new_quantity)

    # Перегрузка оператора умножения
    def __mul__(self, number):
        """
        При умножении товара на число умножается только его количество.
        """
        if not isinstance(number, (int, float)) or number <= 0:
            raise ValueError("Умножение товара возможно только на положительное число!")
        return Pair(self.first, self.second * number)

    # Перегрузка оператора деления (деление на число)
    def __truediv__(self, number):
        """
        При делении товара на число, его количество уменьшается в некоторое количество раз.
        """
        if not isinstance(number, (int, float)) or number <= 0:
            raise ValueError("Деление возможно только на положительное число!")
        return Pair(round(self.first), round(self.second / number))

    # Перегрузка операторов сравнения
    def __eq__(self, other):
        if not isinstance(other, Pair):
            return False
        return self.cost() == other.cost()

    def __lt__(self, other):
        if not isinstance(other, Pair):
            raise TypeError("Сравнение возможно только между товарами!")
        return self.cost() < other.cost()

    def __le__(self, other):
        if not isinstance(other, Pair):
            raise TypeError("Сравнение возможно только между товарами!")
        return self.cost() <= other.cost()

    # Перегрузка оператора удаления
    def __del__(self):
        """
        Помимо удаления теперь и выводится информация об удаленном товаре.
        """
        print(f"Объект с ценой {self.first} и количеством {self.second} удалён")


# Функция для создания объекта Pair
def make_pair(first, second):
    try:
        return Pair(first, second)
    except ValueError as e:
        print(f"Ошибка создания объекта: {e}")
        return None


# Пример использования
if __name__ == "__main__":
    # Создание двух объектов Pair
    print("Создание двух объектов Pair: ")
    pair1 = make_pair(20.0, 3)  # Цена: 20.0, Количество: 3
    pair2 = make_pair(15.0, 2)  # Цена: 15.0, Количество: 2

    if pair1 and pair2:
        print("\nДанные о первом товаре: ")
        pair1.display()
        print("Данные о втором товаре: ")
        pair2.display()

        # Сложение объектов
        print("\nТовар со средними характеристиками будет следующим: ")
        sum_pair = pair1 + pair2
        sum_pair.display()

        # Вычитание объектов
        print("\nВот что будет с первым товаром, если потратить все деньги со вторго товара на первый товар:")
        sub_pair = pair1 - pair2
        sub_pair.display()

        # Умножение на число
        print("\nВот что будет, есть первого товара будет в 2 раза больше по количеству: ")
        mul_pair = pair1 * 2
        mul_pair.display()

        # Деление на число
        print("\nВот что будет, есть первого товара будет в 2 раза меньше по количеству: ")
        div_pair = pair1 / 2
        div_pair.display()

        # Сравнение объектов
        print("\nСравнение товаров:")
        if pair1 == pair2:
            print("\nОбщая стоимость первого товара совпадает с общей стоимостью второго товара.\n")
        elif pair1 < pair2:
            print("\nОбщая стоимость первого товара меньще общей стоимость второго товара.\n")
        else:
            print("\nОбщая стоимость первого товара больше общей стоимость второго товара.\n")
