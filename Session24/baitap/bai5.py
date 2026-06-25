import re


class BistroTable:
    """
    Quản lý một bàn ăn trong nhà hàng Rikkei Bistro.
    """

    # Class Attribute
    _vat_rate = 0.08

    def __init__(self, table_id, capacity):
        self.__table_id = table_id.upper()
        self.capacity = capacity
        self.__current_bill = 0

    @property
    def table_id(self):
        """Đọc mã bàn."""
        return self.__table_id

    @property
    def current_bill(self):
        """Đọc tiền tạm tính."""
        return self.__current_bill

    @property
    def status(self):
        """Tính trạng thái động."""
        if self.__current_bill == 0:
            return "Đang trống"
        return "Có khách"

    @property
    def final_bill(self):
        """Tính tổng thanh toán sau VAT."""
        return int(self.__current_bill * (1 + BistroTable._vat_rate))

    @staticmethod
    def is_valid_table_id(table_id):
        """
        Kiểm tra mã bàn.
        Ví dụ hợp lệ: TB01
        """
        return re.fullmatch(r"TB\d+", table_id.upper()) is not None

    @classmethod
    def update_vat_rate(cls, new_rate):
        cls._vat_rate = new_rate

    def order_dish(self, amount):
        """Gọi món."""
        if amount <= 0:
            print("Vui lòng nhập số tiền là một số nguyên dương!")
            return

        self.__current_bill += amount

        print(
            f">> Thành công: Đã ghi nhận món ăn {amount:,}đ vào Bàn '{self.__table_id}'."
        )
        print(f">> Số tiền tạm tính hiện tại của bàn: {self.__current_bill:,}đ.")

    def cancel_dish(self, amount):
        """Hủy món."""
        if amount <= 0:
            print("Vui lòng nhập số tiền là một số nguyên dương!")
            return

        if amount > self.__current_bill:
            print("Lỗi: Số tiền giảm trừ vượt quá giá trị hóa đơn hiện tại!")
            return

        self.__current_bill -= amount

        print(
            f">> Thành công: Đã giảm trừ {amount:,}đ khỏi Bàn '{self.__table_id}' do sự cố bếp."
        )
        print(f">> Số tiền tạm tính còn lại: {self.__current_bill:,}đ.")

        if self.__current_bill == 0:
            print(
                f">> Bàn '{self.__table_id}' hiện đã chuyển về trạng thái Đang trống."
            )

    def checkout(self):
        """Thanh toán."""
        if self.__current_bill == 0:
            print("Lỗi: Bàn này hiện đang trống, không có hóa đơn để thanh toán!")
            return

        print(f"\n--- HÓA ĐƠN THANH TOÁN BÀN {self.__table_id} ---")
        print(f"Số tiền món ăn: {self.__current_bill:,}đ")
        print(f"Thuế suất VAT áp dụng: {BistroTable._vat_rate*100:.0f}%")
        print(f"Tổng tiền cần thanh toán: {self.final_bill:,}đ")
        print("-----------------------------------")

        self.__current_bill = 0

        print(
            f">> Thanh toán thành công! Bàn '{self.__table_id}' đã được dọn sạch và chuyển sang trạng thái Đang trống."
        )


# ==========================
# Mock Data
# ==========================

table_records = [
    BistroTable("TB01", 4),
    BistroTable("TB02", 2),
    BistroTable("TB03", 8),
]


def find_table(table_id):
    table_id = table_id.upper()
    for table in table_records:
        if table.table_id == table_id:
            return table
    return None


# ==========================
# MENU
# ==========================

while True:

    print("\n===== HỆ THỐNG ĐIỀU PHỐI BÀN ĂN - RIKKEI BISTRO =====")
    print("1. Hiển thị sơ đồ bàn")
    print("2. Gọi món")
    print("3. Hủy món")
    print("4. Cập nhật VAT")
    print("5. Thanh toán")
    print("6. Thoát")
    print("====================================================")

    choice = input("Chọn chức năng (1-6): ")

    # =====================================
    if choice == "1":

        print("\n--- SƠ ĐỒ BÀN ĂN RIKKEI BISTRO ---")

        for i, table in enumerate(table_records, start=1):
            print(
                f"{i}. "
                f"Mã bàn: {table.table_id} | "
                f"Sức chứa: {table.capacity} người | "
                f"Tạm tính: {table.current_bill:,}đ | "
                f"Trạng thái: {table.status}"
            )

        print("----------------------------------")

    # =====================================
    elif choice == "2":

        print("\n--- GỌI MÓN MỚI ---")

        table_id = input("Nhập mã bàn gọi món: ").strip().upper()

        if not BistroTable.is_valid_table_id(table_id):
            print("Mã bàn không hợp lệ!")
            continue

        table = find_table(table_id)

        if table is None:
            print("Không tìm thấy bàn.")
            continue

        try:
            amount = int(input("Nhập giá tiền món ăn mới: "))
            table.order_dish(amount)
        except ValueError:
            print("Vui lòng nhập số tiền là một số nguyên dương!")

    # =====================================
    elif choice == "3":

        print("\n--- HỦY MÓN / GIẢM TRỪ HÓA ĐƠN ---")

        table_id = input("Nhập mã bàn: ").strip().upper()

        table = find_table(table_id)

        if table is None:
            print("Không tìm thấy bàn.")
            continue

        try:
            amount = int(input("Nhập giá trị món muốn giảm trừ: "))
            table.cancel_dish(amount)
        except ValueError:
            print("Vui lòng nhập số tiền là một số nguyên dương!")

    # =====================================
    elif choice == "4":

        print("\n--- CẬP NHẬT THUẾ SUẤT VAT ---")

        print(
            f"VAT hiện tại: {BistroTable._vat_rate*100:.0f}% ({BistroTable._vat_rate})"
        )

        try:
            new_rate = float(input("Nhập VAT mới: "))

            if new_rate < 0 or new_rate > 0.2:
                print("Tỷ lệ thuế không hợp lệ!")
                continue

            BistroTable.update_vat_rate(new_rate)

            print(
                f">> Thông báo: VAT mới là {new_rate*100:.0f}%."
            )

        except ValueError:
            print("Tỷ lệ thuế không hợp lệ!")

    # =====================================
    elif choice == "5":

        print("\n--- THANH TOÁN HÓA ĐƠN ---")

        table_id = input("Nhập mã bàn: ").strip().upper()

        table = find_table(table_id)

        if table is None:
            print("Không tìm thấy bàn.")
            continue

        table.checkout()

    # =====================================
    elif choice == "6":

        print("Cảm ơn bạn đã sử dụng hệ thống điều phối bàn ăn Rikkei Bistro!")
        break

    else:
        print("Lựa chọn không hợp lệ!")