from datetime import datetime

patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]


# Hiển thị danh sách hồ sơ
def display_records(records):
    if len(records) == 0:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return

    print("--- DANH SÁCH BỆNH NHÂN --------------------------------------------------")

    for i in range(len(records)):
        info = records[i].split("-")

        print(
            f"{i+1}. [{info[0]}] {info[1]:<18} | "
            f"Năm sinh: {info[2]} | "
            f"Chẩn đoán: {info[3]}"
        )

    print("--------------------------------------------------------------------------")


# Kiểm tra mã bệnh nhân tồn tại
def is_duplicate_id(records, patient_id):
    for record in records:
        if record.startswith(patient_id + "-"):
            return True
    return False


# Thêm bệnh nhân mới
def add_patient(records):
    print("\n--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if is_duplicate_id(records, patient_id):
        print("\nMã bệnh nhân đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ")
    name = name.replace("-", " ")
    name = name.strip().title()

    current_year = datetime.now().year

    while True:
        birth_year = input("Nhập năm sinh: ").strip()

        if birth_year.isdigit():
            year = int(birth_year)

            if 1900 <= year <= current_year:
                break

        print("\nNăm sinh không hợp lệ, vui lòng nhập lại!")

    diagnosis = input("Nhập chẩn đoán: ")
    diagnosis = diagnosis.replace("-", " ")
    diagnosis = diagnosis.strip().capitalize()

    new_record = "-".join([
        patient_id,
        name,
        birth_year,
        diagnosis
    ])

    records.append(new_record)

    print("\nThêm hồ sơ bệnh nhân thành công!")
    print("Dữ liệu đã lưu:")
    print(new_record)


# Cập nhật chẩn đoán
def update_diagnosis(records):
    print("\n--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")

    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()

    found = False

    for i in range(len(records)):
        if records[i].startswith(patient_id + "-"):

            info = records[i].split("-")

            print(f"\nTìm thấy bệnh nhân: {info[1]}")
            print(f"Chẩn đoán hiện tại: {info[3]}")

            new_diagnosis = input("Nhập chẩn đoán mới: ")

            new_diagnosis = new_diagnosis.replace("-", " ")
            new_diagnosis = new_diagnosis.strip().capitalize()

            # String immutable => tách -> sửa -> ghép lại
            info[3] = new_diagnosis

            records[i] = "-".join(info)

            print("\nCập nhật chẩn đoán thành công!")
            found = True
            break

    if not found:
        print(f"\nKhông tìm thấy bệnh nhân mang mã {patient_id}!")


# Báo cáo độ tuổi
def generate_age_report(records):
    print("\n--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")

    current_year = datetime.now().year

    children = 0
    adults = 0
    elderly = 0

    for record in records:
        info = record.split("-")

        age = current_year - int(info[2])

        if age < 16:
            children += 1
        elif age <= 60:
            adults += 1
        else:
            elderly += 1

    print(f"Trẻ em: {children} bệnh nhân")
    print(f"Trưởng thành: {adults} bệnh nhân")
    print(f"Người cao tuổi: {elderly} bệnh nhân")
    print("--------------------------------------")


# Chương trình chính
while True:
    print("\n===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
    print("1. Xem danh sách hồ sơ bệnh án")
    print("2. Thêm hồ sơ bệnh nhân mới")
    print("3. Cập nhật chẩn đoán theo Mã BN")
    print("4. Báo cáo phân loại theo độ tuổi")
    print("5. Thoát chương trình")
    print("==================================================")

    choice = input("Chọn chức năng (1-5): ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ!")
        continue

    choice = int(choice)

    if choice == 1:
        display_records(patient_records)

    elif choice == 2:
        add_patient(patient_records)

    elif choice == 3:
        update_diagnosis(patient_records)

    elif choice == 4:
        generate_age_report(patient_records)

    elif choice == 5:
        print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
        break

    else:
        print("Lựa chọn không hợp lệ!")