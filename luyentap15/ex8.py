class Product:
    def __init__(self, price):
        self._price = 0
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Lỗi: Giá không được nhỏ hơn 0!")
        else:
            self._price = value

p = Product(100)
p.price = -50
print(f"Giá hiện tại: {p.price}")
