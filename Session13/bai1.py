def check_in():
    global next_id

    # Nhập biển số
    while True:
        plate = input("Nhập biển số: ").strip()

        if plate == "":
            print("ERR-02: Biển số không được để trống.")
            continue

        duplicate = False
        for car in parking_lot:
            if car["plate"] == plate:
                duplicate = True
                break

        if duplicate:
            print("ERR-03: Biển số đã tồn tại.")
        else:
            break

    # Chọn loại xe
    while True:
        try:
            vehicle = int(input("1. Xe máy\n2. Ô tô\nChọn loại xe: "))

            if vehicle == 1:
                vehicle = "Xe máy"
                break
            elif vehicle == 2:
                vehicle = "Ô tô"
                break
            else:
                print("ERR-05: Chỉ được nhập 1 hoặc 2.")

        except ValueError:
            print("ERR-06: Vui lòng nhập số.")

    # Giờ vào
    while True:
        try:
            entry = int(input("Nhập giờ vào: "))
            break
        except ValueError:
            print("ERR-06: Giờ vào phải là số.")

    car = {
        "id": next_id,
        "plate": plate,
        "type": vehicle,
        "entry_time": entry
    }

    parking_lot.append(car)
    next_id += 1

    print("Check-in thành công!")
    
def show_cars():

    if len(parking_lot) == 0:
        print("ERR-07: Bãi xe đang trống.")
        return

    print("-" * 55)
    print(f"{'ID':<5}{'Biển số':<15}{'Loại xe':<15}{'Giờ vào'}")
    print("-" * 55)

    for car in parking_lot:
        print(
            f"{car['id']:<5}"
            f"{car['plate']:<15}"
            f"{car['type']:<15}"
            f"{car['entry_time']}"
        )

    print("-" * 55)
    
def search_car():

    plate = input("Nhập biển số cần tìm: ").strip()

    if plate == "":
        print("ERR-02: Không được để trống.")
        return

    for car in parking_lot:
        if car["plate"] == plate:
            print("\nThông tin xe:")
            print(car)
            return

    print("ERR-04: Không tìm thấy xe.")
    
def check_out():

    plate = input("Nhập biển số: ").strip()

    if plate == "":
        print("ERR-02: Không được để trống.")
        return

    found = None

    for car in parking_lot:
        if car["plate"] == plate:
            found = car
            break

    if found is None:
        print("ERR-04: Không tìm thấy xe.")
        return

    while True:
        try:
            exit_time = int(input("Nhập giờ ra: "))

            if exit_time < found["entry_time"]:
                print("ERR-08: Giờ ra phải lớn hơn hoặc bằng giờ vào.")
            else:
                break

        except ValueError:
            print("ERR-06: Vui lòng nhập số.")

    hours = exit_time - found["entry_time"]

    if found["type"] == "Xe máy":
        fee = hours * 5000
    else:
        fee = hours * 20000

    print("\n===== HÓA ĐƠN =====")
    print("Biển số :", found["plate"])
    print("Loại xe :", found["type"])
    print("Giờ vào :", found["entry_time"])
    print("Giờ ra  :", exit_time)
    print("Số giờ  :", hours)
    print("Phí gửi :", fee, "VNĐ")

    parking_lot.remove(found)

    print("Check-out thành công.")
    
parking_lot = []
next_id = 1


def menu():
    print("\n========== SMART PARKING ==========")
    print("1. Check-in")
    print("2. Danh sách xe")
    print("3. Tìm kiếm xe")
    print("4. Check-out")
    print("5. Thoát")
    print("===================================")
while True:

    menu()

    try:
        choice = int(input("Nhập lựa chọn: "))

    except ValueError:
        print("ERR-01: Lựa chọn không hợp lệ.")
        continue

    if choice == 1:
        check_in()

    elif choice == 2:
        show_cars()

    elif choice == 3:
        search_car()

    elif choice == 4:
        check_out()

    elif choice == 5:
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break

    else:
        print("ERR-01: Lựa chọn không hợp lệ.")