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

    @classmethod
    def new_product(cls, product_data: dict):
        """Создает новый продукт из словаря"""
        return cls(
            name=product_data["name"],
            price=product_data["price"],
            description=product_data["description"],
            quantity=product_data["quantity"]
        )

    @classmethod
    def new_product_with_check(cls, product_data: dict, existing_products=None):
        """Создает продукт с проверкой на дубликаты"""
        if existing_products:
            for product in existing_products:
                if product.name == product_data["name"]:
                    # Нашли дубликат
                    product.quantity += product_data["quantity"]
                    if product_data["price"] > product.price:
                        product.price = product_data["price"]
                    return product

        # Если дубликатов нет
        return cls.new_product(product_data)

    def __str__(self):
        return f"{self.name}, {self.price} руб. (остаток: {self.quantity})"
