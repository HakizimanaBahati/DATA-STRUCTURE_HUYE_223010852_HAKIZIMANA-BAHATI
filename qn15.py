from collections import deque
class Inventory:
    def __init__(self):
        self.available = []  
        self.recently_added = []       
        self.shipping = [] 
        

    def add_product(self):
        product = input("Please enter the product name:")
        self.available.append(product)
        self.recently_added.append(product)  
        print(f"Product added: {product}")

    def ship_order(self):
        if self.shipping:
            order = self.shipping.pop(0)
            print(f"Shipping order: {order}")
        else:
            print("No orders to ship.")

    def create(self):
        product = input("According to the available prodect please enter the product you want to arder")
        if product in self.available:
            for product in self.available:
                self.shipping.append(product)

                print(f"This : {product} is in proggress to be ordered")
        else:
            print(f"Product not available: {product}")

    def view(self):
        print("Available products:")
        for product in self.available:
            print(f"- {product}")

    def view_recently_added(self):
        print("Recently added products :")
        for product in self.available:
            product = self.recently_added.pop()
            print(product)
    def view_shipping(self):
        print("Current shipping product:")
        for order in self.shipping:
            print(order)
if __name__ =="__main__":
    investory = Inventory()
    for i in range(0,3):
        investory.add_product()
    investory.view()
    investory.view_recently_added()
    investory.create()
    investory.ship_order()
    investory.view_shipping()