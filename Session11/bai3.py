product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]
while True:
    print("===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")
    
    choice = int(input("Mời nhập lựa chọn: "))
    
    if choice == 1:
        print("Danh sách sản phẩm hiện tại:")
        for i, j in enumerate(product_list, start=1):
            print(
                f"{i} "
                f"Mã SP: {j['product_id']} |"
                f"Tên: {j['product_name']} |"
                f"Giá: {j['price']} |"
                f"Số lượng: {j['quantity']}"
            )
    elif choice == 2:
        print("-- Thêm sản phẩm mới --")
        product_id = input("Nhập mã sản phẩm: ").strip().upper()
        for i in product_list:
            if product_id == i['product_id']:
                print("Sản phẩm đã tồn tại")
                break
        product_name = input("Nhập tên sản phẩm: ")
        price = float(input("Nhập giá sản phẩm: "))
        if price <= 0:
            print("Giá sản phẩm ko hợp lệ")
            break
        quantity = int(input("Nhập số lượng sản phẩm: "))
        if quantity <= 0:
            print("Số lượng sản phẩm không hợp lệ.")
                
        product_list.append({
            "product_id": product_id,
            "product_name": product_name,
            "price": price,
            "quantity": quantity
        })
        print("Thêm sản phẩm thành công!")
    elif choice == 3:
        print("-- Cập nhật sản phẩm --")
        search = input("Nhập mã sản phẩm cần chỉnh sửa: ").strip().upper()
        for i in product_list:
            if search != i['product_id']:
                print("Mã sản phẩm không tồn tại.")
                break
            else:
                i["product_name"] = input("Nhập tên sản phẩm: ")
                i["price"] = float(input("Nhập giá sản phẩm: "))
                i["quantity"] = int(input("Nhập số lượng sản phẩm: "))
                print("Cập nhật sản phẩm thành công!")
                break
    elif choice == 4:
        print("-- Xoá sản phẩm --")
        id = input("Nhập mã sản phẩm: ").strip().upper()
        for i in product_list:
            if id != i['product_id']:
                print("Mã sản phẩm không tồn tại.")
                break
            else:
                product_list.remove(i)
                print("Xoá sản phẩm thành công!")
                break
    elif choice == 5:
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ")
        