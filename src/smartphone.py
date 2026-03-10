from src.product import Product

class Smartphone(Product):
    def __init__(self, name, price, description, quantity, efficiency, model, memory, color):
        #               name, price, description, quantity — порядок как в Product!
        super().__init__(name, price, description, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

