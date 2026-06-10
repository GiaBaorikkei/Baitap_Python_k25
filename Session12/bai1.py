cart_items = [
         {
         	"id": "P001", 
         	"name": "Dien thoai iPhone 15",
         	"number": 1,
         	"price": 25000000
         },
         {
         	"id": "P002",
         	"name": "Op lung Silicon", 
         	"number": 2, 
         	"price": 150000
         }
]
while True:
    print("== SHOPPE CART MANAGEMENT SYSTEM ==")
    print("1. Xem chi tiết giỏ hàng và tính tổng số tiền")
    print("2. Thêm sản phẩm mới / cộng dồn số lượng")
    print("3. Cập nhật số lượng sản phẩm")
    print("4. Xoá sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")
    
    choice = int(input("Nhập lựa chọn của bạn: "))
    
    if choice == 1:
        total_number = 0
        total_price = 0
        print("-- Chi tiết giỏ hàng --")
        print(f"{'STT |'}{'Mã SP |'}{'Tên SP |'}{'SL |'}{'Đơn Giá |'}{'Thành Tiền |'}")
        for i, j in enumerate(cart_items, start=1):
            total = j["number"] * j["price"]
            total_number += j["number"]
            total_price += total
            print(
                f"{i} |"
                f"{j['id']} |"
                f"{j['name']} |"
                f"{j['number']} |"
                f"{j['price']} |"
                f"{total}"
            )
        print(f"Tổng số lượng sản phẩm trong giỏ hàng: {total_number}")
        print(f"Tổng tiền thanh toán: {total_price}")
    if choice == 2:
        print("Thêm sản phẩm mới.")
        add_id = input("Nhập mã sản phẩm cần thêm: ").strip().upper()
        for i in cart_items:
            if i['number'] == add_id.upper():
                number = int(input("Nhập số lượng sản phẩm: "))
                if number <= 0:
                    print("Số lượng phải lớn hơn 0")
                    continue
                else:
                    i[number] += number
                    print("Đã cộng dồn số lượng.")
                    break
            else:
                name = input("Nhập tên sản phẩm: ")
                number = int(input("Nhập số lượng sản phẩm: "))
                price = float(input("Nhập giá sản phẩm: "))
                cart_items.append({
                    "id": add_id,
                    "name": name,
                    "number": number,
                    "price": price
                })
                print("Đã thêm sản phẩm mới.")
                break
    if choice == 3:
        print("Cập nhật số lượng sản phẩm: ")
        search_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
        for i in cart_items:
            if search_id.upper() == i["id"]:
                number = int(input("Nhập số lượng mới: "))
                if number <= 0:
                    print("Số lượng phải lớn hơn 0")
                    continue
                else:
                    i["number"] = number
                    print("Đã cập nhật số lượng.")
                    break
    if choice == 4:
        search_id = input("Nhập mã sản phẩm cần xoá: ").strip().upper()
        a = False
        for i in cart_items:
            if search_id.upper() == i["id"]:
                cart_items.remove(i)
                print("Xoá thành công")
                a = True
                break
        if a == False:
            print("Không tìm thấy mã sản phẩm cần xoá")
    if choice == 5:
        print("Đã thoát chương trình.")
        break
    if choice > 5 or choice < 1:
        print("Lựa chọn không hợp lệ.")
        break
                