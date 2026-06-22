import logging


def show_devices(devices):
    """
    Hiển thị danh sách thiết bị
    """

    if not devices:
        print("\n[INFO] Hệ thống hiện chưa có thiết bị.\n")
        return

    print("\n{:<8}{:<25}{:<15}{:<15}{:<15}{:<15}".format(
        "MÃ TB", "VỊ TRÍ PHÂN XƯỞNG", "CHỈ SỐ CŨ",
        "CHỈ SỐ MỚI", "ĐIỆN TIÊU THỤ", "TRẠNG THÁI"
    ))

    print("-" * 95)

    for device in devices:
        consumption = (
            device["new_index"] - device["old_index"]
        )

        print(
            f"{device['id']:<8}"
            f"{device['location']:<25}"
            f"{device['old_index']:<15}"
            f"{device['new_index']:<15}"
            f"{consumption:<15}"
            f"{device['status']:<15}"
        )


def find_device_by_id(devices, device_id):
    """
    Tìm thiết bị theo ID
    """

    for device in devices:
        if device["id"] == device_id:
            return device

    return None


def input_non_negative_number(message):
    """
    Nhập số >=0
    """

    while True:
        try:
            value = int(input(message))

            if value < 0:
                print("Giá trị phải >=0. Nhập lại.")
                continue

            return value

        except ValueError:
            print("Sai kiểu dữ liệu. Vui lòng nhập số.")


def update_indices(devices):
    """
    Cập nhật chỉ số điện
    """

    device_id = input("Nhập mã thiết bị: ").strip().upper()

    device = find_device_by_id(
        devices,
        device_id
    )

    if device is None:
        print("\n[ERR-E01] Không tìm thấy thiết bị\n")
        return

    old_index = input_non_negative_number(
        "Nhập chỉ số cũ: "
    )

    while True:
        new_index = input_non_negative_number(
            "Nhập chỉ số mới: "
        )

        if new_index < old_index:
            print(
                "[ERR-E02] "
                "Chỉ số mới không được nhỏ hơn chỉ số cũ"
            )
        else:
            break

    device["old_index"] = old_index
    device["new_index"] = new_index

    logging.info(
        f"Cập nhật dữ liệu thiết bị {device_id}"
    )

    print("\nCập nhật thành công!\n")


def activate_alert(devices):
    """
    Kích hoạt cảnh báo quá tải
    """

    device_id = input(
        "Nhập mã thiết bị: "
    ).strip().upper()

    device = find_device_by_id(
        devices,
        device_id
    )

    if device is None:
        print("\n[ERR-E01] Không tìm thấy thiết bị\n")
        return

    if device["status"] == "Overload":
        print("\n[ERR-E04] Thiết bị đã quá tải\n")
        return

    consumption = (
        device["new_index"]
        - device["old_index"]
    )

    if consumption > 5000:

        device["status"] = "Overload"

        logging.warning(
            f"Thiết bị {device_id} quá tải"
        )

        print(
            "\nĐã kích hoạt trạng thái Overload\n"
        )

    else:
        print(
            "\nThiết bị chưa vượt ngưỡng quá tải\n"
        )


def calculate_energy_financials(devices):
    """
    Tính toán tài chính

    return:
    (
        total_consumption,
        discount_percent,
        final_cost
    )
    """

    total_consumption = sum(
        d["new_index"] - d["old_index"]
        for d in devices
    )

    price_per_kwh = 3000

    total_cost = (
        total_consumption
        * price_per_kwh
    )

    discount_percent = 0

    if total_consumption >= 50000:
        discount_percent = 3

    final_cost = (
        total_cost
        * (100 - discount_percent)
        / 100
    )

    return (
        total_consumption,
        discount_percent,
        final_cost
    )


def display_menu():

    print("\n===== SMART ENERGY MONITOR =====")
    print("1. Xem danh sách thiết bị giám sát")
    print("2. Cập nhật chỉ số điện tiêu thụ")
    print("3. Kích hoạt trạng thái cảnh báo quá tải")
    print("4. Tính tổng lượng điện và chi phí năng lượng")
    print("5. Thoát chương trình")
    print("=" * 35)


def main():

    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s - "
            "%(levelname)s - "
            "%(message)s"
        )
    )

    devices = [
        {
            "id": "M01",
            "location": "Mechanical Shop A",
            "old_index": 1200,
            "new_index": 4500,
            "status": "Normal"
        },

        {
            "id": "M02",
            "location": "Assembly Line B",
            "old_index": 2300,
            "new_index": 8500,
            "status": "Overload"
        }
    ]

    while True:

        display_menu()

        try:
            choice = int(
                input(
                    "Nhập lựa chọn: "
                )
            )

            if choice == 1:
                show_devices(
                    devices
                )

            elif choice == 2:
                update_indices(
                    devices
                )

            elif choice == 3:
                activate_alert(
                    devices
                )

            elif choice == 4:

                total, discount, cost = (
                    calculate_energy_financials(
                        devices
                    )
                )

                print("\n===== BÁO CÁO =====")
                print(
                    f"Tổng điện tiêu thụ:"
                    f" {total} kWh"
                )

                print(
                    f"Chiết khấu:"
                    f" {discount}%"
                )

                print(
                    f"Tổng tiền:"
                    f" {cost:,.0f} VND"
                )

            elif choice == 5:
                print(
                    "\nCảm ơn đã sử dụng hệ thống!"
                )

                break

            else:
                print(
                    "Lựa chọn không hợp lệ"
                )

        except ValueError:
            print(
                "Vui lòng nhập số!"
            )


if __name__ == "__main__":
    main()