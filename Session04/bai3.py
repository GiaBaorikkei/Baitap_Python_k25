so_hoa_don = int(input("Nhập tổng số lượng hóa đơn: "))

max_bill = 0
min_bill = 0

for i in range(1, so_hoa_don + 1):
    gia_tri = float(input(f"Nhập giá trị hóa đơn thứ {i}: "))

    if max_bill is 0 or gia_tri > max_bill:
        max_bill = gia_tri

    if min_bill is 0 or gia_tri < min_bill:
        min_bill = gia_tri

print("\n===== KẾT QUẢ =====")
print("Giá trị lớn nhất:", max_bill)
print("Giá trị bé nhất:", min_bill)