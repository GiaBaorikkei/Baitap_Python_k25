# Hàm tính tổng tiền đơn hàng
def calculate_final_price(price, discount, shipping_fee):
    total = price - (price * discount) + shipping_fee
    print("Đã tính xong tổng tiền:", total)
    return total
    # Hàm đang kết thúc tại đây

# Đơn hàng mua áo thun: Giá 100000, giảm giá 10% (0.1), phí ship 15000
# Gọi hàm để tính tiền
order_total = calculate_final_price(100000, 0.1, 15000)

# Hệ thống cộng thêm 5000 phí đóng gói vào tổng tiền đơn hàng
final_payment = order_total + 5000

print("Khách hàng cần thanh toán:", final_payment)