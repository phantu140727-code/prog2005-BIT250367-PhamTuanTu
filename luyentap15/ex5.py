def count_vowels(s):
    vowels = "aeiouAEOUI"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

chuoi = input("Nhập chuỗi: ")
print(f"Số lượng nguyên âm: {count_vowels(chuoi)}")
