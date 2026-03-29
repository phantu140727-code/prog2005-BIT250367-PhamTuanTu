class Hoa:
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau

    def __str__(self):
        return f"Hoa: {self.ten}, Mau: {self.mau}"

# Test
h = Hoa("Lan", "Trang")
print(h)
