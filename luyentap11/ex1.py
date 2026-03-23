def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and len(key) > len(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Bước {i}: {arr}")
    return arr

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x: return mid
        elif len(arr[mid]) < len(x): high = mid - 1
        else: low = mid + 1
    return -1

strings = [input(f"Nhập chuỗi {i+1}: ") for i in range(5)]
sorted_list = insertion_sort(strings)
search_val = input("Nhập chuỗi cần tìm: ")
pos = binary_search(sorted_list, search_val)
print(f"Vị trí: {pos}" if pos != -1 else "Không tìm thấy
