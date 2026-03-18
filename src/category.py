"""Модуль для работы с категориями товаров."""

from src.base_collection import BaseCollection
from src.product import Product


class Category(BaseCollection):
    """Класс для описания категории товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Инициализация категории с названием, описанием и списком товаров."""
        super().__init__(name, description)
        self.name = name  # ← добавить!
        self.description = description
        self._products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """Добавляет продукт в категорию (только Product и его наследников)."""
        #  можно добавить валидацию
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты Product или его наследников"
            )
        self._products.append(product)
        Category.product_count += 1

    #  property для доступа к данным
    @property
    def products(self):
        """Возвращает строку со всеми продуктами по шаблону."""
        result = ""
        for product in self._products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    #  свойство для количества товаров (без доступа к сырым данным)
    @property
    def products_count(self):
        """Количество товаров в категории."""
        return len(self._products)

    def __str__(self):
        """Название категории, количество продуктов: X шт."""
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def middle_price(self):
        """Средняя цена товаров в категории."""
        try:
            total = sum(product.price for product in self._products)
            return total / len(self._products)
        except ZeroDivisionError:
            return 0
