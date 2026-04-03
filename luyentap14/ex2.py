names = [input(f"Nhập tên {i+1}: ") for i in range(5)]
print("Ban đầu:", names)
if len(names) >= 2:
    names.pop(1)
print("Sau khi xóa:", names)
