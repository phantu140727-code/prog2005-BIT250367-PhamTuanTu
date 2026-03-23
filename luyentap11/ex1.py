def insertion_sort_strings(arr):
    n = len(arr)
    print(f"\nTrạng thái ban đầu: {arr}")
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and len(key) > len(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Bước {i}: {arr}")
    return arr

strings = []
for i in range(5):
    s = input(f"Nhập chuỗi thứ {i + 1}: ")
    strings.append(s)

sorted_list = insertion_sort_strings(strings)

print("-" * 30)
print(f"Danh sách cuối cùng: {sorted_list}")
