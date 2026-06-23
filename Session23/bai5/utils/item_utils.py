import random
from utils.player_utils import find_player

rewards = ["Potion", "Iron Sword", "Magic Scroll", "100 Gold", "Mana Stone"]

shop_items = {
    "Potion": 50,
    "Iron Sword": 200,
    "Magic Book": 300,
    "Mana Stone": 150
}


def open_treasure_chest(records):
    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    pid = input("Nhập mã người chơi mở rương: ")
    idx = find_player(records, pid)

    if idx == -1:
        print("Không tìm thấy người chơi!")
        return

    player = records[idx]
    reward = random.choice(rewards)

    print(f">> Người chơi {player['name']} đã mở rương!")
    print(f">> Phần thưởng nhận được: {reward}")

    if reward == "100 Gold":
        player["gold"] += 100
        print(">> Đã cộng 100 vàng!")
    else:
        player["inventory"].append(reward)
        print(f">> Đã thêm {reward} vào túi đồ.")


def buy_item(records):
    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    pid = input("Nhập mã người chơi: ")
    idx = find_player(records, pid)

    if idx == -1:
        print("Không tìm thấy người chơi!")
        return

    item = input("Nhập tên vật phẩm muốn mua: ")

    if item not in shop_items:
        print("Vật phẩm không tồn tại trong cửa hàng!")
        return

    player = records[idx]
    price = shop_items[item]

    if player["gold"] < price:
        print("Không đủ vàng để mua vật phẩm này!")
        return

    player["gold"] -= price
    player["inventory"].append(item)

    print(f">> Mua thành công {item}!")
    print(f">> Số vàng còn lại: {player['gold']}")