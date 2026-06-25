class MemberCard:

    def __init__(self, customer_name, points=0):
        self.customer_name = customer_name
        self.__points = 0
        self.points = points

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        if not isinstance(value, int) or value < 0:
            print("Dữ liệu điểm không hợp lệ!")
            return

        self.__points = value

    def add_points(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.__points += amount
        else:
            print("Số điểm cộng không hợp lệ!")

    @staticmethod
    def is_eligible_for_voucher(bill_amount):
        return bill_amount >= 200000

card1 = MemberCard("Le Van C", 100)

print("===== Điểm ban đầu =====")
print(card1.points)

print("\n===== Thử gán điểm âm =====")
card1.points = -50

print("Điểm hiện tại:", card1.points)

print("\n===== Thử gán chuỗi =====")
card1.points = "một trăm"

print("Điểm hiện tại:", card1.points)

print("\n===== Cộng điểm =====")
card1.add_points(50)

print("Điểm hiện tại:", card1.points)

print("\n===== Kiểm tra Voucher =====")
result = MemberCard.is_eligible_for_voucher(250000)

print("Hóa đơn 250000 có được tặng voucher?", result)