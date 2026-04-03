class Book:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    @property
    def name(self): return self._name
    @name.setter
    def name(self, v): self._name = v
    @property
    def price(self): return self._price
    @price.setter
    def price(self, v): self._price = v
b = Book("Python Basics", 50000)
print(b.price)
