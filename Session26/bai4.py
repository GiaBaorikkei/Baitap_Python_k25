from abc import ABC, abstractmethod


class Equipment(ABC):
    """
    Lớp trừu tượng đại diện cho một trang bị.
    """
    @abstractmethod
    def calculate_total_damage(self):
        """
        Tính sát thương tổng của trang bị.
        """
        pass

class Weapon(Equipment):
    """
    Đại diện cho vũ khí vật lý.
    """

    def __init__(self, name, base_damage, upgrade_level=0):
        self.name = name.title()
        self.base_damage = base_damage
        self.upgrade_level = upgrade_level

    def calculate_total_damage(self):
        """
        Sát thương = base_damage + upgrade_level * 10
        """
        return self.base_damage + self.upgrade_level * 10

    def __gt__(self, other):
        """
        So sánh sức mạnh của hai trang bị.
        """

        if not isinstance(other, Equipment):
            raise TypeError("Chỉ có thể so sánh giữa các trang bị!")

        return (
            self.calculate_total_damage()
            >
            other.calculate_total_damage()
        )

    def __add__(self, other):
        """
        Dung hợp hai vũ khí.
        """

        if not isinstance(other, Equipment):
            raise TypeError("Chỉ có thể dung hợp giữa các trang bị!")

        new_name = f"Fusion({self.name} + {other.name})"

        new_damage = (
            self.base_damage
            + other.base_damage
        )

        new_upgrade = (
            self.upgrade_level
            + other.upgrade_level
        )

        return Weapon(
            new_name,
            new_damage,
            new_upgrade,
        )


class MagicMixin:
    """
    Mixin bổ sung thuộc tính phép thuật.
    """

    def __init__(self, magic_power):
        self.magic_power = magic_power

    def cast_glow(self):
        print(f"{self.name} phát ra ánh sáng huyền bí!")


class MagicSword(Weapon, MagicMixin):
    """
    Kiếm ma thuật.
    Kế thừa đa cấp:
        Weapon
        MagicMixin
    """

    def __init__(
        self,
        name,
        base_damage,
        upgrade_level,
        magic_power,
    ):

        Weapon.__init__(
            self,
            name,
            base_damage,
            upgrade_level,
        )

        MagicMixin.__init__(
            self,
            magic_power,
        )

    def calculate_total_damage(self):
        """
        Tổng sát thương =
        base_damage
        + upgrade_level * 10
        + magic_power
        """

        return (
            self.base_damage
            + self.upgrade_level * 10
            + self.magic_power
        )
inventory = []

