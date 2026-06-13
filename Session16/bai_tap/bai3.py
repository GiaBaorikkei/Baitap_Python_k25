patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]


# Hàm kiểm tra giới tính
def validate_gender(gender_input):
    gender = gender_input.strip().lower()
    return gender == "nam" or gender == "nu"


# Hàm tìm vị trí bệnh nhân theo mã
def find_patient_index(patient_list, patient_id):
    patient_id = patient_id.strip().upper()

    for i in range(len(patient_list)):
        if patient_list[i][0] == patient_id:
            return i

    return -1


# Hiển thị danh sách bệnh nhân
def display_patients(patient_list):
    print("----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")

    if len(patient_list) == 0:
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return

    for i in range(len(patient_list)):
        print(
            f"{i + 1}. Mã: {patient_list[i][0]} | "
            f"Tên: {patient_list[i][1]} | "
            f"Giới tính: {patient_list[i][2]} | "
            f"Bệnh: {patient_list[i][3]}"
        )


# Tiếp nhận bệnh nhân mới
def add_patient(patient_list):
    print("----- TIẾP NHẬN BỆNH NHÂN MỚI -----")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if len(patient_id) == 0:
        print("Mã bệnh nhân không được để trống!")
        return

    if find_patient_index(patient_list, patient_id) != -1:
        print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
        return

    patient_name = input("Nhập tên bệnh nhân: ").strip().title()

    if len(patient_name) == 0:
        print("Tên bệnh nhân không được để trống!")
        return

    while True:
        gender = input("Nhập giới tính Nam/Nu: ").strip()

        if validate_gender(gender):
            gender = gender.title()
            break

        print("Giới tính không hợp lệ, vui lòng nhập lại!")

    diagnosis = input("Nhập chẩn đoán bệnh: ").strip().capitalize()

    new_patient = [
        patient_id,
        patient_name,
        gender,
        diagnosis
    ]

    patient_list.append(new_patient)

    print("Tiếp nhận bệnh nhân thành công!")


# Cập nhật chẩn đoán
def update_diagnosis(patient_list):
    print("----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")

    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip()

    if len(patient_id) == 0:
        print("Mã bệnh nhân không được để trống!")
        return

    index = find_patient_index(patient_list, patient_id)

    if index == -1:
        print(f"Không tìm thấy hồ sơ mang mã {patient_id.upper()}!")
        return

    print("Tìm thấy bệnh nhân:", patient_list[index][1])
    print("Chẩn đoán hiện tại:", patient_list[index][3])

    new_diagnosis = input("Nhập chẩn đoán mới: ").strip()

    if len(new_diagnosis) == 0:
        print("Chẩn đoán bệnh không được để trống!")
        return

    patient_list[index][3] = new_diagnosis.capitalize()

    print("Cập nhật chẩn đoán bệnh thành công!")


# Tìm kiếm theo bệnh
def search_by_disease(patient_list):
    print("----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")

    keyword = input("Nhập từ khóa tên bệnh: ").strip()

    if len(keyword) == 0:
        print("Từ khóa tìm kiếm không được để trống!")
        return

    count = 0

    print("Kết quả tìm kiếm:")

    for patient in patient_list:
        if keyword.lower() in patient[3].lower():
            count += 1

            print(
                f"{count}. Mã: {patient[0]} | "
                f"Tên: {patient[1]} | "
                f"Giới tính: {patient[2]} | "
                f"Bệnh: {patient[3]}"
            )

    if count == 0:
        print("Không tìm thấy bệnh nhân nào phù hợp.")

    print(
        f"\nCó tổng cộng {count} bệnh nhân mắc bệnh liên quan đến '{keyword}'."
    )


# Chương trình chính
while True:
    print("\n===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
    print("1. Hiển thị danh sách bệnh nhân")
    print("2. Tiếp nhận bệnh nhân mới")
    print("3. Cập nhật chẩn đoán bệnh theo mã BN")
    print("4. Tìm kiếm và thống kê theo tên bệnh")
    print("5. Thoát chương trình")
    print("===========================================")

    choice = input("Nhập lựa chọn của bạn: ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")
        continue

    choice = int(choice)

    if choice == 1:
        display_patients(patients)

    elif choice == 2:
        add_patient(patients)

    elif choice == 3:
        update_diagnosis(patients)

    elif choice == 4:
        search_by_disease(patients)

    elif choice == 5:
        print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")