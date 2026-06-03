for i in range(1,4):
    print("Đang xử lí nhân viên số", i)
    ma_nv = int(input("Nhập mã nhân viên: "))
    ho_ten = str(input("Nhập họ và tên nhân viên: "))
    phong_ban = str(input("Nhập phòng ban của nhân viên: "))
    if str(ma_nv).strip() == "" or str(ho_ten).strip() == "":
        print("[Cảnh báo] Dữ liệu tên hoặc mã không hợp lệ! Huỷ bỏ tạo hồ sơ cho nhân viên này.")
    else:
        print(f"Nhân viên số {i}: Mã nv: NV{ma_nv} - Họ tên: {ho_ten} - Phòng ban: {phong_ban}")