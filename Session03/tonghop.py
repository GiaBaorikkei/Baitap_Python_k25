print("===== HỆ THỐNG QUẢN LÝ CHẤM CÔNG NHÂN VIÊN =====")

tiep_tuc = "y"

while tiep_tuc == "y":

    so_nhan_vien = int(input("Nhập số lượng nhân viên: "))

    for i in range(1, so_nhan_vien + 1):
        print(f"--- Nhân viên thứ {i} ---")

        ten = input("Nhập tên nhân viên: ")
        so_ngay_lam = int(input("Nhập số ngày đi làm: "))

        print(f"Nhân viên {i}")
        print("Tên nhân viên:", ten)
        print("Số ngày đi làm:", so_ngay_lam)

        if so_ngay_lam < 20:
            print("Đánh giá: Cần cải thiện chuyên cần")
        else:
            print("Đánh giá: Nhân viên chuyên cần tốt")

    tiep_tuc = input(
        "Bạn có muốn tiếp tục chương trình không? (y/n): "
    )

print("Chương trình kết thúc!")