from abc import ABC, abstractmethod

active_companions = []
class Companion(ABC):
    """
    Lớp trừu tượng đại diện cho sinh vật đồng hành.
    """

    def __init__(self, name, level=1, **kwargs):
        super().__init__(**kwargs)
        self.name = name.title()
        self.level = level

    @abstractmethod
    def unleash_skill(self):
        """
        Kỹ năng đặc trưng.
        """
        pass

    def __add__(self, other):
        """
        Lai tạo 2 sinh vật.
        Chỉ cho phép cùng loài.
        """

        if not isinstance(other, Companion):
            raise TypeError(
                "Chỉ có thể lai tạo 2 sinh vật cùng loài!"
            )

        if type(self) != type(other):
            raise TypeError(
                "Chỉ có thể lai tạo 2 sinh vật cùng loài!"
            )

        if isinstance(self, Dragon):
            return Dragon(
                name=f"{self.name} {other.name}",
                bonus_atk=self.bonus_atk + other.bonus_atk,
                bonus_speed=self.bonus_speed + other.bonus_speed,
                level=max(self.level, other.level) + 1,
            )

        elif isinstance(self, Pet):
            return Pet(
                name=f"{self.name} {other.name}",
                bonus_atk=self.bonus_atk + other.bonus_atk,
                level=max(self.level, other.level) + 1,
            )

        elif isinstance(self, Mount):
            return Mount(
                name=f"{self.name} {other.name}",
                bonus_speed=self.bonus_speed + other.bonus_speed,
                level=max(self.level, other.level) + 1,
            )


class Pet(Companion):
    """
    Thú cưng chiến đấu.
    """

    def __init__(self, bonus_atk, **kwargs):
        super().__init__(**kwargs)
        self.bonus_atk = bonus_atk

    def unleash_skill(self):
        print(
            f">> {self.name} gầm gừ: "
            f"Tấn công kẻ thù, gây {self.bonus_atk} sát thương!"
        )


class Mount(Companion):
    """
    Thú cưỡi.
    """

    def __init__(self, bonus_speed, **kwargs):
        super().__init__(**kwargs)
        self.bonus_speed = bonus_speed

    def unleash_skill(self):
        print(
            f">> {self.name} hí vang: "
            f"Tăng tốc độ di chuyển thêm "
            f"{self.bonus_speed} điểm!"
        )


class Dragon(Pet, Mount):
    """
    Rồng.
    Kế thừa Pet và Mount.
    """

    def __init__(
        self,
        name,
        bonus_atk,
        bonus_speed,
        level=1,
    ):
        super().__init__(
            name=name,
            level=level,
            bonus_atk=bonus_atk,
            bonus_speed=bonus_speed,
        )

    def unleash_skill(self):
        print(f">> {self.name} thị uy:")

        Pet.unleash_skill(self)
        Mount.unleash_skill(self)
