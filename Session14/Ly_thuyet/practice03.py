"""
Các loại tham số:

"""

# Tham số thông thường
"""
Bắt buộc phải truyền đối số vào
"""
def get_student_1(name, age, school):
    print(f"{name} | {age} | {school}")
get_student_1("Bảo", 20, "PTIT")
    
# Tham số mặc định
"""
Nếu không có đối số => truyền mặc định giá trị khởi tạo
Nếu có đối số => lấy giá trị đối số mới đó
"""
def get_student_2(name = "Bảo", age = 20, school = "PTIT"):
        print(f"{name} | {age} | {school}")

get_student_2()

# Tham số từ khoá
def get_student_3(name, age, school):
    print(f"{name} | {age} | {school}")
get_student_3(age=17, school="PTIT", name="Bảo")

# Tham số args
def get_information_in_company(name, age, room, *args):
    print(f"{name} | {age} | {room} | {args}")

# Trường hợp của nhân viên
get_information_in_company("Bảo", 25, "IT")

# Trường hợp trưởng phòng
get_information_in_company("Bach", 30, "TeachLead", 3, 7)

