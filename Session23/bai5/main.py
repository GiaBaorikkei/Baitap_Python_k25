from data.players import player_records
from reports.dungeon_report import display_players, show_leaderboard
from utils.item_utils import open_treasure_chest, buy_item
from utils.battle_utils import fight_monster


def main():
    while True:
        print("""
===== RIKKEI DUNGEON - PYTHON MODULE ADVENTURE =====
1. Hiển thị danh sách người chơi
2. Mở rương báu ngẫu nhiên
3. Mua vật phẩm trong cửa hàng
4. Chiến đấu với quái vật
5. Xem bảng xếp hạng người chơi
6. Thoát chương trình
====================================================
""")

        choice = input("Chọn chức năng (1-6): ")

        if choice == "1":
            display_players(player_records)
        elif choice == "2":
            open_treasure_chest(player_records)
        elif choice == "3":
            buy_item(player_records)
        elif choice == "4":
            fight_monster(player_records)
        elif choice == "5":
            show_leaderboard(player_records)
        elif choice == "6":
            print("Cảm ơn bạn đã tham gia Rikkei Dungeon!")
            break
        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()