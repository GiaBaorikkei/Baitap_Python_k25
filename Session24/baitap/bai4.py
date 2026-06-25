import re


class MenuItem:
    """
    Class đại diện cho một món đồ uống.
    """

    # Class Attribute
    service_charge = 0.0

    def __init__(self, item_id, item_name, base_price):
        self.item_id = item_id
        self.item_name = item_name.title()
        self.__base_price = base_price
        self.__is_available = True

    @property
    def base_price(self):
        """Getter của giá gốc."""
        return self.__base_price

    @base_price.setter
    def base_price(self, new_price):
        """Setter kiểm tra giá hợp lệ."""
        if new_price <= 0:
            print("Giá đồ uống phải lớn hơn 0!")
            print("Giá cũ được giữ nguyên.")
            return

        self.__base_price = new_price
        print("Cập nhật giá gốc thành công!")

    @property
    def is_available(self):
        """Getter trạng thái bán."""
        return self.__is_available

    @property
    def status(self):
        """Hiển thị trạng thái."""
        return "Đang bán" if self.__is_available else "Hết hàng"

    @staticmethod
    def is_valid_item_id(item_id):
        """
        Mã hợp lệ:
        CF01
        TE01
        JU99
        """
        return re.fullmatch(r"[A-Z]{2}\d{2}", item_id) is not None

    @classmethod
    def update_service_charge(cls, new_rate):
        """Cập nhật phụ phí toàn hệ thống."""
        cls.service_charge = new_rate

    def toggle_availability(self):
        """Đảo trạng thái bán."""
        self.__is_available = not self.__is_available

    def selling_price(self):
        """Giá niêm yết."""
        return int(self.__base_price * (1 + MenuItem.service_charge))


# ===============================
# Mock Data
# ===============================

menu_db = [
    MenuItem("CF01", "Cà Phê Đen", 30000),
    MenuItem("CF02", "Bạc Xỉu", 45000),
    MenuItem("TE01", "Trà Đào Cam Sả", 50000)
]


def find_item(item_id):
    for item in menu_db:
        if item.item_id == item_id:
            return item
    return None


# ===============================
# MENU
# ===============================

while True:

    print("\n===== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE =====")
    print("1. Xem thực đơn")
    print("2. Thêm món mới")
    print("3. Cập nhật trạng thái")
    print("4. Điều chỉnh giá gốc")
    print("5. Cập nhật phụ phí dịch vụ")
    print("6. Thoát")
    print("===================================================")

    choice = input("Chọn chức năng (1-6): ")

    # ==========================
    if choice == "1":

        print("\n--- THỰC ĐƠN RIKKEI COFFEE ---")

        for i, item in enumerate(menu_db, start=1):
            print(
                f"{i}. "
                f"Mã: {item.item_id} | "
                f"Tên: {item.item_name:<20} | "
                f"Trạng thái: {item.status:<10} | "
                f"Giá niêm yết: {item.selling_price():,} VNĐ"
            )

    # ==========================
    elif choice == "2":

        print("\n--- THÊM MÓN MỚI ---")

        item_id = input("Nhập mã món: ").strip().upper()

        if not MenuItem.is_valid_item_id(item_id):
            print("Mã món không hợp lệ!")
            print("Mã món phải gồm 2 chữ cái in hoa và 2 chữ số.")
            continue

        if find_item(item_id):
            print("Mã món đã tồn tại!")
            continue

        item_name = input("Nhập tên món: ")

        while True:
            try:
                base_price = int(input("Nhập giá gốc: "))
                if base_price <= 0:
                    print("Giá phải lớn hơn 0.")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập số.")

        menu_db.append(MenuItem(item_id, item_name, base_price))

        print("Thêm món mới thành công!")

    # ==========================
    elif choice == "3":

        print("\n--- CẬP NHẬT TRẠNG THÁI ---")

        item_id = input("Nhập mã món: ").strip().upper()

        item = find_item(item_id)

        if item is None:
            print("Không tìm thấy món.")
            continue

        item.toggle_availability()

        if item.is_available:
            print(f">> Đã cập nhật {item.item_name} thành ĐANG BÁN!")
        else:
            print(f">> Đã cập nhật {item.item_name} thành HẾT HÀNG!")

    # ==========================
    elif choice == "4":

        print("\n--- ĐIỀU CHỈNH GIÁ GỐC ---")

        item_id = input("Nhập mã món: ").strip().upper()

        item = find_item(item_id)

        if item is None:
            print("Không tìm thấy món.")
            continue

        try:
            new_price = int(input("Nhập giá mới: "))
            item.base_price = new_price
        except ValueError:
            print("Giá phải là số.")

    # ==========================
    elif choice == "5":

        print("\n--- CẬP NHẬT PHỤ PHÍ DỊCH VỤ ---")

        print(
            f"Phụ phí hiện tại: {MenuItem.service_charge * 100:.0f}%"
        )

        try:
            new_rate = float(
                input("Nhập phụ phí mới (Ví dụ 0.1): ")
            )

            if new_rate < 0:
                print("Không hợp lệ.")
                continue

            MenuItem.update_service_charge(new_rate)

            print("Cập nhật phụ phí dịch vụ thành công!")

        except ValueError:
            print("Dữ liệu không hợp lệ.")

    # ==========================
    elif choice == "6":

        print("Cảm ơn bạn đã sử dụng hệ thống Rikkei Coffee!")
        break

    else:
        print("Lựa chọn không hợp lệ.")