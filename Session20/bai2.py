# Dữ liệu từ API
player_records = [
    ("Levi", 120, 2500),
    ("SofM", 150),
    ("Optimus", 100, "N/A")
]


# Hàm tính thưởng
def calculate_bonus(matches, mmr):
    return (matches * 10) + (mmr * 0.5)


# Hàm xử lý
def process_bonus(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")

    for record in player_records:
        name = record[0]

        try:
            matches = record[1]
            mmr = record[2]

            mmr = int(mmr)

            bonus = calculate_bonus(matches, mmr)

            print(f"{name}: Nhận được {bonus} RP")

        except IndexError:
            print(f"{name}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue

        except ValueError:
            print(f"{name}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue


# Chạy chương trình
process_bonus(player_records)