product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5,
        "returned": 1,
        "discount": 0
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3,
        "returned": 0,
        "discount": 10
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7,
        "returned": 1,
        "discount": 15
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ GIAO DỊCH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Xử lý đổi trả sản phẩm")
    print("4. Áp dụng giảm giá cho sản phẩm")
    print("5. Nhập thêm hàng vào kho cửa hàng")
    print("6. Thoát chương trình")

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
                    f"Đổi trả: {product['returned']} | "
                    f"Giảm giá: {product['discount']}% | "
                    f"Trạng thái: {status}"
                )
                
    elif choice == 2:
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
                    print("Số lượng mua không hợp lệ")
                    break

                if buy_quantity <= 0:
                    print("Số lượng mua không hợp lệ")
                    break

                if buy_quantity > product["quantity"]:
                    print("Số lượng trong kho không đủ để bán")
                    break

                final_price = (
                    product["price"]
                    * (100 - product["discount"])
                    / 100
                )

                total_money = final_price * buy_quantity

                product["quantity"] -= buy_quantity
                product["sold"] += buy_quantity

                print("Bán hàng thành công!")
                print(f"Tổng tiền khách cần thanh toán: {total_money:.0f}")

                break

        if not found:
            print("Không tìm thấy sản phẩm cần bán")

    elif choice == 3:
        product_id = input(
            "Nhập mã sản phẩm khách muốn đổi/trả: "
        ).strip().upper()

        found = False

        for product in product_list:
            if product["product_id"] == product_id:
                found = True

                try:
                    return_quantity = int(
                        input("Nhập số lượng đổi/trả: ")
                    )
                except ValueError:
                    print("Số lượng đổi/trả không hợp lệ")
                    break

                if return_quantity <= 0:
                    print("Số lượng đổi/trả không hợp lệ")
                    break

                if return_quantity > product["sold"]:
                    print(
                        "Số lượng đổi/trả không được vượt quá số lượng đã bán"
                    )
                    break

                refund_price = (
                    product["price"]
                    * (100 - product["discount"])
                    / 100
                )

                refund_money = refund_price * return_quantity

                product["sold"] -= return_quantity
                product["quantity"] += return_quantity
                product["returned"] += return_quantity

                print("Xử lý đổi trả thành công!")
                print(f"Số tiền hoàn lại: {refund_money:.0f}")

                break

        if not found:
            print("Không tìm thấy sản phẩm cần đổi trả")

    elif choice == 4:
        product_id = input(
            "Nhập mã sản phẩm cần áp dụng giảm giá: "
        ).strip().upper()

        found = False

        for product in product_list:
            if product["product_id"] == product_id:
                found = True

                try:
                    discount = int(
                        input("Nhập phần trăm giảm giá: ")
                    )
                except ValueError:
                    print("Phần trăm giảm giá không hợp lệ")
                    break

                if discount < 0 or discount > 70:
                    print("Phần trăm giảm giá không hợp lệ")
                    break

                product["discount"] = discount

                print(
                    f"Cập nhật giảm giá thành công: {discount}%"
                )

                break

        if not found:
            print("Không tìm thấy sản phẩm")

    elif choice == 5:
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
                    print("Số lượng nhập kho không hợp lệ")
                    break

                if import_quantity <= 0:
                    print("Số lượng nhập kho không hợp lệ")
                    break

                product["quantity"] += import_quantity

                print("Nhập kho thành công!")
                print(
                    f"Tồn kho hiện tại: {product['quantity']}"
                )

                break

        if not found:
            print("Không tìm thấy sản phẩm cần nhập kho")

    elif choice == 6:
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")