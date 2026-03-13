def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

s = "5; 7; 8; -2; 8; 11; 13; 9; 10"
nums = [int(x.strip()) for x in s.split(';')]

for n in nums: print(n)
print(f"Số chẵn: {len([x for x in nums if x % 2 == 0])}")
print(f"Số âm: {len([x for x in nums if x < 0])}")
print(f"Số nguyên tố: {len([x for x in nums if is_prime(x)])}")
print(f"Trung bình: {sum(nums)/len(nums)}")
