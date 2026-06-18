import logging

# ==========================
# Logging Configuration
# ==========================
logging.basicConfig(
    filename="roster_app.log",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s"
)

# ==========================
# Initial Data
# ==========================

roster = [
    {
        "player_id": "P01",
        "name": "Faker",
        "role": "Mid Lane",
        "salary": 5000.0,
        "status": "Active"
    },
    {
        "player_id": "P02",
        "name": "Oner",
        "role": "Jungle",
        "salary": 3500.0,
        "status": "Active"
    },
    {
        "player_id": "P03",
        "name": "Ruler",
        "role": "ADC",
        "salary": 6000.0,
        "status": "Benched"
    }
]


# ==========================
# Helper Functions
# ==========================

def calculate_actual_pay(player):
    """
    Tính lương thực nhận của tuyển thủ.

    Active  -> 100%
    Benched -> 50%

    Args:
        player (dict)

    Returns:
        float
    """

    salary = player["salary"]

    if player["status"] == "Benched":
        return salary * 0.5

    return salary


def input_salary():
    """
    Nhập mức lương hợp lệ.

    Returns:
        float
    """

    while True:

        try:
            salary = float(input("Nhập mức lương hàng tháng: "))

            if salary <= 0:
                print("Lương phải là số dương. Vui lòng nhập lại.")
                logging.warning(
                    "Failed to sign player - Invalid salary input"
                )
                continue

            return salary

        except ValueError:
            print("Lương phải là số. Vui lòng nhập lại.")
            logging.warning(
                "Failed to sign player - Invalid salary input"
            )


# ==========================
# Feature 1
# ==========================

def display_roster(roster_list):
    """
    Hiển thị danh sách tuyển thủ.

    Args:
        roster_list (list)

    Returns:
        None
    """

    if not roster_list:
        print("\nĐội hình hiện đang trống.")
        return

    print("\n--- ĐỘI HÌNH RIKKEI ESPORTS ---")
    print(
        f"{'ID':<8}"
        f"{'Tên tuyển thủ':<25}"
        f"{'Vị trí':<18}"
        f"{'Lương':<15}"
        f"{'Trạng thái'}"
    )

    print("-" * 85)

    for player in roster_list:

        try:

            status = player.get("status", "Unknown")

            name = player["name"]

            if status == "Benched":
                name += " [DỰ BỊ]"

            print(
                f"{player['player_id']:<8}"
                f"{name:<25}"
                f"{player['role']:<18}"
                f"{player['salary']:<15,.1f}"
                f"{status}"
            )

        except KeyError as error:

            print("Lỗi: Một tuyển thủ đang bị thiếu dữ liệu.")
            logging.error(f"Missing key while displaying roster: {error}")

    logging.info("Coach viewed the team roster.")


# ==========================
# Feature 2
# ==========================

def sign_player(roster_list):
    """
    Chiêu mộ tuyển thủ mới.

    Args:
        roster_list (list)

    Returns:
        None
    """

    print("\n--- CHIÊU MỘ TUYỂN THỦ MỚI ---")

    player_id = input("Nhập mã tuyển thủ: ").strip().upper()

    for player in roster_list:

        if player["player_id"] == player_id:
            print(f"\nLỗi: Mã tuyển thủ {player_id} đã tồn tại.")

            logging.warning(
                f"Failed to sign player - Duplicate player ID {player_id}"
            )
            return

    name = input("Nhập tên tuyển thủ: ").strip().title()

    role = input("Nhập vị trí thi đấu: ").strip().title()

    salary = input_salary()

    new_player = {
        "player_id": player_id,
        "name": name,
        "role": role,
        "salary": salary,
        "status": "Active"
    }

    roster_list.append(new_player)

    print(f"\nThành công: Đã chiêu mộ tuyển thủ {name}.")

    logging.info(
        f"Signed new player {name} with salary {salary}"
    )
    # ==========================
# Feature 3
# ==========================

