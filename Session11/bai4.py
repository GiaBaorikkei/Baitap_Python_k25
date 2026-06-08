product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]

while True:
    print("\n===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Nhập thêm hàng vào kho")
    print("4. Xem báo cáo doanh thu")
    print("5. Thoát chương trình")

    choice = int(input("Mời nhập lựa chọn: "))

    if choice == 1:
        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("\nDanh sách sản phẩm hiện tại:")

            for index, product in enumerate(product_list, start=1):

                if product["quantity"] == 0:
                    status = "Hết hàng"
                elif product["quantity"] <= 5:
                    status = "Sắp hết hàng"
                else:
                    status = "Còn hàng"

                print(
                    f"{index}. "
                    f"Mã SP: {product['product_id']} | "
                    f"Tên: {product['product_name']} | "
                    f"Giá: {product['price']} | "
                    f"Tồn kho: {product['quantity']} | "
                    f"Đã bán: {product['sold']} | "
                    f"Trạng thái: {status}"
                )

    elif choice == 2:
        print("\n--- BÁN SẢN PHẨM ---")

        product_id = input(
            "Nhập mã sản phẩm khách muốn mua: "
        ).strip().upper()

        found = False

        for product in product_list:
            if product["product_id"] == product_id:
                found = True

                try:
                    buy_quantity = int(
                        input("Nhập số lượng khách mua: ")
                    )
                except ValueError:
                    print("Số lượng mua không hợp lệ.")
                    break

                if buy_quantity <= 0:
                    print("Số lượng mua không hợp lệ.")
                    break

                if buy_quantity > product["quantity"]:
                    print("Số lượng trong kho không đủ để bán.")
                    break

                product["quantity"] -= buy_quantity
                product["sold"] += buy_quantity

                total_money = buy_quantity * product["price"]

                print("Bán hàng thành công!")
                print(
                    f"Khách cần thanh toán: {total_money}"
                )

                break

        if not found:
            print("Không tìm thấy sản phẩm cần bán.")

    elif choice == 3:
        print("\n--- NHẬP THÊM HÀNG ---")

        product_id = input(
            "Nhập mã sản phẩm cần nhập thêm: "
        ).strip().upper()

        found = False

        for product in product_list:
            if product["product_id"] == product_id:
                found = True

                try:
                    import_quantity = int(
                        input("Nhập số lượng nhập thêm: ")
                    )
                except ValueError:
                    print("Số lượng nhập kho không hợp lệ.")
                    break

                if import_quantity <= 0:
                    print("Số lượng nhập kho không hợp lệ.")
                    break

                product["quantity"] += import_quantity

                print("Nhập kho thành công!")
                print(
                    f"Tồn kho hiện tại: {product['quantity']}"
                )

                break

        if not found:
            print("Không tìm thấy sản phẩm cần nhập kho.")

    elif choice == 4:
        print(
            "\n===== BÁO CÁO DOANH THU CỬA HÀNG YODY ====="
        )

        total_revenue = 0
        max_sold = 0
        best_seller = ""

        for index, product in enumerate(product_list, start=1):

            revenue = (
                product["price"] * product["sold"]
            )

            total_revenue += revenue

            print(
                f"{index}. "
                f"{product['product_name']} | "
                f"Đã bán: {product['sold']} | "
                f"Doanh thu: {revenue}"
            )

            if product["sold"] > max_sold:
                max_sold = product["sold"]
                best_seller = product["product_name"]

        if total_revenue == 0:
            print("Chưa có doanh thu phát sinh.")
        else:
            print(
                f"\nTổng doanh thu: {total_revenue}"
            )
            print(
                f"Sản phẩm bán chạy nhất: {best_seller}"
            )

    elif choice == 5:
        print("Thoát chương trình.")
        break

    else:
        print(
            "Lựa chọn không hợp lệ, vui lòng nhập lại!"
        )
