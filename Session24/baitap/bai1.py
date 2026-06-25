class CoffeeOrder:

    # Class Attribute
    vat_rate = 0.10

    def __init__(self, table_number):
        """
        Initialize a new coffee order.
        """
        self.table_number = table_number
        self.__total_amount = 0

    @property
    def total_amount(self):
        """
        Read-only property for total amount.
        """
        return self.__total_amount

    def add_item(self, price):
        """
        Add item price into the bill.
        """
        if price > 0:
            self.__total_amount += price

    def calculate_final_bill(self):
        """
        Calculate final bill including VAT.
        """
        return self.__total_amount * (1 + CoffeeOrder.vat_rate)

    @classmethod
    def update_vat_rate(cls, new_rate):
        """
        Update VAT rate for the entire system.
        """
        cls.vat_rate = new_rate

order_table1 = CoffeeOrder("Bàn 1")
order_table2 = CoffeeOrder("Bàn 2")

order_table1.add_item(50000)
order_table2.add_item(30000)

print("===== Trước khi gian lận =====")
print(order_table1.total_amount)

try:
    order_table1.total_amount = 0
except AttributeError:
    print("Không thể sửa trực tiếp tổng tiền hóa đơn!")

print("\n===== Sau khi cố sửa =====")
print(order_table1.total_amount)

# Quản lý cập nhật VAT
CoffeeOrder.update_vat_rate(0.08)

print("\n===== Kiểm tra VAT =====")
print("VAT bàn 1:", order_table1.vat_rate)
print("VAT bàn 2:", order_table2.vat_rate)

print("\n===== Hóa đơn =====")
print("Bàn 1:", order_table1.calculate_final_bill())
print("Bàn 2:", order_table2.calculate_final_bill())