class CompanionManager:
    """
    Quản lý danh sách sinh vật đồng hành.
    """

    def __init__(self, companions):
        self.active_companions = companions

    def display_companions(self):
        """
        Hiển thị danh sách sinh vật.
        """

        print("\n===== ĐỘI HÌNH SINH VẬT =====")

        if not self.active_companions:
            print("Hiện chưa có sinh vật nào.")
            return

        for index, companion in enumerate(self.active_companions, start=1):

            if isinstance(companion, Dragon):

                print(
                    f"{index}. [Dragon] "
                    f"{companion.name}"
                    f" | Cấp: {companion.level}"
                    f" | Atk: +{companion.bonus_atk}"
                    f" | Speed: +{companion.bonus_speed}"
                )

            elif isinstance(companion, Pet):

                print(
                    f"{index}. [Pet] "
                    f"{companion.name}"
                    f" | Cấp: {companion.level}"
                    f" | Atk: +{companion.bonus_atk}"
                )

            elif isinstance(companion, Mount):

                print(
                    f"{index}. [Mount] "
                    f"{companion.name}"
                    f" | Cấp: {companion.level}"
                    f" | Speed: +{companion.bonus_speed}"
                )

    def summon_pet(self):
        """
        Triệu hồi Pet.
        """

        print("\n--- TRIỆU HỒI PET ---")

        name = input("Tên thú cưng: ").strip()

        try:
            atk = int(input("Bonus Atk: "))

            if atk <= 0:
                print("Giá trị phải lớn hơn 0!")
                return

        except ValueError:
            print("Vui lòng nhập số.")
            return

        pet = Pet(
            name=name,
            bonus_atk=atk,
        )

        self.active_companions.append(pet)

        print(">> Triệu hồi Pet thành công!")

    def summon_mount(self):
        """
        Triệu hồi Mount.
        """

        print("\n--- TRIỆU HỒI MOUNT ---")

        name = input("Tên thú cưỡi: ").strip()

        try:
            speed = int(input("Bonus Speed: "))

            if speed <= 0:
                print("Giá trị phải lớn hơn 0!")
                return

        except ValueError:
            print("Vui lòng nhập số.")
            return

        mount = Mount(
            name=name,
            bonus_speed=speed,
        )

        self.active_companions.append(mount)

        print(">> Triệu hồi Mount thành công!")

    def summon_dragon(self):
        """
        Triệu hồi Dragon.
        """

        print("\n--- TRIỆU HỒI RỒNG ---")

        name = input("Tên rồng: ").strip()

        try:

            atk = int(input("Bonus Atk: "))
            speed = int(input("Bonus Speed: "))

            if atk <= 0 or speed <= 0:
                print("Giá trị phải lớn hơn 0!")
                return

        except ValueError:
            print("Vui lòng nhập số.")
            return

        dragon = Dragon(
            name=name,
            bonus_atk=atk,
            bonus_speed=speed,
        )

        self.active_companions.append(dragon)

        print(">> Triệu hồi Dragon thành công!")

    def breed_companion(self):
        """
        Lai tạo sinh vật.
        """

        print("\n===== LAI TẠO SINH VẬT =====")

        if len(self.active_companions) < 2:
            print("Cần ít nhất 2 sinh vật.")
            return

        self.display_companions()

        try:

            first = int(input("\nChọn sinh vật thứ nhất: ")) - 1
            second = int(input("Chọn sinh vật thứ hai: ")) - 1

            obj1 = self.active_companions[first]
            obj2 = self.active_companions[second]

            new_companion = obj1 + obj2

            self.active_companions.append(new_companion)

            print("\n>> Lai tạo thành công!")

            if isinstance(new_companion, Dragon):

                print(
                    f"{new_companion.name}"
                    f" | Cấp {new_companion.level}"
                    f" | Atk {new_companion.bonus_atk}"
                    f" | Speed {new_companion.bonus_speed}"
                )

            elif isinstance(new_companion, Pet):

                print(
                    f"{new_companion.name}"
                    f" | Cấp {new_companion.level}"
                    f" | Atk {new_companion.bonus_atk}"
                )

            else:

                print(
                    f"{new_companion.name}"
                    f" | Cấp {new_companion.level}"
                    f" | Speed {new_companion.bonus_speed}"
                )

        except IndexError:
            print("Sinh vật không tồn tại.")

        except TypeError as e:
            print(e)

        except ValueError:
            print("Vui lòng nhập số.")

    def battle(self):
        """
        Xuất chiến.
        """

        print("\n===== XUẤT CHIẾN =====")

        if not self.active_companions:
            print("Không có sinh vật nào.")
            return

        for companion in self.active_companions:
            companion.unleash_skill()
def main():
    """
    Hàm chính của chương trình.
    """

    manager = CompanionManager(active_companions)

    while True:

        print("\n========== RIKKEI RPG - COMPANION SYSTEM ==========")
        print("1. Xem đội hình sinh vật")
        print("2. Triệu hồi Pet")
        print("3. Triệu hồi Mount")
        print("4. Triệu hồi Dragon")
        print("5. Lai tạo sinh vật")
        print("6. Xuất chiến")
        print("7. Thoát")

        choice = input("\nChọn chức năng (1-7): ").strip()

        if choice == "1":
            manager.display_companions()

        elif choice == "2":
            manager.summon_pet()

        elif choice == "3":
            manager.summon_mount()

        elif choice == "4":
            manager.summon_dragon()

        elif choice == "5":
            manager.breed_companion()

        elif choice == "6":
            manager.battle()

        elif choice == "7":
            print("\nCảm ơn bạn đã chơi Rikkei RPG!")
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()