ho_ten = str(input("Nhập họ và tên bệnh nhân: "))
tuoi = int(input("Nhập tuổi của bệnh nhân: "))
spO2 = int(input("Nhập chỉ số SpO2 của bệnh nhân (%): "))
nhip_tim = int(input("Nhập nhịp tim của bệnh nhân (nhịp/phút): "))
bhyt = str(input("Nhập loại bảo hiểm y tế của bệnh nhân (no/yes): "))

# Phân luồng y khoa
if spO2 < 90 or nhip_tim > 120:
    triage = "Đỏ: Cấp cứu ngay"
elif 90 <= spO2 <= 95 or 100 <= nhip_tim <= 120:
    triage = "Vàng: Cần theo dõi sát"
else:
    triage = "Xanh: Ổn định, chờ theo thứ tự"
    
# Tạm ứng viện phí
price = 500000

if tuoi < 6 or tuoi >= 80:
    price = 0
elif bhyt == "yes":
    price = price - price * 0.5
else:
    price = price
    
print("PHIẾU TIẾP NHẬN BỆNH NHÂN:")
print(f"Họ và tên: {ho_ten}")
print(f"Tuổi: {tuoi} tuổi")
print(f"Chỉ số SpO2: {spO2}%")
print(f"Nhịp tim: {nhip_tim} nhịp/phút")
print(f"Loại bảo hiểm y tế: {bhyt}")
print(f"Phân luồng y khoa: {triage}")
print(f"Số tiền tạm ứng viện phí: {price} VND")