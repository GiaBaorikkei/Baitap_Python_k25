import random

name = str(input("Nhập tên của bệnh nhân: "))
sex = str(input("Nhập giới tính của bệnh nhân: "))
age = int(input("Nhập năm sinh của bệnh nhân: "))
phone = str(input("Nhập số điện thoại của bệnh nhân: "))
email = str(input("Nhập email của bệnh nhân: "))
tt = str(input("Nhập tình trạng bệnh của bệnh nhân: "))
price = float(input("Nhập chi phí điều trị của bệnh nhân: "))

so_ngau_nhien = random.randint(1, 100)
ma_benh_nhan = "BN" + str(age) + str(so_ngau_nhien) 

print("\n" + "=" * 50)
print("           THẺ THÔNG TIN BỆNH NHÂN")
print("=" * 50)

print(f"Mã bệnh nhân      : {ma_benh_nhan}")
print(f"Tên bệnh nhân     : {name}")
print(f"Giới tính         : {sex}")
print(f"Năm sinh          : {age}")
print(f"Số điện thoại     : {phone}")
print(f"Email             : {email}")
print(f"Triệu chứng       : {tt}")
print(f"Chi phí khám      : {price:,.2f} VNĐ")
