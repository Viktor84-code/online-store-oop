from src.product import Product

class LawnGrass(Product):
    def __init__(self, name, price, description, quantity, country, germination_period, color):
        #               name, price, description, quantity — порядок как в Product!
        super().__init__(name, price, description, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


