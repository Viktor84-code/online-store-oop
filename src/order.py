"""Модуль для работы с заказами."""

from src.base_collection import BaseCollection


class Order(BaseCollection):
    """Класс для заказа (один товар)."""

    def __init__(self, name, description, product, quantity):
        """
        Инициализация заказа.

        :param name: Название заказа
        :param description: описание заказа
        :param product: товар (Product или его наследник)
        :param quantity: количество
        """
        super().__init__(name, description)
        self.name = name
        self.description = description
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __str__(self):
        """Строковое представление заказа."""
        return (
            f"Заказ: {self.name}\n"
            f"Товар: {self.product.name}\n"
            f"Количество: {self.quantity}\n"
            f"Сумма: {self.total_price} руб."
        )
