def get_status(hp):
    if hp <= 0:
        return "Đã gục ngã"
    elif hp < 50:
        return "Nguy hiểm"
    elif hp < 100:
        return "Ổn định"
    return "Sung sức"


def display_players(records):
    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    print("\n--- DANH SÁCH NGƯỜI CHƠI ---")
    for i, p in enumerate(records, 1):
        print(
            f"{i}. Mã: {p['player_id']} | Tên: {p['name']} | "
            f"HP: {p['hp']} | Mana: {p['mana']} | Gold: {p['gold']} | "
            f"Level: {p['level']} | Trạng thái: {get_status(p['hp'])}"
        )
    print("------------------------------")


def show_leaderboard(records):
    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    sorted_list = sorted(
        records,
        key=lambda x: (x["level"], x["gold"], x["hp"]),
        reverse=True
    )

    print("\n--- BẢNG XẾP HẠNG NGƯỜI CHƠI ---")
    for i, p in enumerate(sorted_list, 1):
        print(f"{i}. {p['name']} | Level: {p['level']} | Gold: {p['gold']} | HP: {p['hp']}")
    print("--------------------------------")