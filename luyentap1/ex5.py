import random

m = int(input("Nhập M: "))
n = int(input("Nhập N: "))
matrix = [[random.randint(1, 100) for _ in range(n)] for _ in range(m)]

print("Ma trận:")
for r in matrix: print(r)

r_idx = int(input("Chọn hàng: "))
print(f"Hàng {r_idx}:", matrix[r_idx] if 0 <= r_idx < m else "Lỗi")

c_idx = int(input("Chọn cột: "))
print(f"Cột {c_idx}:", [matrix[i][c_idx] for i in range(m)] if 0 <= c_idx < n else "Lỗi")

print("Max:", max(max(row) for row in matrix))