class BlacksmithManager:
    """
    Quản lý kho vũ khí.
    """

    def __init__(self, inventory):
        self.inventory = inventory

    def display_inventory(self):
        """
        Hiển thị kho vũ khí.
        """

        print("\n--- KHO VŨ KHÍ CỦA NGƯỜI CHƠI ---")

        if not self.inventory:
            print("Kho vũ khí hiện đang trống.")
            print("Vui lòng rèn vũ khí bằng Chức năng 2 hoặc 3.")
            return

        print(
            f"{'STT':<6}"
            f"{'Tên vũ khí':<30}"
            f"{'Loại':<15}"
            f"{'Cấp':<8}"
            f"{'Sát thương'}"
        )

        print("-" * 75)

        for index, item in enumerate(self.inventory, start=1):

            weapon_type = type(item).__name__

            print(
                f"{index:<6}"
                f"{item.name:<30}"
                f"{weapon_type:<15}"
                f"{item.upgrade_level:<8}"
                f"{item.calculate_total_damage()}"
            )

    def forge_weapon(self):
        """
        Tạo Weapon.
        """

        print("\n--- RÈN VŨ KHÍ VẬT LÝ ---")

        name = input("Nhập tên vũ khí: ").strip().title()

        try:
            damage = int(input("Nhập sát thương gốc: "))

            if damage <= 0:
                print("Giá trị phải lớn hơn 0!")
                return

            level = int(input("Nhập cấp cường hóa: "))

            if level <= 0:
                print("Giá trị phải lớn hơn 0!")
                return

        except ValueError:
            print("Vui lòng nhập số!")
            return

        weapon = Weapon(
            name,
            damage,
            level,
        )

        self.inventory.append(weapon)

        print("\n>> Rèn vũ khí vật lý thành công!")
        print(f"Tên: {weapon.name}")
        print("Loại: Weapon")
        print(f"Cấp: {weapon.upgrade_level}")
        print(
            f"Sát thương tổng: {weapon.calculate_total_damage()}"
        )

    def forge_magic_sword(self):
        """
        Tạo MagicSword.
        """

        print("\n--- RÈN KIẾM MA THUẬT ---")

        name = input("Nhập tên kiếm: ").strip().title()

        try:

            damage = int(input("Nhập sát thương gốc: "))

            if damage <= 0:
                print("Giá trị phải lớn hơn 0!")
                return

            level = int(input("Nhập cấp cường hóa: "))

            if level <= 0:
                print("Giá trị phải lớn hơn 0!")
                return

            magic = int(
                input("Nhập sức mạnh phép thuật: ")
            )

            if magic <= 0:
                print("Giá trị phải lớn hơn 0!")
                return

        except ValueError:
            print("Vui lòng nhập số!")
            return

        sword = MagicSword(
            name,
            damage,
            level,
            magic,
        )

        self.inventory.append(sword)

        print("\n>> Rèn kiếm ma thuật thành công!")

        print(f"Tên: {sword.name}")
        print("Loại: MagicSword")
        print(f"Cấp: {sword.upgrade_level}")
        print(f"Sát thương gốc: {sword.base_damage}")
        print(f"Sức mạnh phép: {sword.magic_power}")
        print(
            f"Sát thương tổng: {sword.calculate_total_damage()}"
        )

    def compare_weapon(self):
        """
        So sánh hai vũ khí đầu tiên.
        """

        print("\n--- THẨM ĐỊNH VŨ KHÍ ---")

        if len(self.inventory) < 2:
            print(
                "Cần ít nhất 2 vũ khí trong kho để thẩm định!"
            )
            return

        first = self.inventory[0]
        second = self.inventory[1]

        print(
            f"\nVũ khí thứ nhất:"
            f"\n{first.name}"
            f" | Loại: {type(first).__name__}"
            f" | Sát thương: {first.calculate_total_damage()}"
        )

        print(
            f"\nVũ khí thứ hai:"
            f"\n{second.name}"
            f" | Loại: {type(second).__name__}"
            f" | Sát thương: {second.calculate_total_damage()}"
        )

        if first > second:
            print(
                f"\nKết quả: {first.name} mạnh hơn {second.name}."
            )

        elif second > first:
            print(
                f"\nKết quả: {second.name} mạnh hơn {first.name}."
            )

        else:
            print("\nKết quả: Hai vũ khí ngang sức.")

    def fusion_weapon(self):
        """
        Dung hợp hai vũ khí đầu tiên.
        """

        print("\n--- DUNG HỢP VŨ KHÍ ---")

        if len(self.inventory) < 2:
            print(
                "Cần ít nhất 2 vũ khí trong kho để dung hợp!"
            )
            return

        first = self.inventory[0]
        second = self.inventory[1]

        print("Đang dung hợp 2 vũ khí đầu tiên...\n")

        print(
            f"Vũ khí 1:"
            f" {first.name}"
            f" | Cấp: {first.upgrade_level}"
            f" | Base Damage: {first.base_damage}"
        )

        print(
            f"Vũ khí 2:"
            f" {second.name}"
            f" | Cấp: {second.upgrade_level}"
            f" | Base Damage: {second.base_damage}"
        )

        new_weapon = first + second

        self.inventory.pop(0)
        self.inventory.pop(0)

        self.inventory.append(new_weapon)

        print("\n>> Dung hợp thành công!")

        print(f"Đã xóa: {first.name}")
        print(f"Đã xóa: {second.name}")

        print()

        print(f"Vũ khí mới: {new_weapon.name}")
        print("Loại: Weapon")
        print(
            f"Cấp cường hóa: {new_weapon.upgrade_level}"
        )
        print(
            f"Sát thương tổng: {new_weapon.calculate_total_damage()}"
        )
def main():
    """
    Hàm chính của chương trình.
    """

    manager = BlacksmithManager(inventory)

    while True:

        print("\n===== LÒ RÈN VŨ KHÍ RIKKEI STUDIOS =====")
        print("1. Xem kho vũ khí")
        print("2. Rèn Vũ khí Vật lý")
        print("3. Rèn Kiếm Ma Thuật")
        print("4. Thẩm định vũ khí")
        print("5. Dung hợp vũ khí")
        print("6. Thoát")
        print("=" * 40)

        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == "1":
            manager.display_inventory()

        elif choice == "2":
            manager.forge_weapon()

        elif choice == "3":
            manager.forge_magic_sword()

        elif choice == "4":
            manager.compare_weapon()

        elif choice == "5":
            manager.fusion_weapon()

        elif choice == "6":
            print("\nThoát Lò Rèn. Hẹn gặp lại Anh hùng!")
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()