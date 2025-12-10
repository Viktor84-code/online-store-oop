class Category:
    """Класс для описания категории товаров."""

    category_count = 0  # атрибут класса: количество категорий
    product_count = 0  # атрибут класса: количество товаров

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products  # список товаров

        # Увеличиваем счётчики при создании категории
        Category.category_count += 1
        Category.product_count += len(products)
