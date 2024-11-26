class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.category})"

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)
        print(f"{product.name} has been added to the cart.")

    def remove_item(self, product_name):
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                print(f"{product_name} has been removed from the cart.")
                return
        print(f"{product_name} not found in the cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for item in self.items:
                print(f" - {item}")
    
    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

if __name__ == "__main__":
    product1 = Product("Laptop", 999.99, "Electronics")
    product2 = Product("Headphones", 199.99, "Electronics")
    product3 = Product("Coffee Mug", 14.99, "Kitchen")

    cart = Cart()

    cart.add_item(product1)
    cart.add_item(product2)
    cart.add_item(product3)

    cart.view_cart()

    cart.remove_item("Headphones")

    cart.view_cart()

    total = cart.calculate_total()
    print(f"Total price: ${total:.2f}")
