so_nhan_vien = int(input("Nhập số lượng nhân viên: "))

for i in range(1, so_nhan_vien + 1):

    print(f"\nNhân viên thứ {i}")

    ten = input("Nhập tên nhân viên: ")
    ngay_lam = int(input("Nhập số ngày làm việc: "))

    if ngay_lam < 0 or ngay_lam > 22:
        print("Dữ liệu không hợp lệ")
        continue

    if ngay_lam == 0:
        print("Nhân viên nghỉ toàn bộ tháng")

    print("Biểu đồ ngày làm việc:")

    for hang in range(1):
        for cot in range(ngay_lam):
            print("*", end="")
        print()

    if ngay_lam >= 18:
        print("Làm việc chăm chỉ")
    elif ngay_lam < 10:
        print("Làm việc ít")
    else:
        print("Làm việc bình thường")

    lua_chon = input("Tiếp tục nhập? (Y/N): ")

    if lua_chon.upper() == "N":
        break

print("\nKết thúc chương trình")