raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-099 "

def giai_ma_du_lieu():
    products = []

    danh_sach = raw_batch.split(";")

    for item in danh_sach:
        code = item.strip().upper()

        parts = code.split("-")

        if len(parts) != 4:
            continue

        product_type = parts[0]
        country = parts[1]
        year = "20" + parts[2]
        serial = parts[3]

        if serial.isdigit():
            status = "Pass"
            valid = True
        else:
            status = "Lỗi Serial - Reject"
            valid = False

        products.append({
            "code": product_type,
            "country": country,
            "year": year,
            "serial": serial,
            "status": status,
            "valid": valid
        })

    return products


while True:
    print("\n===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====")
    print("1. Hiển thị chuỗi mã vạch gốc")
    print("2. Giải mã, làm sạch và in báo cáo kiểm kê")
    print("3. Tra cứu nhanh theo đuôi Serial")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()

    if not choice.isdigit():
        print("Chức năng không tồn tại, vui lòng nhập số từ 1-4!")
        continue

    choice = int(choice)

    if choice == 1:
        print("\nDỮ LIỆU GỐC:")
        print(raw_batch)

    elif choice == 2:
        products = giai_ma_du_lieu()

        print("\n===== BÁO CÁO KIỂM KÊ =====")
        print("-" * 80)
        print(
            f"{'MÃ SP':<12}"
            f"{'XUẤT XỨ':<12}"
            f"{'NĂM SX':<12}"
            f"{'SERIAL':<12}"
            f"{'TRẠNG THÁI'}"
        )
        print("-" * 80)

        valid_count = 0

        for p in products:
            print(
                f"{p['code']:<12}"
                f"{p['country']:<12}"
                f"{p['year']:<12}"
                f"{p['serial']:<12}"
                f"{p['status']}"
            )

            if p["valid"]:
                valid_count += 1

        print("-" * 80)
        print(
            f"Đã giải mã thành công {valid_count} sản phẩm hợp lệ / "
            f"Tổng số {len(products)} sản phẩm."
        )

    elif choice == 3:
        products = giai_ma_du_lieu()

        serial_search = input(
            "Nhập 2 số cuối của Serial cần tìm: "
        ).strip()

        found = False

        for p in products:
            if p["serial"][-2:] == serial_search:
                print("\nTHÔNG TIN SẢN PHẨM")
                print("Mã SP:", p["code"])
                print("Xuất xứ:", p["country"])
                print("Năm SX:", p["year"])
                print("Serial:", p["serial"])
                print("Trạng thái:", p["status"])
                found = True

        if not found:
            print("Không tìm thấy sản phẩm phù hợp")

    elif choice == 4:
        print("Đóng ca kiểm kho. Chào tạo biệt!")
        break

    else:
        print("Chức năng không tồn tại, vui lòng nhập số từ 1-4!")