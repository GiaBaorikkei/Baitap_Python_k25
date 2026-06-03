so_phieu = int(input("Nhập số lượng phiếu đăng ký: "))

if so_phieu <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ")
else:
    for i in range(1, so_phieu + 1):
        print(f"\nNhập phiếu đăng ký thứ {i}:")
        registration = input()

        data = registration.split("|")

        if len(data) != 4:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
            continue

        student_name = data[0].strip().title()
        course_name = data[1].strip().title()
        student_code = data[2].strip().upper()
        email = data[3].strip().lower()

        if "@" not in email:
            print("Email không hợp lệ. Bỏ qua phiếu này")
            continue

        if len(student_code) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            continue

        confirmation_code = (
            student_code + "_" +
            course_name.upper().replace(" ", "-")
        )

        print("\n===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
        print("Học viên:", student_name)
        print("Khóa học:", course_name)
        print("Mã học viên:", student_code)
        print("Email:", email)
        print("Mã xác nhận:", confirmation_code)