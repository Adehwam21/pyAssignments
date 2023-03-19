ITEMS = {
    "cabbage" : 6.0,
    "carrots" : 5.5,
    "shampoo" : 25.0,
    "cards" : 4.0,
    "notepad" : 20.0
}

class ShoppingCart:
    def __init__(self) -> None:
        self.items = []
        self.totalPrice = 0.0

    # s = specified item
    def addItem(self, item):
        self.items.append(item)
        

    def removeItem(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed item :{item}")


    def getTotalPrice(self):
        products = [p for p in ITEMS.keys()]
        prices = []
        for i in products:  
            if i in self.items:
                prices.append(ITEMS.get(i))
            else:
                continue
        self.totalPrice = sum(prices)
        return self.totalPrice
    
if __name__ == "__main__":
    cart1 = ShoppingCart()
    cart1.addItem("cabbage")
    cart1.addItem("cards")
    cart1.addItem("shampoo")
    cart1.addItem("carrots")
    print(f"Shopping Cart :{cart1.items}")
    print(f"Price of items in cart GHc {cart1.getTotalPrice()}\n")
    cart1.removeItem("shampoo")
    print(f"\nShopping Cart :{cart1.items}")
    print(f"Price of items in cart GHc {cart1.getTotalPrice()}") 