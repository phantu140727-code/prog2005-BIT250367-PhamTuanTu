m1 = float(input("Nhập điểm môn 1: "))
m2 = float(input("Nhập điểm môn 2: "))
m3 = float(input("Nhập điểm môn 3: "))
dtb = (m1 + m2 + m3) / 3
print(f"Điểm trung bình: {dtb:.2f}")
if dtb >= 8:
    print("Xếp loại: Giỏi")
elif dtb >= 6.5:
    print("Xếp loại: Khá")
elif dtb >= 5.0:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")
