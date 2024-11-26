class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        self.products = [p for p in self.products if p.name != name]

    def total_value(self):
        return sum(p.price * p.quantity for p in self.products)
    
inventory = Inventory()
inventory.add_product(Product("Apple", 0.5, 100))
inventory.add_product(Product("Banana", 0.3, 150))

print("Total Inventory Value: $", inventory.total_value())  





