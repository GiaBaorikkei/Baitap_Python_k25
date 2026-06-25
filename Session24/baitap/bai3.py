import re


class MemberCard:
    # Class Attribute
    point_value_vnd = 1000

    def __init__(self, card_id, name):
        self.card_id = card_id
        self.name = name.title()
        self.__points = 0
        self.__tier = "Standard"

    @property
    def points(self):
        return self.__points

    @property
    def tier(self):
        return self.__tier

    @staticmethod
    def is_valid_card_id(card_id):
        return re.fullmatch(r"RC\d{2}", card_id) is not None

    @classmethod
    def update_point_value(cls, new_value):
        cls.point_value_vnd = new_value

    def earn_points(self, bill_amount):
        earned = bill_amount // 10000
        self.__points += earned

        upgraded = False
        if self.__points >= 100 and self.__tier != "VIP":
            self.__tier = "VIP"
            upgraded = True

        return earned, upgraded

    def redeem_points(self, points_to_use):
        """
        Redeem points for discount.
        """
        if points_to_use <= 0:
            print("Số điểm phải lớn hơn 0.")
            return False

        if points_to_use > self.__points:
            print("\nKhông thể đổi điểm!")
            print("Số điểm muốn sử dụng vượt quá số điểm hiện có.")
            print(f"Điểm hiện tại của khách: {self.__points}")
            print("Điểm cũ được giữ nguyên.")
            print(f"Số điểm sau giao dịch: {self.__points}")
            return False

        self.__points -= points_to_use

        discount = points_to_use * MemberCard.point_value_vnd

        print(f"\nĐã trừ {points_to_use} điểm.")
        print(f"Khách hàng được giảm giá {discount:,} VNĐ vào hóa đơn!")
        print(f"Số điểm còn lại: {self.__points}")
        print(f"Hạng thẻ hiện tại: {self.__tier}")

        return True


cards = []


def find_card(card_id):
    for card in cards:
        if card.card_id == card_id:
            return card
    return None


while True:

    print("\n===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====")
    print("1. Xem danh sách thẻ thành viên")
    print("2. Đăng ký thẻ mới")
    print("3. Khách mua hàng (Tích điểm)")
    print("4. Khách dùng điểm (Đổi ưu đãi)")
    print("5. Cập nhật tỷ giá quy đổi điểm")
    print("6. Thoát chương trình")
    print("================================================")

    choice = input("Chọn chức năng (1-6): ")
    if choice == "1":

        if not cards:
            print("Chưa có thẻ thành viên.")
        else:
            print("\n===== DANH SÁCH THẺ =====")
            for i, card in enumerate(cards, start=1):
                print(
                    f"{i}. Mã: {card.card_id} | "
                    f"Tên: {card.name:<20} | "
                    f"Điểm: {card.points:<5} | "
                    f"Hạng: {card.tier}"
                )

    elif choice == "2":

        print("\n--- ĐĂNG KÝ THẺ THÀNH VIÊN MỚI ---")

        card_id = input("Nhập mã thẻ: ").strip().upper()

        if not MemberCard.is_valid_card_id(card_id):
            print("Mã thẻ không đúng định dạng!")
            continue

        if find_card(card_id):
            print("Mã thẻ đã tồn tại trong hệ thống!")
            print("Vui lòng kiểm tra lại.")
            continue

        name = input("Nhập tên khách hàng: ")

        card = MemberCard(card_id, name)

        cards.append(card)

        print("\nĐăng ký thẻ thành viên thành công!")
        print(f"Mã thẻ: {card.card_id}")
        print(f"Tên khách hàng: {card.name}")
        print(f"Điểm ban đầu: {card.points}")
        print(f"Hạng thẻ: {card.tier}")
    elif choice == "3":

        print("\n--- KHÁCH MUA HÀNG - TÍCH ĐIỂM ---")

        card_id = input("Nhập mã thẻ: ").strip().upper()

        card = find_card(card_id)

        if card is None:
            print("Không tìm thấy thẻ.")
            continue

        bill = int(input("Nhập tổng tiền hóa đơn: "))

        earned, upgraded = card.earn_points(bill)

        print(f"\nKhách hàng: {card.name}")
        print(f"Hóa đơn: {bill:,} VNĐ")
        print(f"Số điểm được tích: {earned}")
        print(f"Tổng điểm hiện tại: {card.points}")

        if upgraded:
            print("\nChúc mừng! Khách hàng đã được nâng hạng lên VIP.")

        print(f"Hạng thẻ hiện tại: {card.tier}")

    elif choice == "4":

        print("\n--- KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI ---")

        print(
            f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ"
        )

        card_id = input("Nhập mã thẻ: ").strip().upper()

        card = find_card(card_id)

        if card is None:
            print("Không tìm thấy thẻ.")
            continue

        points = int(input("Nhập số điểm muốn sử dụng: "))

        card.redeem_points(points)

    elif choice == "5":

        print("\n--- CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM ---")

        print(
            f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ"
        )

        new_value = int(input("Nhập tỷ giá mới cho 1 điểm: "))

        MemberCard.update_point_value(new_value)

        print("\nCập nhật tỷ giá thành công!")
        print(
            f"Tỷ giá mới: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ"
        )

    elif choice == "6":

        print("Cảm ơn bạn đã sử dụng hệ thống thẻ thành viên Rikkei Coffee!")
        break

    else:
        print("Lựa chọn không hợp lệ.")