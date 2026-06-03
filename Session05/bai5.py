while True:
    print("\n===== MENU =====")
    print("1. Nhập dữ liệu và xem báo cáo")
    print("2. Hướng dẫn sử dụng")
    print("3. Thoát chương trình")

    choice = input("Chọn chức năng: ")

    if choice == "1":

        so_chi_nhanh = int(input("Nhập số lượng chi nhánh: "))

        max_hoc_vien = -1
        chi_nhanh_max = 0

        for cn in range(1, so_chi_nhanh + 1):

            print(f"\n--- Chi nhánh {cn} ---")

            so_lop = int(input("Nhập số lớp học: "))

            tong_hoc_vien = 0
            lop_duoi_10 = []

            for lop in range(1, so_lop + 1):

                while True:
                    hoc_vien = int(
                        input(f"Nhập số học viên lớp {lop}: ")
                    )

                    if hoc_vien < 0:
                        print("Lỗi: Số học viên không được âm!")
                    else:
                        break

                tong_hoc_vien += hoc_vien

                if hoc_vien < 10:
                    lop_duoi_10.append(lop)

            print(f"Tổng số học viên: {tong_hoc_vien}")

            if tong_hoc_vien > max_hoc_vien:
                max_hoc_vien = tong_hoc_vien
                chi_nhanh_max = cn

            if len(lop_duoi_10) > 0:
                print("Các lớp dưới 10 học viên:")
                for lop in lop_duoi_10:
                    print(f"- Lớp {lop}")
            else:
                print("Không có lớp nào dưới 10 học viên")

        print("\n===== THỐNG KÊ TOÀN HỆ THỐNG =====")
        print(
            f"Chi nhánh có nhiều học viên nhất: "
            f"Chi nhánh {chi_nhanh_max}"
        )
        print(
            f"Tổng số học viên của chi nhánh này: "
            f"{max_hoc_vien}"
        )

    elif choice == "2":

        print("\n===== HƯỚNG DẪN =====")
        print("- Nhập số lượng chi nhánh")
        print("- Nhập số lớp của từng chi nhánh")
        print("- Nhập số học viên của từng lớp")
        print("- Hệ thống tự động thống kê")
        print("- Số học viên không được âm")

    elif choice == "3":

        print("Thoát chương trình")
        break

    else:

        print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 3.")
        