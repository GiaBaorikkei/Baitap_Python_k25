branch_names = [
    "Highlands Nhà Thờ",
    "Highlands Bà Triệu",
    "Highlands Nguyễn Du",
    "Highlands Landmark 81",
    "Highlands Trần Hưng Đạo"
]

daily_revenues = [
    15500000,
    28000000,
    9200000,
    45000000,
    11000000
]

target_achieved = [
    True,
    True,
    False,
    True,
    False
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====")
    print("1. Hiển thị báo cáo doanh thu tổng hợp")
    print("2. Thống kê chi nhánh Cao nhất / Thấp nhất")
    print("3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)")
    print("4. Thoát chương trình")
    print("================================================")

    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()

    if choice == "1":
        print("\nBÁO CÁO DOANH THU TỔNG HỢP")
        print("-" * 80)
        print(f"{'STT':<5}{'CHI NHÁNH':<30}{'DOANH THU (VNĐ)':<20}{'TRẠNG THÁI'}")
        print("-" * 80)

        for i in range(len(branch_names)):
            status = "Đạt" if target_achieved[i] else "Không Đạt"

            print(
                f"{i+1:<5}"
                f"{branch_names[i]:<30}"
                f"{daily_revenues[i]:<20,}"
                f"{status}"
            )

        print("-" * 80)
        print(f"Tổng doanh thu: {sum(daily_revenues):,} VNĐ")

    elif choice == "2":
        max_revenue = max(daily_revenues)
        min_revenue = min(daily_revenues)

        max_index = daily_revenues.index(max_revenue)
        min_index = daily_revenues.index(min_revenue)

        print("\nTHỐNG KÊ DOANH THU")
        print(
            f"Chi nhánh doanh thu cao nhất: "
            f"{branch_names[max_index]} "
            f"({max_revenue:,} VNĐ)"
        )

        print(
            f"Chi nhánh doanh thu thấp nhất: "
            f"{branch_names[min_index]} "
            f"({min_revenue:,} VNĐ)"
        )

    elif choice == "3":
        failed_branches = []

        for i in range(len(target_achieved)):
            if target_achieved[i] == False:
                failed_branches.append(branch_names[i])

        print("\nDANH SÁCH CƠ SỞ KHÔNG ĐẠT CHỈ TIÊU")
        print(failed_branches)

    elif choice == "4":
        print("\nHệ thống ghi nhận dữ liệu hoàn tất. Tạm biệt!")
        break

    else:
        print(
            "\n[Lỗi] Lựa chọn không hợp lệ, "
            "vui lòng nhập lại số từ 1 đến 4!"
        )