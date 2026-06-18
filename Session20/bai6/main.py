import logging

logging.basicConfig(
    filename="arena_tickets.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

ticket_db = [
    {
        "ticket_id": "T01",
        "buyer_name": "Nguyen Van A",
        "price": 500.0,
        "status": "Booked",
        "seat": ("A", 1)
    },
    {
        "ticket_id": "T02",
        "buyer_name": "Tran Thi B",
        "price": 300.0,
        "status": "Cancelled",
        "seat": ("B", 5)
    },
    {
        "ticket_id": "T03",
        "buyer_name": "Le Van C",
        "price": 500.0,
        "status": "Booked",
        "seat": ("A", 2)
    }
]


def find_ticket(ticket_list, ticket_id):
    """Tìm vị trí vé theo ID."""
    ticket_id = ticket_id.strip().upper()

    for index, ticket in enumerate(ticket_list):
        if ticket["ticket_id"] == ticket_id:
            return index
    return -1


def calculate_total_revenue(ticket_list):
    """Tính tổng doanh thu của các vé Booked."""

    total = 0.0

    for ticket in ticket_list:
        if ticket["status"] == "Booked":
            total += ticket["price"]

    return total


def display_tickets(ticket_list):
    """Hiển thị danh sách vé."""

    if not ticket_list:
        print("Hiện chưa có vé nào trong hệ thống.")
        return

    print("\n--- DANH SÁCH VÉ ---")
    print(f"{'Mã Vé':<8}{'Tên Khách Hàng':<20}{'Giá Vé':<12}{'Chỗ':<10}{'Trạng thái'}")
    print("-" * 70)

    for ticket in ticket_list:
        try:
            seat = ticket["seat"]
            status = ticket["status"]

            if status == "Cancelled":
                status += " [ĐÃ HỦY]"

            print(
                f"{ticket['ticket_id']:<8}"
                f"{ticket['buyer_name']:<20}"
                f"{ticket['price']:<12}"
                f"{seat[0]}-{seat[1]:<8}"
                f"{status}"
            )

        except KeyError as error:
            print("Lỗi: Một vé đang bị thiếu dữ liệu, vui lòng kiểm tra lại.")
            logging.error(f"Missing key while displaying ticket: {error}")

    logging.info("User viewed ticket list.")


def book_ticket(ticket_list):
    """Đặt vé mới."""

    print("\n--- ĐẶT VÉ MỚI ---")

    ticket_id = input("Nhập mã vé: ").strip().upper()

    if find_ticket(ticket_list, ticket_id) != -1:
        print(f"Lỗi: Mã vé {ticket_id} đã tồn tại.")
        logging.warning(f"Duplicate ticket ID entered: {ticket_id}")
        return

    buyer_name = input("Nhập tên khách hàng: ").strip()

    while True:
        try:
            price = float(input("Nhập giá vé: "))

            if price <= 0:
                print("Giá vé phải lớn hơn 0. Vui lòng nhập lại.")
                continue

            break

        except ValueError:
            print("Giá vé phải là số. Vui lòng nhập lại.")
            logging.warning("Invalid price input while booking ticket")

    row = input("Nhập khu vực ghế: ").strip().upper()

    while True:
        try:
            seat_number = int(input("Nhập số ghế: "))

            if seat_number <= 0:
                print("Số ghế phải lớn hơn 0.")
                continue

            break

        except ValueError:
            print("Số ghế phải là số nguyên.")

    new_ticket = {
        "ticket_id": ticket_id,
        "buyer_name": buyer_name,
        "price": price,
        "status": "Booked",
        "seat": (row, seat_number)
    }

    ticket_list.append(new_ticket)

    print(f"\nThành công: Đã đặt vé {ticket_id} cho khách hàng {buyer_name}.")
    logging.info(f"Booked new ticket {ticket_id} for {buyer_name}")


def change_seat(ticket_list):
    """Đổi chỗ ngồi."""

    print("\n--- ĐỔI CHỖ NGỒI ---")

    ticket_id = input("Nhập mã vé cần đổi chỗ: ").strip().upper()

    index = find_ticket(ticket_list, ticket_id)

    if index == -1:
        print(f"Không tìm thấy vé mang mã {ticket_id}.")
        logging.warning(f"Change seat failed - Ticket {ticket_id} not found")
        return

    new_row = input("Nhập khu vực ghế mới: ").strip().upper()

    while True:
        try:
            new_number = int(input("Nhập số ghế mới: "))

            if new_number <= 0:
                print("Số ghế phải lớn hơn 0.")
                continue

            break

        except ValueError:
            print("Số ghế phải là số nguyên. Vui lòng nhập lại.")

    ticket_list[index]["seat"] = (new_row, new_number)

    print(f"Thành công: Đã đổi chỗ vé {ticket_id} sang {new_row}-{new_number}.")
    logging.info(f"Seat changed for ticket {ticket_id} to {new_row}-{new_number}")


def cancel_ticket(ticket_list):
    """Hủy vé."""

    print("\n--- HỦY VÉ ---")

    ticket_id = input("Nhập mã vé cần hủy: ").strip().upper()

    index = find_ticket(ticket_list, ticket_id)

    if index == -1:
        print(f"Không tìm thấy vé mang mã {ticket_id}.")
        logging.warning(f"Cancel ticket failed - Ticket {ticket_id} not found")
        return

    if ticket_list[index]["status"] == "Cancelled":
        print(f"Vé {ticket_id} đã ở trạng thái Cancelled trước đó.")
        return

    ticket_list[index]["status"] = "Cancelled"

    print(f"Thành công: Vé {ticket_id} đã được hủy.")
    logging.warning(f"Ticket {ticket_id} has been cancelled.")


def revenue_report(ticket_list):
    """Báo cáo doanh thu."""

    print("\n--- BÁO CÁO DOANH THU ---")

    try:
        booked = 0
        cancelled = 0

        for ticket in ticket_list:
            if ticket["status"] == "Booked":
                booked += 1
            else:
                cancelled += 1

        total = calculate_total_revenue(ticket_list)

        print(f"Tổng số vé đã đặt: {booked}")
        print(f"Tổng số vé đã hủy: {cancelled}")
        print(f"Tổng doanh thu hợp lệ: {total}")

        logging.info(f"Revenue report generated. Total: {total}")

    except KeyError as error:
        print("Lỗi: Một vé đang bị thiếu dữ liệu doanh thu.")
        logging.error(f"Missing key while calculating revenue: {error}")


def main():
    """Chương trình chính."""

    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ VÉ RIKKEI ESPORTS ===")
        print("1. Xem danh sách vé đã bán")
        print("2. Đặt vé mới")
        print("3. Đổi chỗ ngồi")
        print("4. Hủy vé")
        print("5. Báo cáo doanh thu")
        print("6. Thoát chương trình")

        choice = input("Chọn chức năng (1-6): ")

        if choice == "1":
            display_tickets(ticket_db)

        elif choice == "2":
            book_ticket(ticket_db)

        elif choice == "3":
            change_seat(ticket_db)

        elif choice == "4":
            cancel_ticket(ticket_db)

        elif choice == "5":
            revenue_report(ticket_db)

        elif choice == "6":
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý vé Rikkei Esports.")
            logging.info("Ticket management system closed.")
            break

        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()