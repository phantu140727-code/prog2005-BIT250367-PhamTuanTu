students = {"An": 8.5, "Bình": 7.0, "Chi": 9.0}

def tinh_trung_binh(danh_sach):
    if not danh_sach:
        return 0
    tong_diem = sum(danh_sach.values())
    return tong_diem / len(danh_sach)

print(f"Điểm trung bình lớp: {tinh_trung_binh(students):.2f}")
