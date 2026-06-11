inventory_stock = 100
total_revenue = 0.0

def add_stock():
    global inventory_stock
    
    amount = int(input("Nhập số lượng sản phẩm muốn thêm: "))
    
    if amount <= 0:
        print("Dữ liệu nhập vào phải lớn hơn 0.")
        return
    
    inventory_stock += amount
    
    print(f"Đã nhập thành công {amount} đơn hàng vào kho")
    print(f"Tồn kho hiện tại {inventory_stock}")
    return inventory_stock

def process_sale(quantity):
    global inventory_stock
    if quantity > inventory_stock:
        print(f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {total_revenue}.")
        return False
    inventory_stock -= quantity
    return True

def calculate_final_price(quantity, price):
    global total_revenue
    total_price = quantity * price
    vat = total_price * 0.08
    discount = 0
    
    if total_price >= 1000:
        discount = total_price * 0.1
        
    final_total = total_price - discount + vat
    total_revenue += final_total
    
    print("-> Hoá đơn chi tiết:")
    print(f"Số lượng: {quantity} | Đơn giá: {price}")
    print(f"Tạm tính: {total_price}")
    print(f"Giảm giá: {discount}")
    print(f"Thuế VAT (8%): {vat}")
    print(f"Tổng thanh toán thành công: {final_total}")
    print("Đã bán thành công.")
    return final_total

def print_report():
    print("--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: {total_revenue}")
    
def main():
    while True:
        print("===== TECHSTORE MANAGEMENT SYSTEM =====")
        print("1. Nhập thêm hàng vào kho")
        print("2. Bán hàng (tính toán hoá đơn)")
        print("3. Xem báo cáo tổng quan")
        print("4. Thoát chương trình")
        print("=======================================")
        
        choice = input("Chọn chức năng (1-4): ")
        
        if choice == "1":
            add_stock()
        elif choice == "2":
            quantity = int(input("Nhập số lượng mua: "))
            process_sale(quantity)
            price = float(input("Nhập đơn giá ($): "))
            calculate_final_price(quantity, price)
        elif choice == "3":
            print_report()
        elif choice == "4":
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")
main()
            