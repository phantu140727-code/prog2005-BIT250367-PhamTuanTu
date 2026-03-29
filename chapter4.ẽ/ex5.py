class Product:
    def __init__(self, price):
        self._price = price if price > 0 else 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value

    def __str__(self):
        return f"Price: {self._price}"

# Test
p = Product(100)
p.price = 150
print(p)
