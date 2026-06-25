class BankAccount:
    # Class attributes
    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        # Private attributes
        self.__account_number = account_number
        self.__balance = 0

        # Use setter automatically
        self.account_name = account_name

    # ================= PROPERTY =================

    # @property:
    # Allows reading value like attribute:
    # account.balance
    @property
    def balance(self):
        return self.__balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def account_name(self):
        return self.__account_name

    # @setter:
    # Controls updating account_name safely
    @account_name.setter
    def account_name(self, new_name):

        cleaned_name = " ".join(new_name.strip().split())

        if cleaned_name == "":
            print("Tên tài khoản không được để trống")
            return

        self.__account_name = cleaned_name.upper()

    # ================= STATIC METHOD =================

    @staticmethod
    def validate_account_number(account_number):
        return (
            account_number.isdigit()
            and len(account_number) == 10
        )

    # ================= CLASS METHOD =================

    @classmethod
    def update_transaction_fee(cls, new_fee):
        cls.transaction_fee = new_fee

    # ================= INSTANCE METHODS =================

    def deposit(self, amount):

        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        self.__balance += amount
        return True

    def withdraw(self, amount):

        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        total = amount + BankAccount.transaction_fee

        if self.__balance < total:
            print(
                "Giao dịch thất bại. "
                "Số dư không đủ để thanh toán số tiền và phí giao dịch"
            )
            return False

        self.__balance -= total
        return True

    def display_info(self):

        print("\n--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Ngân hàng: {BankAccount.bank_name}")
        print(f"Số tài khoản: {self.__account_number}")
        print(f"Tên chủ tài khoản: {self.__account_name}")
        print(
            f"Số dư hiện tại: "
            f"{self.__balance:,} VND"
        )
        print(
            f"Phí giao dịch: "
            f"{BankAccount.transaction_fee:,} VND"
        )


# ================= MAIN PROGRAM =================

current_account = None

while True:

    print("\n===== VIETCOMBANK DIGIBANK SIMULATOR =====")
    print("1. Mở tài khoản mới")
    print("2. Xem thông tin tài khoản")
    print("3. Giao dịch Nạp / Rút tiền")
    print("4. Cập nhật Tên chủ tài khoản")
    print("5. Đổi phí giao dịch hệ thống")
    print("6. Thoát chương trình")
    print("==========================================")

    choice = input("Chọn chức năng (1-6): ")

    # ================= FUNCTION 1 =================

    if choice == "1":

        print("\n--- MỞ TÀI KHOẢN MỚI ---")

        while True:

            account_number = input(
                "Nhập số tài khoản 10 chữ số: "
            )

            if BankAccount.validate_account_number(
                account_number
            ):
                break

            print("Số tài khoản không hợp lệ!")
            print(
                "Số tài khoản phải gồm đúng 10 chữ số."
            )

        account_name = input(
            "Nhập tên chủ tài khoản: "
        )

        current_account = BankAccount(
            account_number,
            account_name
        )

        print("\nMở tài khoản thành công!")
        print(
            f"Số tài khoản: "
            f"{current_account.account_number}"
        )
        print(
            f"Tên chủ tài khoản: "
            f"{current_account.account_name}"
        )

    # ================= FUNCTION 2 =================

    elif choice == "2":

        if current_account is None:
            print(
                "\nHệ thống chưa có thông tin tài khoản"
            )
            print(
                "Vui lòng mở tài khoản "
                "ở Chức năng 1 trước."
            )

        else:
            current_account.display_info()

    # ================= FUNCTION 3 =================

    elif choice == "3":

        if current_account is None:
            print(
                "\nHệ thống chưa có thông tin tài khoản"
            )
            continue

        print("\n--- GIAO DỊCH NẠP / RÚT TIỀN ---")
        print("1. Nạp tiền")
        print("2. Rút tiền")

        transaction_type = input(
            "Chọn loại giao dịch (1-2): "
        )

        try:

            amount = int(
                input(
                    "Nhập số tiền giao dịch: "
                )
            )

            if transaction_type == "1":

                if current_account.deposit(amount):

                    print(
                        f"\nNạp tiền thành công: "
                        f"+{amount:,} VND"
                    )

                    print(
                        f"Số dư mới: "
                        f"{current_account.balance:,} VND"
                    )

            elif transaction_type == "2":

                if current_account.withdraw(amount):

                    print(
                        f"\nRút tiền thành công: "
                        f"-{amount:,} VND"
                    )

                    print(
                        f"Phí giao dịch: "
                        f"{BankAccount.transaction_fee:,} VND"
                    )

                    print(
                        f"Số dư mới: "
                        f"{current_account.balance:,} VND"
                    )

                else:

                    print(
                        f"Số dư mới: "
                        f"{current_account.balance:,} VND"
                    )

            else:
                print("Lựa chọn không hợp lệ")

        except ValueError:
            print(
                "Vui lòng nhập số tiền hợp lệ"
            )

    # ================= FUNCTION 4 =================

    elif choice == "4":

        if current_account is None:
            print(
                "\nHệ thống chưa có thông tin tài khoản"
            )
            continue

        print(
            "\n--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---"
        )

        new_name = input("Nhập tên mới: ")

        old_name = current_account.account_name

        current_account.account_name = new_name

        if old_name != current_account.account_name:

            print(
                f"Cập nhật thành công. "
                f"Tên mới: "
                f"{current_account.account_name}"
            )

    # ================= FUNCTION 5 =================

    elif choice == "5":

        print(
            "\n--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---"
        )

        print(
            f"Phí giao dịch hiện tại: "
            f"{BankAccount.transaction_fee:,} VND"
        )

        try:

            new_fee = int(
                input(
                    "Nhập phí giao dịch mới: "
                )
            )

            if new_fee < 0:

                print(
                    "Phí giao dịch không được âm"
                )

                print(
                    f"Phí giao dịch hiện tại "
                    f"vẫn là "
                    f"{BankAccount.transaction_fee:,} VND"
                )

            else:

                BankAccount.update_transaction_fee(
                    new_fee
                )

                print(
                    "Đã cập nhật phí giao dịch "
                    f"toàn hệ thống thành "
                    f"{new_fee:,} VND"
                )

        except ValueError:

            print(
                "Phí giao dịch không hợp lệ"
            )

    # ================= FUNCTION 6 =================

    elif choice == "6":

        print(
            "\nCảm ơn bạn đã sử dụng "
            "Vietcombank Digibank!"
        )

        break

    else:
        print("Lựa chọn không hợp lệ")