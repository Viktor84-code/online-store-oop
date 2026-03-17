"""Абстрактный базовый класс для всех продуктов."""

from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __init__(self, name, price, description, quantity):
        """
        Инициализация продукта.

        :param name: название продукта
        :param price: цена
        :param description: описание
        :param quantity: количество на складе
        """
        pass

    @abstractmethod
    def __str__(self):
        """Возвращает строковое представление продукта."""
        pass

    @abstractmethod
    def __add__(self, other):
        """
        Складывает общую стоимость двух продуктов (цена × количество).

        :param other: другой продукт
        :return: сумма произведений цены на количество
        :raises TypeError: если other не Product или классы разные
        """
        pass

    @property
    @abstractmethod
    def price(self):
        """Геттер для цены."""
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        """Сеттер для цены с валидацией."""
        pass
