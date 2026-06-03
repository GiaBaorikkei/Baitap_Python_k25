print("-- Phần mềm tính tổng quỹ lương --")

tong_luong = 0
for i in range(1,4):
     print("Đang xử lí nhân viên số", i)
     luong = int(input("Nhập mức lương: "))
     tong_luong += luong

print("Tổng ngân sách cần chuẩn bị là:", tong_luong)