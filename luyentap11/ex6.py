data = {}
for _ in range(3):
    name = input("Tên: ")
    age = int(input("Tuổi: "))
    data[name] = age
print(f"Tuổi TB: {sum(data.values())/len(data)}")