def update_player_status(roster_list):
    """
    Cập nhật lương hoặc trạng thái tuyển thủ.

    Args:
        roster_list (list)

    Returns:
        None
    """

    print("\n--- CẬP NHẬT LƯƠNG & TRẠNG THÁI THI ĐẤU ---")

    player_id = input("Nhập mã tuyển thủ cần cập nhật: ").strip().upper()

    for player in roster_list:

        if player["player_id"] == player_id:

            print(f"\nTuyển thủ: {player['name']}")
            print(f"Vị trí: {player['role']}")
            print(f"Lương hiện tại: {player['salary']:,.1f}")
            print(f"Trạng thái hiện tại: {player['status']}")

            print("\nBạn muốn cập nhật:")
            print("1. Cập nhật lương")
            print("2. Cập nhật trạng thái thi đấu")

            choice = input("Chọn chức năng cập nhật (1-2): ").strip()

            if choice == "1":

                old_salary = player["salary"]

                while True:

                    try:
                        new_salary = float(input("Nhập mức lương mới: "))

                        if new_salary <= 0:
                            print("Lương phải là số dương. Vui lòng nhập lại.")
                            logging.warning(
                                "Failed to update player - Invalid salary input"
                            )
                            continue

                        player["salary"] = new_salary

                        print(
                            f"\nThành công: Đã cập nhật lương cho tuyển thủ {player_id}."
                        )

                        logging.info(
                            f"Updated player {player_id} salary "
                            f"from {old_salary} to {new_salary}"
                        )
                        return

                    except ValueError:
                        print("Lương phải là số.")
                        logging.warning(
                            "Failed to update player - Invalid salary input"
                        )

            elif choice == "2":

                print("\nChọn trạng thái mới:")
                print("1. Active")
                print("2. Benched")

                status_choice = input("Nhập lựa chọn trạng thái (1-2): ")

                if status_choice == "1":
                    player["status"] = "Active"

                elif status_choice == "2":
                    player["status"] = "Benched"

                else:
                    print("Lựa chọn không hợp lệ.")
                    return

                print(
                    f"\nThành công: Đã cập nhật trạng thái cho tuyển thủ {player_id}."
                )

                logging.info(
                    f"Updated player {player_id} status to {player['status']}"
                )

                return

            else:
                print("Lựa chọn không hợp lệ.")
                return

    print(f"\nKhông tìm thấy tuyển thủ mang mã {player_id}.")

    logging.warning(
        f"Failed to update player - Player ID {player_id} not found"
    )


# ==========================
# Feature 4
# ==========================

def generate_payroll_report(roster_list):
    """
    Báo cáo quỹ lương.

    Args:
        roster_list (list)

    Returns:
        None
    """

    print("\n--- BÁO CÁO QUỸ LƯƠNG HÀNG THÁNG ---")

    if not roster_list:
        print("Đội hình hiện đang trống. Tổng quỹ lương: 0.0")
        return

    print(
        f"{'ID':<8}"
        f"{'Tên tuyển thủ':<18}"
        f"{'Trạng thái':<12}"
        f"{'Lương gốc':<15}"
        f"{'Lương thực nhận'}"
    )

    print("-" * 80)

    total_salary = 0

    for player in roster_list:

        try:

            actual_salary = calculate_actual_pay(player)

            total_salary += actual_salary

            print(
                f"{player['player_id']:<8}"
                f"{player['name']:<18}"
                f"{player['status']:<12}"
                f"{player['salary']:<15,.1f}"
                f"{actual_salary:,.1f}"
            )

        except KeyError as error:

            print("Lỗi: Một tuyển thủ đang bị thiếu dữ liệu.")

            logging.error(
                f"Missing key while generating payroll report: {error}"
            )

    print("-" * 80)
    print(f"Tổng quỹ lương hàng tháng: {total_salary:,.1f}")

    logging.info(
        f"Generated monthly payroll report. Total: {total_salary}"
    )


# ==========================
# Main Menu
# ==========================

def main():
    """
    Hàm chính.
    """

    while True:

        print("\n===== HỆ THỐNG QUẢN LÝ ĐỘI HÌNH RIKKEI ESPORTS =====")
        print("1. Xem đội hình thi đấu hiện tại")
        print("2. Chiêu mộ tuyển thủ mới")
        print("3. Cập nhật lương & Trạng thái thi đấu")
        print("4. Báo cáo quỹ lương hàng tháng")
        print("5. Thoát hệ thống")

        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            display_roster(roster)

        elif choice == "2":
            sign_player(roster)

        elif choice == "3":
            update_player_status(roster)

        elif choice == "4":
            generate_payroll_report(roster)

        elif choice == "5":
            logging.info("Application closed.")
            print("Đã thoát hệ thống.")
            break

        else:
            print("Lựa chọn không hợp lệ.")
            logging.warning("Invalid menu choice selected")


# ==========================
# Run Program
# ==========================

if __name__ == "__main__":
    main()