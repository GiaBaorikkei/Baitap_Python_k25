raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "


def chuan_hoa_du_lieu():
    employees = []

    danh_sach = raw_data.split("|")

    for nv in danh_sach:
        info = nv.split(";")

        emp_id = info[0].strip().upper()
        name = info[1].strip().title()
        phone = info[2].strip().replace("-", "")
        department = info[3].strip().upper()

        if phone.isdigit():
            phone = "******" + phone[-4:]
        else:
            phone = "Invalid Format"

        employees.append({
            "id": emp_id,
            "name": name,
            "phone": phone,
            "department": department
        })

    return employees


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")

    choice = input("Chọn chức năng: ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    choice = int(choice)

    if choice == 1:
        print("\nDỮ LIỆU GỐC:")
        print(raw_data)

    elif choice == 2:
        employees = chuan_hoa_du_lieu()

        print("\nBÁO CÁO NHÂN SỰ")
        print("-" * 70)
        print(f"{'ID':<12}{'HỌ TÊN':<25}{'ĐIỆN THOẠI':<20}{'PHÒNG BAN':<10}")
        print("-" * 70)

        for emp in employees:
            print(
                f"{emp['id']:<12}"
                f"{emp['name']:<25}"
                f"{emp['phone']:<20}"
                f"{emp['department']:<10}"
            )

    elif choice == 3:
        employees = chuan_hoa_du_lieu()

        search_id = input("Nhập mã nhân viên cần tìm: ")
        search_id = search_id.strip().upper()

        found = False

        for emp in employees:
            if emp["id"] == search_id:
                print("\nTHÔNG TIN NHÂN VIÊN")
                print(f"ID: {emp['id']}")
                print(f"Họ tên: {emp['name']}")
                print(f"Điện thoại: {emp['phone']}")
                print(f"Phòng ban: {emp['department']}")
                found = True
                break

        if not found:
            print("Không tìm thấy nhân viên")

    elif choice == 4:
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")