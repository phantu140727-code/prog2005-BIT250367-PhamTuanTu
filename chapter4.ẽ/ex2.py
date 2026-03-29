def tinh_trung_binh(d):
    return sum(d.values()) / len(d) if d else 0

# Test
sinh_vien = {"Tu": 8, "Duy": 7, "Thuan": 9}
print(tinh_trung_binh(sinh_vien))
