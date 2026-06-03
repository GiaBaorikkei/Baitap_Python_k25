raw_input = "   nGuyen vaN aN  ;  2004   "

while True:

    print("\n===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa Họ tên và tính Tuổi")
    print("3. Tạo Mã ID và Email tự động")
    print("4. Thoát chương trình")
    print("=====================================")

    choice = input("Nhập lựa chọn của bạn (1-4): ")

    if choice == "1":
        print("\nDữ liệu gốc:")
        print(raw_input)

    elif choice == "2":

        data = raw_input.split(";")

        ho_ten = data[0].strip().title()
        nam_sinh = data[1].strip()

        tuoi = 2026 - int(nam_sinh)

        print("\n===== THÔNG TIN THÀNH VIÊN =====")
        print(f"Họ tên   : {ho_ten}")
        print(f"Năm sinh : {nam_sinh}")
        print(f"Tuổi     : {tuoi}")

    elif choice == "3":

        data = raw_input.split(";")

        ho_ten = data[0].strip().title()
        nam_sinh = data[1].strip()

        parts = ho_ten.split()

        ho = parts[0]
        ten = parts[-1]

        if len(parts) >= 3:
            ten_dem = parts[1]
        else:
            ten_dem = ""

        email = (
            ho[0].lower()
            + ten_dem[0].lower()
            + ten.lower()
            + "@company.com"
        )

        member_id = ten.upper() + nam_sinh[-2:]

        print("\n+------------------------------+")
        print("      THẺ THÀNH VIÊN MỚI         ")
        print("+------------------------------+")
        print(f"| Họ tên : {ho_ten:<18}|")
        print(f"| ID     : {member_id:<18}|")
        print(f"| Email  : {email:<18}|")
        print("+------------------------------+")

    elif choice == "4":
        print("Tạm biệt! Hẹn gặp lại.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")