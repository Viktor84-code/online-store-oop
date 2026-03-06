from src.product import Product


class Category:
    """Класс для описания категории товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self._products = products  # Приватный список (сырые данные)

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """Добавляет продукт в категорию"""
        #  можно добавить валидацию
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product")
        self._products.append(product)
        Category.product_count += 1

    #  property для доступа к данным
    @property
    def products(self):
        """Возвращает строку со всеми продуктами по шаблону"""
        result = ""
        for product in self._products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    #  свойство для количества товаров (без доступа к сырым данным)
    @property
    def products_count(self):
        """Количество товаров в категории"""
        return len(self._products)

    def __str__(self):
        """Название категории, количество продуктов: X шт."""
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

