class Product:
    def __init__(self, name, price, description, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для цены"""
        return self._price

    @price.setter
    def price(self, value):
        """Сеттер с валидацией (без подтверждения)"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self._price = value

    def set_price_with_confirmation(self, value):
        """Установка цены с подтверждением при понижении (для дополнительного задания)"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if value < self._price:
            answer = input(f"Понизить цену с {self._price} до {value}? (y/n): ")
            if answer.lower() == "y":
                self._price = value
                print("Цена успешно изменена")
            else:
                print("Изменение цены отменено")
        else:
            self._price = value

    @classmethod
    def new_product(cls, product_data: dict):
        """Создает новый продукт из словаря"""
        return cls(
            name=product_data["name"],
            price=product_data["price"],
            description=product_data["description"],
            quantity=product_data["quantity"],
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
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только Product с Product")
        if type(self) is not type(other):
            raise TypeError(f"Нельзя складывать {type(self).__name__} с {type(other).__name__}")
        return (self.price * self.quantity) + (other.price * other.quantity)

