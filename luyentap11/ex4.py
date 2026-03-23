def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

lst = [1, 5, 8, 12, 7]
lst.append(int(input("Thêm số: ")))
k = int(input("Nhập k: "))
print(f"Số lần {k} xuất hiện: {lst.count(k)}")
print(f"Tổng số nguyên tố: {sum(x for x in lst if is_prime(x))}")
lst.sort()
print(f"Sắp xếp: {lst}")
lst.clear()
