print("Nhập thông tin nhân viên")

employee_id = int(input("Nhập mã nhân viên: "))
name = input("Nhập họ và tên nhân viên: ")

salary = int(input("Nhập mức lương của nhân viên: "))
while salary <= 0:
    print("Lỗi: Mức lương phải lớn hơn 0!")
    salary = int(input("Nhập lại mức lương: "))

performance = int(input("Nhập điểm KPI (1-5): "))
while performance < 1 or performance > 5:
    print("Lỗi: KPI phải nằm trong khoảng từ 1 đến 5!")
    performance = int(input("Nhập lại điểm KPI: "))

year_of_experience = int(input("Nhập số năm kinh nghiệm: "))
while year_of_experience < 0:
    print("Lỗi: Số năm kinh nghiệm phải >= 0!")
    year_of_experience = int(input("Nhập lại số năm kinh nghiệm: "))

print("\n===== THÔNG TIN NHÂN VIÊN =====")
print("Mã nhân viên:", employee_id)
print("Họ và tên:", name)
print("Mức lương:", salary)
print("Điểm KPI:", performance)
print("Số năm kinh nghiệm:", year_of_experience)