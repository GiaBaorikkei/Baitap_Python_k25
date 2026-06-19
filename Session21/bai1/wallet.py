"""
MoMo Wallet CLI
"""

import logging
import os
import re


logging.basicConfig(
    filename="momo_transactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class InvalidAmountError(Exception):
    """Raised when amount <= 0."""


class InsufficientBalanceError(Exception):
    """Raised when balance is insufficient."""


class TransactionLogger:
    """Logging helper."""

    @staticmethod
    def info(message):
        logging.info(message)

    @staticmethod
    def warning(message):
        logging.warning(message)

    @staticmethod
    def error(message):
        logging.error(message)


class Wallet:
    """Wallet model."""

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        """
        Deposit money.
        """

        if amount <= 0:
            raise InvalidAmountError

        self.balance += amount

        TransactionLogger.info(
            f"Deposit successful: +{amount} VND. "
            f"Current Balance: {self.balance}"
        )

    def transfer(self, phone, amount):
        """
        Transfer money.
        """

        if amount <= 0:
            raise InvalidAmountError

        if amount > self.balance:
            raise InsufficientBalanceError

        if amount >= 10_000_000:
            TransactionLogger.warning(
                f"High value transaction detected: "
                f"{amount} VND to {phone}"
            )

        self.balance -= amount

        TransactionLogger.info(
            f"Transfer successful: -{amount} VND to {phone}. "
            f"Current Balance: {self.balance}"
        )

    def show_balance(self):
        """
        Return balance.
        """

        TransactionLogger.info(
            f"Balance checked. Current Balance: {self.balance}"
        )

        return self.balance


def input_amount(message):
    """
    Input amount safely.
    """

    while True:
        try:
            amount = int(input(message))

            if amount <= 0:
                raise InvalidAmountError

            return amount

        except ValueError:
            print("Lỗi: Vui lòng nhập số tiền hợp lệ.")

            TransactionLogger.error(
                "ValueError: Invalid numeric input."
            )

        except InvalidAmountError:
            print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")

            TransactionLogger.error(
                f"InvalidAmountError: Attempted to process "
                f"{amount} VND."
            )


def input_phone():
    """
    Validate phone number.
    """

    while True:

        phone = input("Nhập số điện thoại người nhận: ")

        if re.fullmatch(r"\d{10}", phone):
            return phone

        print("Số điện thoại không hợp lệ.")


def display_log():
    """
    Display log history.
    """

    if not os.path.exists("momo_transactions.log"):
        print("Chưa có lịch sử giao dịch nào trong hệ thống.")
        return

    with open(
        "momo_transactions.log",
        "r",
        encoding="utf-8"
    ) as file:
        print(file.read())


def display_menu():
    """
    Print menu.
    """

    print("\n========== VÍ MOMO GIẢ LẬP ==========")
    print("1. Nạp tiền")
    print("2. Chuyển tiền")
    print("3. Xem số dư")
    print("4. Thoát")
    print("====================================")


def main():
    """
    Main program.
    """

    wallet = Wallet()

    while True:

        display_menu()

        choice = input("Chọn chức năng: ")

        if choice == "1":

            print("\n--- NẠP TIỀN ---")

            amount = input_amount(
                "Nhập số tiền cần nạp: "
            )

            wallet.deposit(amount)

            print(
                f"Nạp thành công: +{amount:,} VND"
            )

            print(
                f"Số dư hiện tại: "
                f"{wallet.balance:,} VND"
            )

        elif choice == "2":

            print("\n--- CHUYỂN TIỀN ---")

            phone = input_phone()

            amount = input_amount(
                "Nhập số tiền cần chuyển: "
            )

            try:

                wallet.transfer(phone, amount)

                print("Chuyển tiền thành công.")

                print(
                    f"Số dư còn lại: "
                    f"{wallet.balance:,} VND"
                )

            except InsufficientBalanceError:

                print(
                    "Giao dịch thất bại: "
                    "Số dư của bạn không đủ."
                )

                TransactionLogger.error(
                    f"InsufficientBalanceError: "
                    f"Attempted to transfer "
                    f"{amount} VND with balance "
                    f"{wallet.balance} VND."
                )

            except InvalidAmountError:

                print(
                    "Lỗi: Số tiền giao dịch "
                    "phải lớn hơn 0."
                )

                TransactionLogger.error(
                    f"InvalidAmountError: "
                    f"Attempted to process "
                    f"{amount} VND."
                )

        elif choice == "3":

            print("\n--- SỐ DƯ VÍ MOMO ---")

            print(
                f"Số dư hiện tại: "
                f"{wallet.show_balance():,} VND"
            )

            print("\n--- LỊCH SỬ GIAO DỊCH ---")
            display_log()

        elif choice == "4":

            print("Cảm ơn bạn đã sử dụng dịch vụ.")

            TransactionLogger.info("System shutdown")

            break

        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()