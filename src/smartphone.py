"""Модуль для работы со смартфонами."""


from src.product import Product


class Smartphone(Product):
    """Класс для смартфонов, наследник Product."""

    def __init__(self, name, price, description, quantity, efficiency, model, memory, color):
        """Инициализация смартфона с дополнительными атрибутами."""
        #               name, price, description, quantity — порядок как в Product!
        super().__init__(name, price, description, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
