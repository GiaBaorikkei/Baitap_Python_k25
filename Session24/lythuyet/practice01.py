"""
Thuộc tính là những vật tĩnh
Phương thức là vật động (hành động, hành vi)
"""

class MyObject:
    pass

# Căn nhà

"""
Class: bản phác thảo
Object: đối tượng cụ thể mà cần phác thảo
"""

class MyHome:
    pass
"""
Của nhà, xe trong nhà, ...
Phòng ăn, phòng ngủ, ..
"""

# Constructor
"""
Khi làm việc với OOP thì phải sử dụng với từ khoá "self"
"""
class SinhVien:
    # Hàm khởi tạo ban đầu
    """
    self.biến => thuộc tính
    """
    
    ## Cách 1 là constructor mặc định
    def __init__(self):
        self.name = "Bảo"
        self.score = 9
        self.school = "PTIT"
        
    # ## Cách 2: Constructor tự khai báo
    # def __init__(self, name, score, school):
    #     self.name = name
    #     self.score = score
    #     self.school = school

# # Đối tượng đã khởi tạo
# sv = SinhVien()

# # Lấy ra các thuộc tính
# print(sv.name)

# Đối tượng đã khởi tạo cho Constructor đã khai báo
sv = SinhVien("Trang", 10, "DUE")
print(sv.name)
print(sv.score)
print(sv.school)

"""
Constructor mặc định <=> tham số mặc định
Contructor tự khai báo <=> tham số thông thường
"""