import logging

# ==========================
# Logging
# ==========================

logging.basicConfig(
    filename="fantasy_league.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ==========================
# Data
# ==========================

players = [
    {
        "player_id": "T101",
        "name": "Faker",
        "market_value": 5000,
        "fan_tokens": 1500,
        "match_points": 0,
        "form_multiplier": 1.0
    },
    {
        "player_id": "GEN01",
        "name": "Chovy",
        "market_value": 4800,
        "fan_tokens": 800,
        "match_points": 500,
        "form_multiplier": 1.2
    },
    {
        "player_id": "DRX01",
        "name": "Deft",
        "market_value": 3000,
        "fan_tokens": 0,
        "match_points": 0,
        "form_multiplier": 0.8
    }
]

# ==========================
# Helper Functions
# ==========================


def find_player_by_id(players: list, player_id: str) -> int:
    """
    Tìm vị trí tuyển thủ theo ID.

    Args:
        players (list): Danh sách tuyển thủ.
        player_id (str): Mã tuyển thủ.

    Returns:
        int: Index của tuyển thủ, -1 nếu không tìm thấy.
    """

    for index, player in enumerate(players):
        if player.get("player_id", "").upper() == player_id:
            return index

    return -1


def get_investment_status(fan_tokens: int) -> str:
    """
    Xác định trạng thái đầu tư.
    """

    if fan_tokens == 0:
        return "Chưa có người đầu tư"

    if fan_tokens <= 1000:
        return "Đang thu hút"

    return "Tuyển thủ Hot"


def calc_actual_withdrawal(withdraw_amount: int) -> float:
    """
    Tính số token thực nhận sau khi trừ 10%.

    Args:
        withdraw_amount (int)

    Returns:
        float
    """

    if withdraw_amount < 0:
        raise ValueError("Withdraw amount cannot be negative.")

    return withdraw_amount * 0.9


# ==========================
# Feature 1
# ==========================

def display_market(players: list) -> None:
    """
    Hiển thị sàn giao dịch tuyển thủ.
    """

    print("\n--- SÀN GIAO DỊCH TUYỂN THỦ ---")

    if not players:
        print("Sàn giao dịch hiện chưa có tuyển thủ nào.")
        return

    print(
        f"{'ID':<10}"
        f"{'Tên':<15}"
        f"{'Giá trị':<15}"
        f"{'Fan Token':<15}"
        f"{'Điểm':<12}"
        f"{'Hệ số':<10}"
        f"Trạng thái"
    )

    print("-" * 95)

    for player in players:

        fan_tokens = player.get("fan_tokens", 0)

        status = get_investment_status(fan_tokens)

        print(
            f"{player.get('player_id', 'Unknown'):<10}"
            f"{player.get('name', 'Unknown'):<15}"
            f"{player.get('market_value', 0):<15,}"
            f"{fan_tokens:<15,}"
            f"{player.get('match_points', 0):<12}"
            f"{player.get('form_multiplier', 1.0):<10}"
            f"{status}"
        )

    logging.info("User viewed the player market.")


# ==========================
# Feature 2
# ==========================

def invest_tokens(players: list) -> None:
    """
    Đầu tư Fan Token.
    """

    print("\n--- ĐẦU TƯ FAN TOKEN ---")

    player_id = input("Nhập mã tuyển thủ: ").strip().upper()

    index = find_player_by_id(players, player_id)

    if index == -1:
        print("Không tìm thấy tuyển thủ!")

        logging.warning(
            f"Invest failed - Player {player_id} not found"
        )
        return

    while True:

        try:

            amount = int(input("Nhập số token muốn đầu tư: "))

            if amount <= 0:
                print("Số token phải là số nguyên dương. Vui lòng nhập lại.")

                logging.warning("Invalid token input while investing")
                continue

            players[index]["fan_tokens"] += amount

            print(
                f"\nThành công: Đã đầu tư {amount} token vào tuyển thủ {player_id}."
            )

            print(
                f"Số Fan Token hiện tại của {players[index]['name']}: "
                f"{players[index]['fan_tokens']:,}"
            )

            logging.info(
                f"Invested {amount} tokens into {player_id}"
            )

            return

        except ValueError:

            print("Số token phải là số nguyên dương. Vui lòng nhập lại.")

            logging.warning("Invalid token input while investing")
            # ==========================
# Feature 3
# ==========================

def withdraw_tokens(players: list) -> None:
    """
    Rút Fan Token.
    """

    print("\n--- RÚT VỐN FAN TOKEN ---")

    player_id = input("Nhập mã tuyển thủ: ").strip().upper()

    index = find_player_by_id(players, player_id)

    if index == -1:
        print("Không tìm thấy tuyển thủ!")
        logging.warning(f"Withdraw failed - Player {player_id} not found")
        return

    while True:

        try:

            amount = int(input("Nhập số token muốn rút: "))

            if amount <= 0:
                print("Số token phải là số nguyên dương.")
                continue

            current_token = players[index]["fan_tokens"]

            if amount > current_token:

                print(
                    "Không thể rút. "
                    "Số token muốn rút vượt quá số Fan Token hiện có."
                )

                print(
                    f"Fan Token hiện có của "
                    f"{players[index]['name']}: {current_token:,}"
                )

                logging.warning(
                    "Withdraw failed - Amount exceeds current fan tokens"
                )
                return

            actual_receive = calc_actual_withdrawal(amount)

            players[index]["fan_tokens"] -= amount

            print(
                f"\nThành công: Đã rút {amount} token "
                f"khỏi tuyển thủ {player_id}."
            )

            print(f"Phí giao dịch 10%: {amount * 0.1} token")
            print(f"Số token thực nhận về ví: {actual_receive} token")

            print(
                f"Fan Token còn lại của "
                f"{players[index]['name']}: "
                f"{players[index]['fan_tokens']:,}"
            )

            logging.info(
                f"Withdrawn {amount} tokens from "
                f"{player_id}. Actual received: {actual_receive}"
            )

            return

        except ValueError:

            print("Số token phải là số nguyên.")

            logging.warning("Invalid withdraw amount")
# ==========================
# Feature 4
# ==========================

def update_form(players: list) -> None:
    """
    Cập nhật hệ số phong độ.
    """

    print("\n--- CẬP NHẬT HỆ SỐ PHONG ĐỘ ---")

    player_id = input("Nhập mã tuyển thủ: ").strip().upper()

    index = find_player_by_id(players, player_id)

    if index == -1:
        print("Không tìm thấy tuyển thủ!")
        return

    while True:

        try:

            multiplier = float(
                input("Nhập hệ số phong độ mới (0.5 - 2.5): ")
            )

            if multiplier < 0.5 or multiplier > 2.5:

                print(
                    "Hệ số phong độ chỉ được nằm "
                    "trong khoảng 0.5 đến 2.5."
                )

                continue

            players[index]["form_multiplier"] = multiplier

            print(
                f"\nThành công: Đã cập nhật hệ số phong độ "
                f"cho {players[index]['name']}."
            )

            print(f"Hệ số mới: x{multiplier}")

            logging.info(
                f"Updated form multiplier for "
                f"{player_id} to {multiplier}"
            )

            return

        except ValueError:

            print(
                "Hệ số phong độ phải là số thực. "
                "Vui lòng nhập lại."
            )

            logging.warning("Invalid form multiplier input")


# ==========================
# Feature 5
# ==========================

def calculate_match_points(players: list) -> None:
    """
    Chấm điểm sau trận đấu.
    """

    print("\n--- CHẤM ĐIỂM SAU TRẬN ĐẤU ---")

    player_id = input("Nhập mã tuyển thủ: ").strip().upper()

    index = find_player_by_id(players, player_id)

    if index == -1:
        print("Không tìm thấy tuyển thủ!")
        return

    while True:

        try:

            base_points = int(input("Nhập điểm gốc của trận đấu: "))

            if base_points < 0:
                print("Điểm phải lớn hơn hoặc bằng 0.")
                continue

            earned_points = (
                base_points *
                players[index]["form_multiplier"]
            )

            players[index]["match_points"] += earned_points

            print(
                f"\n>> Tuyển thủ {players[index]['name']} "
                f"nhận được {earned_points} điểm "
                f"(Hệ số x{players[index]['form_multiplier']})."
            )

            print(
                f"Tổng điểm: "
                f"{players[index]['match_points']}"
            )

            logging.info(
                f"Added {earned_points} "
                f"match points to {player_id}"
            )

            return

        except ValueError:

            print("Điểm phải là số nguyên.")

            logging.warning("Invalid match point input")


# ==========================
# Main Menu
# ==========================

def main() -> None:
    """
    Hàm chính.
    """

    while True:

        print("\n===== HỆ THỐNG RIKKEI ESPORTS FANTASY =====")
        print("1. Xem Sàn Giao Dịch Tuyển Thủ")
        print("2. Đầu tư Fan Token")
        print("3. Rút vốn (Hoàn trả Token)")
        print("4. Biến động phong độ")
        print("5. Chấm điểm sau trận đấu")
        print("6. Thoát hệ thống")

        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == "1":
            display_market(players)

        elif choice == "2":
            invest_tokens(players)

        elif choice == "3":
            withdraw_tokens(players)

        elif choice == "4":
            update_form(players)

        elif choice == "5":
            calculate_match_points(players)

        elif choice == "6":

            logging.info("Fantasy League application closed.")

            print("\nĐóng hệ thống Rikkei Esports Fantasy.")

            break

        else:

            print("Lựa chọn không hợp lệ.")

            logging.warning("Invalid menu choice selected")


# ==========================
# Run Program
# ==========================

if __name__ == "__main__":
    main()