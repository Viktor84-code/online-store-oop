class Product:
    def __init__(self, name, price, description, quantity):
        self.name = name
        self._price = price  # Приватная цена (подготовка к заданию 4)
        self.description = description
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для цены"""
        return self._price

    @price.setter
    def price(self, value):
        """Сеттер с валидацией"""
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self._price = value

    def __str__(self):
        return f"{self.name}, {self.price} руб. (остаток: {self.quantity})"
