print("-- Hệ thống gửi mail thưởng tết --")

for i in range(1,4):
    print("Đang sử lí nhân viên số:", i)
    ngay_cong = int(input("Nhập số ngày công của nhân viên: "))
    if ngay_cong == 0:
        print("Cảnh báo: Nhân viên không có ngày công nào, không được thưởng.")
    else:
        thuong = ngay_cong * 200000
        print(f"Nhân viên số {i} được thưởng: {thuong} VND")