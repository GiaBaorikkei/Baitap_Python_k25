# Phương thức là các hành vi, hoạt động của đối tượng

class SinhVien:
    ## Cách 1 là constructor mặc định
    def __init__(self):
        self.name = "Bảo"
        self.score = 9
        self.school = "PTIT"
    
    # Định nghĩa phương thức
    def get_infomation_of_student(self):
        print(f"Tên tôi là {self.name} được {self.score} tại trường {self.school}")

# Đối tượng đã khởi tạo cho Constructor đã khai báo
sv = SinhVien()
print(sv.score)
sv.get_infomation_of_student()

"""
Thuộc tính <=> biến
Phương thức <=> hàm function(self)
"""