er_patients = [
    "ER01|Nguyen Van Quan|HR:115|TEMP:39.5",
    "ER02|Tran Thi Binh|HR:80|TEMP:37.0",
    "ER03|Le Van Cuong|HR:130|TEMP:38.2"
]


# Kiểm tra mã ER đã tồn tại
def is_duplicate_er(patients, er_id):
    for patient in patients:
        if patient.startswith(er_id + "|"):
            return True
    return False


# Tìm vị trí bệnh nhân theo mã ER
def find_patient_index(patients, er_id):
    for i in range(len(patients)):
        if patients[i].startswith(er_id + "|"):
            return i
    return -1


# Kiểm tra dữ liệu số
def is_valid_number(value):
    value = value.strip()

    if value.replace(".", "", 1).isdigit():
        return float(value) > 0

    return False


# Hiển thị bảng theo dõi
def display_dashboard(patients):
    if len(patients) == 0:
        print("Khoa cấp cứu hiện đang trống.")
        return

    print("\n--- BẢNG THEO DÕI CA CẤP CỨU ------------------------------------")

    for i in range(len(patients)):
        info = patients[i].split("|")

        hr = info[2].split(":")[1]
        temp = info[3].split(":")[1]

        print(
            f"{i+1}. [{info[0]}] {info[1]} | "
            f"Nhịp tim: {hr} bpm | "
            f"Nhiệt độ: {temp} °C"
        )

    print("-----------------------------------------------------------------")


# Tiếp nhận bệnh nhân mới
def admit_patient(patients):
    print("\n--- TIẾP NHẬN CA CẤP CỨU MỚI ---")

    er_id = input("Nhập mã ER: ").strip().upper()

    if len(er_id) == 0:
        print("Mã ER không được để trống!")
        return

    if is_duplicate_er(patients, er_id):
        print("\nMã ca cấp cứu đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ").strip().title()

    if len(name) == 0:
        print("\nTên bệnh nhân không được để trống!")
        return

    while True:
        hr = input("Nhập nhịp tim HR: ").strip()

        if is_valid_number(hr):
            hr_value = int(float(hr))

            if hr_value > 0:
                break

        print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")

    while True:
        temp = input("Nhập nhiệt độ TEMP: ").strip()

        if is_valid_number(temp):
            temp_value = float(temp)

            if temp_value >= 36.5:
                break

        print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!")

    record = "|".join([
        er_id,
        name,
        "HR:" + str(hr_value),
        "TEMP:" + str(temp_value)
    ])

    patients.append(record)

    print("\nTiếp nhận ca cấp cứu mới thành công!")
    print("Dữ liệu đã lưu:")
    print(record)


# Cập nhật sinh hiệu
def update_vitals(patients):
    print("\n--- CẬP NHẬT LẠI SINH HIỆU ---")

    er_id = input("Nhập mã ER cần cập nhật: ").strip().upper()

    index = find_patient_index(patients, er_id)

    if index == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return

    info = patients[index].split("|")

    print(f"Tìm thấy bệnh nhân: {info[1]}")
    print(f"Sinh hiệu hiện tại: {info[2]} | {info[3]}")

    print("Bạn muốn cập nhật:")
    print("1. Nhịp tim HR")
    print("2. Nhiệt độ TEMP")

    choice = input("Chọn loại sinh hiệu: ").strip()

    if choice == "1":
        value = input("Nhập nhịp tim mới: ").strip()

        if not is_valid_number(value):
            print("\nSinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")
            return

        info[2] = "HR:" + str(int(float(value)))

        patients[index] = "|".join(info)

        print("\nCập nhật nhịp tim thành công!")

    elif choice == "2":
        value = input("Nhập nhiệt độ mới: ").strip()

        if not is_valid_number(value):
            print("\nSinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")
            return

        info[3] = "TEMP:" + str(float(value))

        patients[index] = "|".join(info)

        print("\nCập nhật nhiệt độ thành công!")

    else:
        print("\nLựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2!")


# Báo động đỏ
def trigger_red_alert(patients):
    if len(patients) == 0:
        print("Khoa cấp cứu hiện đang trống.")
        return

    critical_count = 0

    print("\n!!! BÁO ĐỘNG ĐỎ - DANH SÁCH BỆNH NHÂN NGUY KỊCH !!!")

    for patient in patients:
        info = patient.split("|")

        hr = int(info[2].split(":")[1])
        temp = float(info[3].split(":")[1])

        if hr > 100 or temp >= 39.0:
            critical_count += 1

            print(
                f"{critical_count}. [{info[0]}] {info[1]} | "
                f"HR: {hr} bpm | "
                f"TEMP: {temp} °C | "
                f"CẦN XỬ LÝ KHẨN CẤP"
            )

    if critical_count == 0:
        print("--- KIỂM TRA BÁO ĐỘNG ĐỎ ---")
        print("Không có bệnh nhân nguy kịch tại thời điểm hiện tại.")
    else:
        print("-----------------------------------------------------")
        print(f"Tổng số ca nguy kịch: {critical_count}")


# Xuất viện / chuyển khoa
def discharge_patient(patients):
    print("\n--- XUẤT VIỆN / CHUYỂN KHOA ---")

    er_id = input("Nhập mã ER cần xóa khỏi hệ thống: ").strip().upper()

    if len(er_id) == 0:
        print("Mã ER không được để trống!")
        return

    index = find_patient_index(patients, er_id)

    if index == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return

    patient_name = patients[index].split("|")[1]

    patients.pop(index)

    print(f"Đã chuyển khoa thành công cho bệnh nhân {patient_name}!")


# Chương trình chính
while True:
    print("\n===== HỆ THỐNG QUẢN LÝ CẤP CỨU RIKKEI ER =====")
    print("1. Bảng theo dõi bệnh nhân")
    print("2. Tiếp nhận ca cấp cứu mới")
    print("3. Cập nhật lại sinh hiệu")
    print("4. BÁO ĐỘNG ĐỎ - Lọc bệnh nhân nguy kịch")
    print("5. Xuất viện / Chuyển khoa")
    print("6. Thoát chương trình")
    print("=================================================")

    choice = input("Chọn chức năng (1-6): ").strip()

    if choice == "1":
        display_dashboard(er_patients)

    elif choice == "2":
        admit_patient(er_patients)

    elif choice == "3":
        update_vitals(er_patients)

    elif choice == "4":
        trigger_red_alert(er_patients)

    elif choice == "5":
        discharge_patient(er_patients)

    elif choice == "6":
        print("Kết thúc ca trực. Hệ thống đã đóng!")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 6!")