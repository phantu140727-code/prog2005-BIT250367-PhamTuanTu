import matplotlib.pyplot as plt

# Dữ liệu
labels = ['Xuất sắc', 'Giỏi', 'Trung bình', 'Yêu', 'Kém']
values = [6, 10, 12, 4, 1]

# Vẽ biểu đồ
plt.figure(figsize=(8, 5))
plt.bar(labels, values, color='skyblue')

# Thêm tiêu đề và nhãn
plt.title('Kết quả học tập của lớp')
plt.xlabel('Xếp loại học lực')
plt.ylabel('Số lượng học sinh')

plt.show()
