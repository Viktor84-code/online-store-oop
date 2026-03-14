"""Модуль для работы с газонной травой."""

from src.product import Product


class LawnGrass(Product):
    """Класс для газонной травы, наследник Product."""

    def __init__(
        self, name, price, description, quantity, country, germination_period, color
    ):
        """Инициализация газонной травы с дополнительными атрибутами."""
        super().__init__(name, price, description, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
