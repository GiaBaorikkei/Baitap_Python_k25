available_seats = 50
flight_revenue = 0.0
BASE_PRICE = 2000.0
MAX_SEATS = 50


def calculate_ticket_cost(quantity, ticket_class):
    if ticket_class == 1:
        price_per_ticket = BASE_PRICE
        class_name = "Economy"
    else:
        price_per_ticket = BASE_PRICE * 1.5
        class_name = "Business"

    subtotal = quantity * price_per_ticket
    service_fee = subtotal * 0.05
    total_payment = subtotal + service_fee

    return total_payment, subtotal, service_fee, class_name


def book_tickets(quantity, total_payment):
    global available_seats
    global flight_revenue

    if quantity > available_seats:
        return False

    available_seats -= quantity
    flight_revenue += total_payment

    return True


def cancel_tickets(quantity):
    global available_seats
    global flight_revenue

    if available_seats + quantity > MAX_SEATS:
        return -1

    refund_amount = quantity * BASE_PRICE * 0.8

    available_seats += quantity
    flight_revenue -= refund_amount

    return refund_amount


def display_flight_status():
    """
    Hiển thị báo cáo tình trạng chuyến bay VN2026:
    - Sức chứa tối đa
    - Ghế đã đặt
    - Ghế trống
    - Tổng doanh thu hiện tại
    """

    booked_seats = MAX_SEATS - available_seats

    print("\n--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print(f"Sức chứa tối đa: {MAX_SEATS}")
    print(f"Ghế đã đặt: {booked_seats}")
    print(f"Ghế trống: {available_seats}")
    print(f"Tổng doanh thu hiện tại: ${flight_revenue}")


while True:
    print("\n============= SKYBOOKING SYSTEM =============")
    print("Chuyến bay: VN2026 | Khởi hành: Hà Nội")
    print("1. Đặt vé máy bay")
    print("2. Hủy vé & Hoàn tiền")
    print("3. Xem tình trạng chuyến bay")
    print("4. Đóng hệ thống")
    print("=============================================")

    choice = input("Chọn chức năng (1-4): ")

    if choice == "1":
        print("\n--- ĐẶT VÉ MÁY BAY ---")

        quantity = int(input("Nhập số lượng vé: "))

        if quantity <= 0:
            print("Số lượng vé không hợp lệ.")
            continue

        ticket_class = int(
            input("Chọn hạng vé (1: Economy, 2: Business): ")
        )

        if ticket_class != 1 and ticket_class != 2:
            print("Hạng vé không hợp lệ.")
            continue

        if quantity > available_seats:
            print(
                f"Rất tiếc, chuyến bay chỉ còn {available_seats} chỗ trống."
            )
            continue

        total_payment, subtotal, service_fee, class_name = (
            calculate_ticket_cost(quantity, ticket_class)
        )

        print("-> Xác nhận đặt chỗ:")
        print(f"Số lượng: {quantity} | Hạng: {class_name}")
        print(f"Tạm tính: ${subtotal}")
        print(f"Phí dịch vụ (5%): ${service_fee}")
        print(f"Tổng thanh toán: ${total_payment}")

        if book_tickets(quantity, total_payment):
            print(
                f"Đặt vé thành công! Ghế trống còn lại: {available_seats}"
            )

    elif choice == "2":
        print("\n--- HỦY VÉ & HOÀN TIỀN ---")

        quantity = int(input("Nhập số lượng vé muốn hủy: "))

        if quantity <= 0:
            print("Số lượng vé không hợp lệ.")
            continue

        refund = cancel_tickets(quantity)

        if refund == -1:
            print(
                "Lỗi: Số lượng vé hủy vượt quá số vé đã bán ra."
            )
        else:
            print(
                f"Hủy vé thành công. Hệ thống đã hoàn lại: ${refund} (80% giá cơ bản)."
            )
            print(f"Ghế trống hiện tại: {available_seats}")

    elif choice == "3":
        display_flight_status()

    elif choice == "4":
        print("Đóng hệ thống. Cảm ơn bạn đã sử dụng SkyBooking!")
        break

    else:
        print("Lựa chọn không hợp lệ.")