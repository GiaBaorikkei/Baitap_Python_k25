blood_inventory = [
    "BL001-Nguyen Van A-O+-250-31/12/2026",
    "BL002-Tran Thi B-A--350-15/11/2026",
    "BL003-Le Van C-AB+-250-20/10/2026"
]


# Tìm vị trí túi máu theo mã
def find_blood_index(inventory, blood_id):
    blood_id = blood_id.strip().upper()

    for i in range(len(inventory)):
        if inventory[i].startswith(blood_id + "-"):
            return i

    return -1


# Hiển thị danh sách kho máu
def display_inventory(inventory):
    if len(inventory) == 0:
        print("Kho máu hiện chưa có túi máu nào.")
        return

    print("\n--- DANH SÁCH KHO MÁU ---")
    print("Mã Túi | Người Hiến       | Nhóm Máu | Thể Tích | Ngày Hết Hạn")
    print("--------------------------------------------------------------")

    total_volume = 0

    for item in inventory:
        parts = item.split("-")

        blood_id = parts[0]
        donor = parts[1]

        # Xử lý nhóm máu có dấu -
        if parts[3].isdigit():
            blood_group = parts[2]
            volume = parts[3]
            expiry = parts[4]
        else:
            blood_group = parts[2] + "-"
            volume = parts[4]
            expiry = parts[5]

        total_volume += int(volume)

        print(
            f"{blood_id:<6} | "
            f"{donor:<16} | "
            f"{blood_group:<8} | "
            f"{volume} ml".ljust(8) + " | "
            f"{expiry}"
        )

    print("--------------------------------------------------------------")
    print(f"Tổng thể tích máu trong kho: {total_volume} ml.")


# Thêm túi máu mới
def add_blood_bag(inventory):
    print("\n--- NHẬP TÚI MÁU MỚI ---")

    blood_id = input("Nhập mã túi máu mới: ").strip().upper()

    if len(blood_id) == 0:
        print("\nLỗi: Mã túi máu không được để trống!")
        return

    if find_blood_index(inventory, blood_id) != -1:
        print(f"\nLỗi: Mã túi máu {blood_id} đã tồn tại! Vui lòng nhập mã khác.")
        return

    donor = input("Nhập tên người hiến: ").strip().title()

    if len(donor) == 0:
        print("\nLỗi: Tên người hiến không được để trống!")
        return

    blood_group = input("Nhập nhóm máu: ").strip().upper()

    volume = input("Nhập thể tích (ml): ").strip()

    if not volume.isdigit() or int(volume) <= 0:
        print("\nLỗi: Thể tích phải là số nguyên lớn hơn 0!")
        return

    expiry = input("Nhập ngày hết hạn (DD/MM/YYYY): ").strip()

    new_bag = "-".join([
        blood_id,
        donor,
        blood_group,
        volume,
        expiry
    ])

    inventory.append(new_bag)

    print(f"\nThành công: Đã nhập túi máu {blood_id} vào kho!")
    print("\nDữ liệu đã lưu:")
    print(new_bag)


# Cập nhật ngày hết hạn
def update_expiry(inventory):
    print("\n--- GIA HẠN / SỬA NGÀY HẾT HẠN ---")

    blood_id = input("Nhập mã túi máu cần cập nhật: ").strip().upper()

    if len(blood_id) == 0:
        print("\nLỗi: Mã túi máu không được để trống!")
        return

    index = find_blood_index(inventory, blood_id)

    if index == -1:
        print(f"\nLỗi: Không tìm thấy túi máu {blood_id} trong kho!")
        return

    new_expiry = input("Nhập ngày hết hạn mới: ").strip()

    # String immutable => split -> sửa -> join
    parts = inventory[index].split("-")

    parts[-1] = new_expiry

    inventory[index] = "-".join(parts)

    print(f"\nThành công: Đã cập nhật ngày hết hạn cho túi máu {blood_id}!")


# Xuất / hủy túi máu
def remove_blood_bag(inventory):
    print("\n--- XUẤT / HỦY TÚI MÁU ---")

    blood_id = input("Nhập mã túi máu cần xuất/hủy: ").strip().upper()

    if len(blood_id) == 0:
        print("\nLỗi: Mã túi máu không được để trống!")
        return

    index = find_blood_index(inventory, blood_id)

    if index == -1:
        print(f"\nLỗi: Không tìm thấy túi máu {blood_id} trong kho!")
        return

    inventory.pop(index)

    print(f"\nThành công: Đã xuất túi máu {blood_id} khỏi kho!")


# Hàm chính
def main():
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ KHO MÁU RIKKEI ===")
        print("1. Xem danh sách túi máu trong kho")
        print("2. Nhập túi máu mới")
        print("3. Gia hạn / Sửa ngày hết hạn")
        print("4. Xuất / Hủy túi máu")
        print("5. Thoát chương trình")
        print("========================================")

        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            display_inventory(blood_inventory)

        elif choice == "2":
            add_blood_bag(blood_inventory)

        elif choice == "3":
            update_expiry(blood_inventory)

        elif choice == "4":
            remove_blood_bag(blood_inventory)

        elif choice == "5":
            print("Cảm ơn bác sĩ đã sử dụng hệ thống. Hẹn gặp lại!")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")


main()