nums = list(map(int, input("Nhập dãy số: ").split()))
evens = [x for x in nums if x % 2 == 0]
print(f"Số chẵn: {evens}")
print(f"Tổng: {sum(evens)}")
