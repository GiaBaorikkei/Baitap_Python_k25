"""
Cấp độ truy cập:
+ public (default): truy cập mọi lúc mọi nơi
+ protected: dùng cho class/subclass
+ private: hạn chế tối đá truy cập trực tiếp vào đây

Ký hiệu:
self.<tên biến> => public
self._<tên biến> => protected
self.__<tên biến> => private

getter/setter
- getter là lấy ra giá trị của thuộc tính
- setter là thay đổi giá trị của thuộc tính
"""

class NganHang: 
    def __init__(self):
        self.name = "BIDV Banking"
        self.tien_gui = 1_000_000
        self.tien_trong_tai_khoan = 20_000_000
        
    def get_tien_tai_khoan(self):
        print()
        
ngan_hang = NganHang()
print(f"Name: {ngan_hang.name}")
print(f"Số tiền gửi: {ngan_hang.tien_gui}")
print(f"Tiền trong TK: {ngan_hang.tien_trong_tai_khoan}")

# Nếu dùng @property thì sẽ đưa phương thức về thuộc tính
"""
Nếu có @property => ngan_hang.get_tien_tai_khoan
"""