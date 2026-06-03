tong_dt = 0
count = 0
for i in range(1,8):
    print("Nhập doanh thu ngày thứ nhất:", i)
    doanh_thu = float(input("Nhập doanh thu: "))
    while doanh_thu < 0:
        print("Lỗi: Doanh thu không được âm! Vui lòng nhập lại.")
        doanh_thu = float(input("Nhập doanh thu: "))
    tong_dt += doanh_thu
    
    if doanh_thu >= 5000000:
        count += 1
   
print("Tổng doanh thu trong tuần là: ", tong_dt)
print(f"Doanh thu trung bình mỗi ngày: ", tong_dt/7)
print("Số ngày đạt doanh thu mục tiêu: ", count)