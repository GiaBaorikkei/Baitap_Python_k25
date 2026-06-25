class Drink:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.__price = price
        self.is_available = True

    @property
    def price(self):
        return self.__price

    def toggle_available(self):
        self.is_available = not self.is_available


menu = [
    Drink("CF01", "Cà phê sữa", 35000),
    Drink("TS01", "Trà sữa matcha", 45000),
    Drink("TD01", "Trà đào cam sả", 40000)
]


def show_menu():
    print("\n=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===")
    print("1. Xem danh sách đồ uống")
    print("2. Thêm đồ uống mới")
    print("3. Cập nhật trạng thái kinh doanh")
    print("4. Thoát chương trình")
    print("=" * 45)


def display_drinks():
    if not menu:
        print("Thực đơn đang trống!")
        return

    print("\n--- DANH SÁCH ĐỒ UỐNG ---")
    print(f"{'Mã món':<10}{'Tên món':<25}{'Giá bán':<12}{'Trạng thái'}")

    for drink in menu:
        status = "Đang bán" if drink.is_available else "Ngừng bán"
        print(f"{drink.code:<10}{drink.name:<25}{drink.price:<12}{status}")


def add_drink():
    code = input("Nhập mã món: ").strip().upper()

    for drink in menu:
        if drink.code == code:
            print("Mã món đã tồn tại trong hệ thống!")
            return

    name = input("Nhập tên món: ").strip()

    try:
        price = int(input("Nhập giá bán: "))
    except ValueError:
        print("Giá bán không hợp lệ!")
        return

    if price <= 0:
        print("Giá bán không hợp lệ!")
        return

    new_drink = Drink(code, name, price)
    menu.append(new_drink)

    print(f"Thành công: Đã thêm món {name} vào thực đơn!")


def update_status():
    code = input("Nhập mã món cần cập nhật: ").strip().upper()

    for drink in menu:
        if drink.code == code:
            drink.toggle_available()
            status = "Đang bán" if drink.is_available else "Ngừng bán"
            print(f"Đã cập nhật trạng thái món {code}.")
            print(f"Trạng thái hiện tại: {status}")
            return

    print("Không tìm thấy món có mã này!")


def main():
    while True:
        show_menu()

        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            display_drinks()

        elif choice == "2":
            add_drink()

        elif choice == "3":
            update_status()

        elif choice == "4":
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý thực đơn Rikkei Coffee!")
            break

        else:
            print("Lựa chọn không hợp lệ!")


main()