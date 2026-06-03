name = str(input("Nhập họ và tên bệnh nhân: "))
age = int(input("Nhập tuổi của bệnh nhân: "))

if name == "" or age <= 0 or age >= 150:
    print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")
else:
    if age < 6:
        print("ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám nhi")
    elif age >= 80:
        print("ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, Chuyển thẳng phòng khám Lão khoa")
    else:
        print("KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ đến lượt khám")