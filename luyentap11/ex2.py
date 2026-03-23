def binary_search_string(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        # Kiểm tra nếu tìm thấy chính xác chuỗi
        if arr[mid] == target:
            return mid
        
        if len(target) > len(arr[mid]):
            high = mid - 1
        else:
            low = mid + 1      
    return -1
print("\n--- Tìm kiếm nhị phân ---")
list_to_search = ["Chuỗi rất dài", "Chuỗi dài", "Chuỗi vừa", "Ngắn", "Ít"] 
print(f"Danh sách hiện tại: {list_to_search}")

val = input("Nhập chuỗi cần tìm kiếm: ")
index = binary_search_string(list_to_search, val)

if index != -1:
    print(f"Tìm thấy chuỗi '{val}' tại vị trí index: {index}")
else:
    print(f"Không tìm thấy chuỗi '{val}' trong danh sách.")
