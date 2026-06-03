from datetime import datetime

# ==========================
# NHẬP THÔNG TIN BỆNH NHÂN
# ==========================

name = input("Nhập tên bệnh nhân: ")
birth_year = int(input("Nhập năm sinh: "))
days_sick = int(input("Nhập số ngày bị bệnh: "))
temperature = float(input("Nhập nhiệt độ cơ thể (°C): "))
exam_fee = float(input("Nhập chi phí khám: "))

# KIỂM TRA DỮ LIỆU HỢP LỆ

current_year = datetime.now().year

if name.strip() == "":
    print("Lỗi: Tên bệnh nhân không được để trống!")
    exit()

if birth_year < 1900 or birth_year > current_year:
    print("Lỗi: Năm sinh không hợp lệ!")
    exit()

if days_sick < 0:
    print("Lỗi: Số ngày bị bệnh phải >= 0!")
    exit()

if temperature < 30 or temperature > 45:
    print("Lỗi: Nhiệt độ không hợp lệ!")
    exit()

if exam_fee <= 0:
    print("Lỗi: Chi phí khám phải lớn hơn 0!")
    exit()

# TÍNH TOÁN THÔNG TIN

age = current_year - birth_year

surcharge = exam_fee * 0.1
total_fee = exam_fee + surcharge

# PHÂN LOẠI TÌNH TRẠNG SỨC KHỎE

if temperature > 38 and days_sick > 3:
    health_status = "Nguy hiểm"
elif temperature > 38:
    health_status = "Sốt cao"
elif temperature > 37.5:
    health_status = "Sốt nhẹ"
else:
    health_status = "Bình thường"

# ĐÁNH GIÁ MỨC ĐỘ ƯU TIÊN

if health_status == "Nguy hiểm":
    if age > 60:
        priority = "Cấp cứu"
    else:
        priority = "Ưu tiên cao"
else:
    priority = "Bình thường"

# ĐÁNH GIÁ MỨC CHI PHÍ

cost_level = "Cao" if total_fee > 500000 else "Thấp"

# HIỂN THỊ KẾT QUẢ

print("\n" + "=" * 50)
print("      THÔNG TIN BỆNH NHÂN")
print("=" * 50)

print(f"Tên bệnh nhân      : {name}")
print(f"Tuổi               : {age}")
print(f"Số ngày bị bệnh    : {days_sick}")
print(f"Nhiệt độ           : {temperature}°C")
print(f"Chi phí khám       : {exam_fee:,.0f} VNĐ")
print(f"Phụ phí (10%)      : {surcharge:,.0f} VNĐ")
print(f"Tổng chi phí       : {total_fee:,.0f} VNĐ")

print("-" * 50)
print(f"Tình trạng sức khỏe: {health_status}")
print(f"Mức độ ưu tiên     : {priority}")
print(f"Mức chi phí        : {cost_level}")

print("=" * 50)