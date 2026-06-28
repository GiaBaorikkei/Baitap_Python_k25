from abc import ABC, abstractmethod


class Champion(ABC):
    """
    Lớp trừu tượng đại diện cho một quân cờ trong game.
    """

    def __init__(self, champion_id, name, base_hp, base_atk):
        """
        Khởi tạo thông tin cơ bản của quân cờ.
        Nếu HP hoặc ATK <= 0 thì mặc định bằng 100.
        """
        self.champion_id = champion_id
        self.name = name
        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self):
        """
        Tính sát thương kỹ năng.
        Bắt buộc lớp con phải cài đặt.
        """
        pass

    def get_combat_power(self):
        """
        Tính chiến lực của quân cờ.
        """
        return self.base_hp + self.calculate_skill_damage() * 1.5

    def __add__(self, other):
        """
        Nạp chồng toán tử +.

        Champion + Champion
        Champion + int
        Champion + float
        """

        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()

        elif isinstance(other, (int, float)):
            return self.get_combat_power() + other

        return NotImplemented

    def __radd__(self, other):
        """
        Hỗ trợ hàm sum().
        """

        if other == 0:
            return self.get_combat_power()

        return self.__add__(other)

    def __gt__(self, other):
        """
        So sánh chiến lực hai quân cờ.
        """

        if isinstance(other, Champion):
            return self.get_combat_power() > other.get_combat_power()

        return NotImplemented


class Warrior(Champion):
    """
    Lớp Warrior.
    """

    def __init__(
        self,
        champion_id,
        name,
        base_hp,
        base_atk,
        shield_bonus,
    ):
        super().__init__(
            champion_id,
            name,
            base_hp,
            base_atk,
        )

        self.shield_bonus = shield_bonus

    def calculate_skill_damage(self):
        """
        Warrior:
        base_atk * 2 + shield_bonus
        """

        return self.base_atk * 2 + self.shield_bonus


class Mage(Champion):
    """
    Lớp Mage.
    """

    def __init__(
        self,
        champion_id,
        name,
        base_hp,
        base_atk,
        ability_power,
    ):
        super().__init__(
            champion_id,
            name,
            base_hp,
            base_atk,
        )

        self.ability_power = ability_power

    def calculate_skill_damage(self):
        """
        Mage:
        base_atk * ability_power
        """

        return self.base_atk * self.ability_power
