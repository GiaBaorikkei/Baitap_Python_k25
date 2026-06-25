class NetflixAccount:
    platform_name = "Netflix"
    max_profiles = 5

    def __init__(self, email):
        self.email = email
        self.__password = ""
        self.__plan = "Basic"
        self.profiles = []

    @property
    def password(self):
        return "********"

    @password.setter
    def password(self, new_password):
        if len(new_password) < 6:
            raise ValueError("Password is too short")

        self.__password = new_password

    @property
    def plan(self):
        return self.__plan

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email

    @classmethod
    def update_max_profiles(cls, new_limit):
        cls.max_profiles = new_limit

    def add_profile(self, profile_name):
        if len(self.profiles) >= NetflixAccount.max_profiles:
            print("Đã đạt giới hạn số lượng Profile trên tài khoản này.")
            return

        self.profiles.append(profile_name)
        print("Thêm Profile thành công.")

    def upgrade_plan(self, new_plan):
        valid_plans = ["Basic", "Standard", "Premium"]

        if new_plan not in valid_plans:
            print("Gói cước không hợp lệ.")
            return

        self.__plan = new_plan
        print("Nâng cấp gói thành công.")

    def display_info(self):
        print("\n========== ACCOUNT INFO ==========")
        print(f"Platform : {NetflixAccount.platform_name}")
        print(f"Email    : {self.email}")
        print(f"Password : {self.password}")
        print(f"Plan     : {self.plan}")

        if self.profiles:
            print("Profiles :")
            for i, profile in enumerate(self.profiles, start=1):
                print(f"  {i}. {profile}")
        else:
            print("Profiles : None")

        print("==================================\n")


def register_account():
    email = input("Enter email: ").strip()

    if not NetflixAccount.validate_email(email):
        print("Email không hợp lệ, vui lòng chứa ký tự '@' và '.'.")
        return None

    account = NetflixAccount(email)

    while True:
        try:
            password = input("Enter password: ")
            account.password = password
            break
        except ValueError as e:
            print(e)

    print("Đăng ký thành công.")
    return account


def main():
    current_account = None

    while True:

        print("\n===== NETFLIX ACCOUNT MANAGER =====")
        print("1. Đăng ký tài khoản mới")
        print("2. Xem thông tin tài khoản")
        print("3. Thêm người xem")
        print("4. Nâng cấp gói cước")
        print("5. Cập nhật chính sách Netflix")
        print("6. Thoát chương trình")
        print("===================================")

        choice = input("Chọn chức năng (1-6): ")

        if choice == "1":

            current_account = register_account()

        elif choice == "2":

            if current_account is None:
                print("Vui lòng đăng ký tài khoản trước (Chức năng 1).")
            else:
                current_account.display_info()

        elif choice == "3":

            if current_account is None:
                print("Vui lòng đăng ký tài khoản trước (Chức năng 1).")
            else:
                profile = input("Nhập tên Profile: ")
                current_account.add_profile(profile)

        elif choice == "4":

            if current_account is None:
                print("Vui lòng đăng ký tài khoản trước (Chức năng 1).")
            else:
                print("\nAvailable Plans")
                print("1. Basic")
                print("2. Standard")
                print("3. Premium")

                option = input("Choose plan: ")

                mapping = {
                    "1": "Basic",
                    "2": "Standard",
                    "3": "Premium"
                }

                if option in mapping:
                    current_account.upgrade_plan(mapping[option])
                else:
                    print("Lựa chọn không hợp lệ.")

        elif choice == "5":

            while True:
                try:
                    new_limit = int(input("Nhập giới hạn Profile mới: "))

                    if new_limit <= 0:
                        print("Giới hạn phải lớn hơn 0.")
                        continue

                    NetflixAccount.update_max_profiles(new_limit)

                    print(
                        f"Đã cập nhật giới hạn Profile toàn hệ thống thành {new_limit}."
                    )

                    break

                except ValueError:
                    print("Vui lòng nhập số nguyên.")

        elif choice == "6":

            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()