# Danh sách chẩn đoán hiện tại của bệnh nhân Nguyễn Văn A
patient_diagnoses = ["Sốt Xuất Huyết"]

# Hàm chuẩn hóa tên bệnh và thêm vào hồ sơ
def add_diagnosis(raw_diagnosis, current_list):
    # Chuẩn hóa tên bệnh
    raw_diagnosis = raw_diagnosis.strip().title()

    # Thêm cả chuỗi vào danh sách
    current_list.append(raw_diagnosis)

    return current_list

# Bác sĩ nhập thêm một chẩn đoán mới bị lỗi định dạng
new_diagnosis = "  viEm phE QUan  "

# Cập nhật hồ sơ
updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)

print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)