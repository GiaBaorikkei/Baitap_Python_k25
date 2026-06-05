cart_items = [
         ["P001", "Dien thoai iPhone 15", 1, 25000000],
         ["P002", "Op lung Silicon", 2, 150000]
]
def chuan_hoa_du_lieu():
    order = []
    for item in cart_items:
        id = item[0].strip().upper()
        name = item[1]
        quantity = item[2]
        price = item[3]
        total = quantity * price
        
        order.append({
            "id": id,
            "name": name,
            "quantity": quantity,
            "price": price,
            "total": total
        })
    return order
        
while True:
    print("-- QUẢN LÍ GIỎ HÀNG SHOPPE --")
    print("1. Xem chi tiết giỏ hàng và Tính tổng tiền")
    print("2. Thêm sảm phẩm mới, Cộng dồn số lượng")
    print("3. Cập nhập số lượng của 1 sản phẩm")
    print("4. Xoá sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")
    print("Mời bạn chọn chức năng")
    
    choice = input("Nhập lựa chọn của bạn: ")
    
    if choice == "1":
        order = chuan_hoa_du_lieu()
        if len(cart_items) == 0:
            print("Danh đơn hàng đang trống.")
        else:
            print(f"{'STT':<5}{'Mã SP':<10}{'Tên SP':<25}{'SL':<5}{'Đơn Giá':<15}{'Thành Tiền'}")
            for stt, i in enumerate(order, start=1):
                print(
                    f"{stt:<5}"
                    f"{i['id']:<10}"
                    f"{i['name']:<25}"
                    f"{i['quantity']:<5}"
                    f"{i['price']:<15,.0f}"
                    f"{i['total']:<15,.0f}"
                )
                
    elif choice == "2":
        id = input("Nhập mã sản phẩm: ").strip().upper()
        for item in cart_items:
            if item[0].upper() == id.upper():
                quantity = int(input("Nhập số lượng: "))
                if quantity <= 0:
                    print("Số lượng phải lớn hơn 0")
                    continue
                else:
                    item[2] += quantity
                    print("Đã cộng dồn số lượng!")
                    break
            else:
                name = input("Nhập tên sản phẩm: ")
                quantity = int(input("Nhập số lượng: "))
                price = float(input("Nhập đơn giá: "))   
                cart_items.append([id, name, quantity, price])
                print("Đã thêm sản phẩm mới.")
    elif choice == "3":
        id = input("Nhập mã sản phẩm: ").strip().upper()
        
        for item in cart_items:
            if item[0].upper() != id:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")
                break
            else:
                new_quantity = int(input("Nhập số lượng mới: "))
                if new_quantity <= 0:
                    print("Số lượng phải lớn hơn 0.")
                    continue
                else:
                    item[2] += quantity
                    print("Đã cập nhật số lượng mới!")
    elif choice == "4":
        id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()

        for item in cart_items:
            if item[0].upper() != id:
                print("Không tìm thấy sản phẩm câng xoá")
                break
            else:
                item[0].upper() == id
                cart_items.remove(item)
                print("Xóa thành công.")
    elif choice == "5":
        print("Đã thoát chương trình!")
        break
    else:
        print("Lựa chọn không hợp lệ!")
        
        