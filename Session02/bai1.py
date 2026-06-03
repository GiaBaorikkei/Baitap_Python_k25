print("HỆ THỐNG PHÂN LOẠI CẤP CỨU")

nhip_tim = int(input("Nhập nhịp tim của bệnh nhân (nhịp/phút): "))

# Hệ thống phân loại ưu tiên
if nhip_tim > 120:
    print("Đỏ: Cấp cứu ngay")
elif nhip_tim > 100:
    print("Vàng: Bất thường, cần theo dõi sát")
elif nhip_tim < 60:
    print("Xanh: Nhịp tim chậm cần kiểm tra thêm")
elif 60 <= nhip_tim <= 100:
    print("Xanh dương: Ổn định, chờ theo thứ tự")
else:
    print("Xanh lá: Nhịp tim bình thường, chờ theo thứ tự")
    
print("Quá trình phân loại đã hoàn tất. Vui lòng chờ để được khám bệnh.")
