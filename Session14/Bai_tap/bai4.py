student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]


# Tính điểm trung bình
def calculate_average(student):
    return (student["math"] + student["physics"] + student["chemistry"]) / 3


# Xếp loại học lực
def get_rank(avg):
    if avg >= 8:
        return "Giỏi"
    elif avg >= 6.5:
        return "Khá"
    elif avg >= 5:
        return "Trung bình"
    else:
        return "Yếu"


# Tìm sinh viên theo mã
def find_student_by_id(records, student_id):
    for student in records:
        if student["student_id"] == student_id:
            return student
    return None


# Kiểm tra điểm hợp lệ
def validate_score():
    while True:
        try:
            score = float(input("Nhập điểm mới: "))

            if 0 <= score <= 10:
                return score

            print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")

        except ValueError:
            print("Vui lòng nhập số!")


# Chức năng 1
def display_grades(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("\n--- BẢNG ĐIỂM SINH VIÊN ---")

    for index, student in enumerate(records, start=1):
        avg = calculate_average(student)
        rank = get_rank(avg)

        print(
            f"{index}. [{student['student_id']}] {student['name']} | "
            f"Toán: {student['math']} | "
            f"Lý: {student['physics']} | "
            f"Hóa: {student['chemistry']} | "
            f"ĐTB: {avg:.2f} - {rank}"
        )

    print("---------------------------")


# Chức năng 2
def update_student_score(records):
    student_id = input("Nhập mã sinh viên cần cập nhật: ").strip().upper()

    student = find_student_by_id(records, student_id)

    if student is None:
        print(f"Không tìm thấy sinh viên mang mã {student_id} trong hệ thống!")
        return

    print("1. Toán")
    print("2. Lý")
    print("3. Hóa")

    subject = input("Chọn môn học (1-Toán, 2-Lý, 3-Hóa): ")

    if subject not in ["1", "2", "3"]:
        print("Môn học không hợp lệ!")
        return

    new_score = validate_score()

    if subject == "1":
        student["math"] = new_score
        subject_name = "Toán"

    elif subject == "2":
        student["physics"] = new_score
        subject_name = "Lý"

    else:
        student["chemistry"] = new_score
        subject_name = "Hóa"

    print(
        f">> Đã cập nhật điểm {subject_name} của sinh viên "
        f"'{student['name']}' thành {new_score}."
    )


# Chức năng 3
def generate_report(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    passed = 0
    failed = 0

    for student in records:
        avg = calculate_average(student)

        if avg >= 5:
            passed += 1
        else:
            failed += 1

    total = len(records)

    pass_percent = passed / total * 100
    fail_percent = failed / total * 100

    print("\n--- BÁO CÁO HỌC VỤ ---")
    print(f"Tổng số sinh viên: {total}")
    print(
        f"Số lượng qua môn (ĐTB >= 5.0): "
        f"{passed} sinh viên ({pass_percent:.2f}%)"
    )
    print(
        f"Số lượng trượt (ĐTB < 5.0): "
        f"{failed} sinh viên ({fail_percent:.2f}%)"
    )
    print("----------------------")


# Chức năng 4
def find_valedictorian(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    top_student = records[0]
    highest_avg = calculate_average(records[0])

    for student in records[1:]:
        avg = calculate_average(student)

        if avg > highest_avg:
            highest_avg = avg
            top_student = student

    print("\n--- VINH DANH THỦ KHOA ---")
    print(
        f"Sinh viên: {top_student['name']} "
        f"(Mã: {top_student['student_id']})"
    )
    print(f"Điểm Trung Bình: {highest_avg:.2f}")
    print("Chúc mừng sinh viên đã đạt thành tích xuất sắc nhất khóa!")
    print("--------------------------")


# Chương trình chính
while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====")
    print("1. Xem bảng điểm và học lực")
    print("2. Cập nhật điểm thi sinh viên")
    print("3. Báo cáo thống kê (Đỗ/Trượt)")
    print("4. Tìm sinh viên Thủ khoa")
    print("5. Thoát chương trình")
    print("======================================================")

    choice = input("Chọn chức năng (1-5): ")

    if choice == "1":
        display_grades(student_records)

    elif choice == "2":
        update_student_score(student_records)

    elif choice == "3":
        generate_report(student_records)

    elif choice == "4":
        find_valedictorian(student_records)

    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")