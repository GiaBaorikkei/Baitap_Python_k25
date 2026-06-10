"""
# Tiêu chuẩn python -> tên biến + tên funcion -> snake
def name_funcion(tham số 1, tham số 2, ...):
    # thực hiện logic như bình thường

# Cách gọi hàm 
name_funcion(tham số 1, tham số 2, ...)

=> Funcion là khối đóng gói các chức năng
"""
student_list = ["Bảo", "Trang", "Thảo"]
def get_all_list(infomation_list):
    for infor in infomation_list:
        print(infor)
get_all_list(student_list)

# Ví dụ
def get_student(name,age,school):
    print(f"{name} | {age} | {school}")
get_student("Bảo", 20, "PTIT")