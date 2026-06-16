products_list = [
    {'id': 'P01', 'name': 'Coca Cola', 'price': 15000},
    {'id': 'P02', 'name': 'Bánh mì', 'price': 20000}
]

def show_products():
    if len(products_list) == 0:
        print("Cửa hàng hiện chưa có sản phẩm nào.")
        return
    print("--- DANH SÁCH SẢN PHẨM ---")
    print(f"{'ID':<10} | {'Tên sản phẩm':<20} | {'Giá bán':<10}")
    for i in products_list:
        print(f"{i['id']:<10} | {i['name']:<20} | {i['price']:<10}")
        
def add_product():
    print("--- THÊM SẢN PHẨM ---")
    while True:
        id_product = input("Nhập mã sản phẩm:").strip().upper()
        if id_product == "":
            print("ID không được để trống")
            continue
        is_exit = False
        for i in products_list:
            if i["id"] == id_product:
                is_exit = True
                break
        if is_exit:
            print("Mã sản phẩm đã tồn tại.")
            continue
        break
    while True:
        name_product = input("Nhập tên sản phẩm: ").strip()
        if name_product == "":
            print("Tên sản phẩm không được để trống.")
        else:
            break
    
    while True:
        price_product = int(input("Nhập giá bán sản phẩm: "))
        if price_product > 0:
            break
        print("Giá bán phải lớn hơn 0")

    product = {
        "id": id_product,
        "name": name_product,
        "price": price_product
    }
    products_list.append(product)
    
    print("Thêm sản phẩm thành công.")
        

def update_price():
    update_id = input("Nhập ID sản phẩm cần thay đổi giá: ").strip().upper()
    for i in products_list:
        if update_id == i["id"]:
            new_price = input("Nhập giá mới: ")
            i["price"] = new_price
            print("Cập nhật thành công")
            return 
    print("Không tìm thấy sản phẩm.")
    
def main():
    while True:
        print("--- QUẢN LÍ CỬA HÀNG - MINI STORE ---")
        print("1. Xem danh sách sản phẩm hiện có.")
        print("2. Thêm mới một sản phẩm.")
        print("3. Cập nhật giá sản phẩm theo ID.")
        print("4. Thoát chương trình.")
        
        choice = input("Mời bạn chọn chức năng (1-4): ")
        
        if choice == "1":
            show_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            update_price()
        elif choice == "4":
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")
main()