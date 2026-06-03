tong_doanh_thu = 0
tong_hoa_don = 0
hoa_don_lon = 0

while True:
    gia_tri = int(input("Nhập giá trị hóa đơn (VND): "))

    tong_doanh_thu += gia_tri
    tong_hoa_don += 1

    if gia_tri >= 1000000:
        hoa_don_lon += 1

    tiep_tuc = input("Có muốn nhập tiếp không? (C/K): ")

    if tiep_tuc.lower() == "k":
        break
    elif tiep_tuc.lower() == "c":
        continue
    else:
        print("Lựa chọn không hợp lệ!")

if tong_hoa_don > 0:
    ty_le = hoa_don_lon / tong_hoa_don * 100
else:
    ty_le = 0

print("\n===== BÁO CÁO DOANH THU CUỐI NGÀY =====")
print("Tổng doanh thu:", tong_doanh_thu, "VND")
print("Tổng số hóa đơn:", tong_hoa_don)
print("Số hóa đơn lớn:", hoa_don_lon)
print(f"Tỷ lệ hóa đơn lớn: {ty_le}%")