champion_pool = [
    Warrior(
        "WAR01",
        "Rikkei Knight",
        1200,
        300,
        150,
    ),
    Warrior(
        "WAR02",
        "Steel Guardian",
        1500,
        250,
        200,
    ),
    Mage(
        "MAG01",
        "Rikkei Wizard",
        800,
        500,
        2,
    )
]
class ChampionManager:
    """
    Quản lý danh sách Champion trong game.
    """

    def __init__(self, champion_pool):
        """
        Khởi tạo danh sách quân cờ.
        """
        self.champion_pool = champion_pool

    def find_champion(self, champion_id):
        """
        Tìm quân cờ theo mã.
        Trả về đối tượng Champion nếu tìm thấy, ngược lại trả về None.
        """
        for champion in self.champion_pool:
            if champion.champion_id.upper() == champion_id.upper():
                return champion
        return None

    def display_champions(self):
        """
        Hiển thị danh sách quân cờ.
        """
        print("\n--- DANH SÁCH QUÂN CỜ TRONG BỂ TƯỚNG ---")

        print(
            f"{'Mã':<8}"
            f"{'Tên tướng':<22}"
            f"{'Hệ':<12}"
            f"{'HP':<8}"
            f"{'ATK':<8}"
            f"{'Chỉ số riêng':<20}"
            f"{'Chiến lực'}"
        )

        print("-" * 95)

        for champion in self.champion_pool:

            if isinstance(champion, Warrior):
                role = "Warrior"
                special = f"Armor: {champion.shield_bonus}"

            elif isinstance(champion, Mage):
                role = "Mage"
                special = f"AP: {champion.ability_power}"

            else:
                role = "Unknown"
                special = ""

            print(
                f"{champion.champion_id:<8}"
                f"{champion.name:<22}"
                f"{role:<12}"
                f"{champion.base_hp:<8}"
                f"{champion.base_atk:<8}"
                f"{special:<20}"
                f"{champion.get_combat_power():.1f}"
            )

        print("-" * 95)

    def add_champion(self):
        """
        Thêm quân cờ mới.
        """

        print("\n1. Warrior")
        print("2. Mage")

        champion_type = input("Chọn hệ: ").strip()

        champion_id = input("Nhập mã tướng: ").strip().upper()

        if self.find_champion(champion_id):
            print(" Mã tướng đã tồn tại!")
            return

        name = input("Nhập tên tướng: ").strip().title()

        try:
            hp = int(input("Nhập HP: "))
            atk = int(input("Nhập ATK: "))
        except ValueError:
            print("HP và ATK phải là số!")
            return

        if champion_type == "1":

            try:
                armor = int(input("Nhập Armor: "))
            except ValueError:
                print("Armor phải là số!")
                return

            champion = Warrior(
                champion_id,
                name,
                hp,
                atk,
                armor,
            )

        elif champion_type == "2":

            try:
                ap = float(input("Nhập Ability Power: "))
            except ValueError:
                print("Ability Power phải là số!")
                return

            champion = Mage(
                champion_id,
                name,
                hp,
                atk,
                ap,
            )

        else:
            print("Hệ không hợp lệ!")
            return

        self.champion_pool.append(champion)

        print("\nThêm tướng thành công!")
        print(
            f"Mã: {champion.champion_id}"
            f" | Tên: {champion.name}"
            f" | Chiến lực: {champion.get_combat_power():.1f}"
        )

    def compare_champions(self):
        """
        So sánh 2 quân cờ bằng toán tử >.
        """

        print("\n--- SO SÁNH HAI QUÂN CỜ ---")

        id1 = input("Nhập mã thứ nhất: ").strip()
        id2 = input("Nhập mã thứ hai: ").strip()

        champion1 = self.find_champion(id1)
        champion2 = self.find_champion(id2)

        if champion1 is None:
            print(f"Mã tướng {id1} không hợp lệ!")
            return

        if champion2 is None:
            print(f"Mã tướng {id2} không hợp lệ!")
            return

        print()

        print(
            f"{champion1.champion_id} - {champion1.name}"
            f" | Chiến lực: {champion1.get_combat_power():.1f}"
        )

        print(
            f"{champion2.champion_id} - {champion2.name}"
            f" | Chiến lực: {champion2.get_combat_power():.1f}"
        )

        if champion1 > champion2:
            print(
                f"\nKết quả: {champion1.name} mạnh hơn {champion2.name}"
            )
        elif champion2 > champion1:
            print(
                f"\nKết quả: {champion2.name} mạnh hơn {champion1.name}"
            )
        else:
            print("\nHai quân cờ có sức mạnh ngang nhau.")

    def calculate_team_power(self):
        """
        Tính tổng chiến lực đội hình.
        """

        print("\n--- TÍNH TỔNG CHIẾN LỰC ---")

        ids = input(
            "Nhập các mã tướng (phân cách bằng dấu phẩy): "
        ).split(",")

        total = 0

        selected = []

        for champion_id in ids:

            champion_id = champion_id.strip()

            champion = self.find_champion(champion_id)

            if champion is None:
                print(
                    f"Mã tướng {champion_id} không hợp lệ, bỏ qua!"
                )
                continue

            selected.append(champion)

            total += champion

        print()

        for index, champion in enumerate(selected, start=1):
            print(
                f"{index}. "
                f"{champion.champion_id} - {champion.name}"
                f" | Chiến lực: {champion.get_combat_power():.1f}"
            )

        print(f"\nTổng chiến lực đội hình: {total:.1f}")
        
def main():
    manager = ChampionManager(champion_pool)
    while True:

        print("\n========== RIKKEI RPG - AUTO BATTLER ==========")
        print("1. Hiển thị bể tướng")
        print("2. Thêm quân cờ mới")
        print("3. So sánh 2 quân cờ")
        print("4. Tính tổng chiến lực đội hình")
        print("5. Thoát")

        choice = input("\nChọn chức năng (1-5): ").strip()

        if choice == "1":
            manager.display_champions()

        elif choice == "2":
            manager.add_champion()

        elif choice == "3":
            manager.compare_champions()

        elif choice == "4":
            manager.calculate_team_power()

        elif choice == "5":
            print("\nCảm ơn bạn đã sử dụng Rikkei RPG - Auto-Battler Manager!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")


if __name__ == "__main__":
    main()