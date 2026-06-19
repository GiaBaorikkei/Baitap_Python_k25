"""
Highlands Mini POS - Business Logic
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000},
}


class ItemNotFoundError(Exception):
    """Raised when drink code does not exist."""


class InvalidQuantityError(Exception):
    """Raised when quantity <= 0."""


def show_menu():
    """Display drink menu."""

    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")

    for code, item in DRINK_MENU.items():
        print(
            f"[{code}] - {item['name']} - {item['price']:,} VNĐ"
        )


def add_to_order(current_order, drink_code, quantity):
    """
    Add drink into order.

    Raises:
        ItemNotFoundError
        InvalidQuantityError
    """

    drink_code = drink_code.strip().upper()

    if drink_code not in DRINK_MENU:
        raise ItemNotFoundError(drink_code)

    if quantity <= 0:
        raise InvalidQuantityError(quantity)

    current_order.append(
        {
            "code": drink_code,
            "quantity": quantity
        }
    )

    logging.info(
        "Added %s of %s to order",
        quantity,
        drink_code
    )


def calculate_total(current_order):
    """Return total payment."""

    total = 0

    for item in current_order:
        price = DRINK_MENU[item["code"]]["price"]
        total += price * item["quantity"]

    return total


def view_order(current_order):
    """Display current order."""

    if not current_order:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return

    print("\n--- GIỎ HÀNG HIỆN TẠI ---")
    print("Mã SP | Tên đồ uống | Đơn giá | SL | Thành tiền")
    print("-" * 65)

    total = 0

    for item in current_order:
        drink = DRINK_MENU[item["code"]]
        subtotal = drink["price"] * item["quantity"]
        total += subtotal

        print(
            f"{item['code']:5}"
            f" | {drink['name']:18}"
            f" | {drink['price']:,}"
            f" | {item['quantity']:2}"
            f" | {subtotal:,} VNĐ"
        )

    print("-" * 65)
    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")


def checkout(current_order):
    """Checkout order."""

    if not current_order:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return

    total = calculate_total(current_order)

    print("\n--- THANH TOÁN ---")
    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")

    confirm = input(
        f"Xác nhận thanh toán {total:,} VNĐ? (y/n): "
    ).strip().lower()

    if confirm == "y":
        logging.info("Checkout successful")
        current_order.clear()
        print("Thanh toán thành công.")
        print("Giỏ hàng đã được làm trống.")

    elif confirm == "n":
        print("Đã hủy thao tác thanh toán. Quay lại menu chính.")

    else:
        print("Lựa chọn không hợp lệ. Thanh toán đã bị hủy.")