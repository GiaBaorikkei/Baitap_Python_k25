students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]

# Hàm kiểm tra điểm hợp lệ
def validate_score(score_input):
    try:
        score = float(score_input)
        if 0 <= score <= 10:
            return True
        return False
    except:
        return False


# Hàm tìm học viên theo mã
def find_student_by_id(student_list, student_id):
    for student in student_list:
        if student["student_id"] == student_id:
            return student
    return None


# Hàm hiển thị danh sách học viên
def display_students(student_list):
    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
        return

    for index, student in enumerate(student_list, start=1):
        print(
            f"{index}. Mã: {student['student_id']} | "
            f"Tên: {student['name']} | "
            f"Toán: {student['math_score']} | "
            f"Anh: {student['english_score']}"
        )


# Hàm thêm học viên
def add_student(student_list):
    student_id = input("Nhập mã học viên: ").strip().upper()

    if find_student_by_id(student_list, student_id):
        print("Mã học viên đã tồn tại, vui lòng nhập mã khác!")
        return

    while True:
        name = input("Nhập tên học viên: ").strip()
        if name != "":
            name = name.title()
            break
        print("Tên học viên không được để trống!")

    while True:
        math_score = input("Nhập điểm Toán: ")
        if validate_score(math_score):
            math_score = float(math_score)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")

    while True:
        english_score = input("Nhập điểm Anh: ")
        if validate_score(english_score):
            english_score = float(english_score)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")

    student = {
        "student_id": student_id,
        "name": name,
        "math_score": math_score,
        "english_score": english_score
    }

    student_list.append(student)
    print("Thêm học viên thành công!")


# Hàm cập nhật điểm
def update_score(student_list):
    student_id = input("Nhập mã học viên cần cập nhật: ").strip().upper()

    student = find_student_by_id(student_list, student_id)

    if student is None:
        print(f"Không tìm thấy học viên mang mã {student_id}!")
        return

    while True:
        math_score = input("Nhập điểm Toán mới: ")
        if validate_score(math_score):
            student["math_score"] = float(math_score)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")

    while True:
        english_score = input("Nhập điểm Anh mới: ")
        if validate_score(english_score):
            student["english_score"] = float(english_score)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")

    print("Cập nhật điểm thành công!")


# Hàm xếp loại
def get_rank(average_score):
    if average_score >= 8:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5:
        return "Trung bình"
    else:
        return "Yếu"


# Hàm đánh giá học lực
def evaluate_students(student_list):
    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
        return

    for student in student_list:
        average = (student["math_score"] + student["english_score"]) / 2
        rank = get_rank(average)

        print(
            f"Mã: {student['student_id']} | "
            f"Tên: {student['name']} | "
            f"ĐTB: {average:.2f} | "
            f"Xếp loại: {rank}"
        )


# Chương trình chính
while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====")
    print("1. Hiển thị danh sách học viên")
    print("2. Thêm học viên mới")
    print("3. Cập nhật điểm thi theo mã học viên")
    print("4. Đánh giá học lực của toàn bộ học viên")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn: ")

    if choice == "1":
        display_students(students)

    elif choice == "2":
        add_student(students)

    elif choice == "3":
        update_score(students)

    elif choice == "4":
        evaluate_students(students)

    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")