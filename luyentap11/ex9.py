def get_matrix(r, c):
    matrix = []
    for i in range(r):
        row = input(f"Nhập hàng {i+1} (cách nhau khoảng trắng): ").split()
        if not row: raise ValueError("Giá trị trống!")
        matrix.append([int(x) for x in row])
    return matrix

try:
    r, c = 2, 2
    m1 = get_matrix(r, c)
    m2 = get_matrix(r, c)
    res = [[m1[i][j] + m2[i][j] for j in range(c)] for i in range(r)]
    print(f"Kết quả: {res}")
except ValueError as e:
    print(f"Lỗi: {e}")
