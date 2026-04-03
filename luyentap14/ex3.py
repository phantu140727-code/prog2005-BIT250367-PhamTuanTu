def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

nums = list(map(int, input("Nhập mảng: ").split()))
odds = [x for x in nums if x % 2 != 0]
primes = [x for x in nums if is_prime(x)]

print(f"Số lẻ: {odds} - Số lượng: {len(odds)}")
print(f"Số nguyên tố: {primes}")
