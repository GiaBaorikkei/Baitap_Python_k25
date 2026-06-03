total_price = float(input("Nhập tổng giá trị đơn hàng ban đầu: "))
if total_price >= 500000:
    discount = total_price * 0.1
    final_price = total_price - discount
    print(f"Số tiền được giảm giá: {discount} VND")
    print(f"Số tiền khách hàng phải trả: {final_price} VND")
else:
    print("Đơn hàng không đủ điều kiện để được giảm giá. Khách hàng phải trả:", total_price, "VND")
    
