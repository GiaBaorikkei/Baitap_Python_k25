grade_book = [
    {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
]


# Tìm học sinh theo ID
def find_student(book, student_id):
    for student in book:
        if student["id"] == student_id:
            return student
    return None


# Hiển thị bảng điểm
def display_grades(book):
    if len(book) == 0:
        print("Danh sách học sinh đang trống!")
        return

    print("\n--- BẢNG ĐIỂM HỌC SINH ---")
    print(f"{'Mã SV':<8}| {'Tên Học Sinh':<20}| {'Điểm Toán':<11}| {'Điểm Anh':<10}| ĐTB")
    print("-" * 70)

    for student in book:
        math_score = student["info"][0]
        english_score = student["info"][1]
        average = (math_score + english_score) / 2

        print(
            f"{student['id']:<8}| "
            f"{student['name']:<20}| "
            f"{math_score:<11}| "
            f"{english_score:<10}| "
            f"{average:.2f}"
        )

    print("-" * 70)


# Thêm học sinh
def add_student(book):
    while True:
        student_id = input("Nhập mã học sinh mới: ").strip().upper()

        if find_student(book, student_id):
            print(
                f"Lỗi: Mã học sinh {student_id} đã tồn tại! "
                f"Vui lòng nhập mã khác."
            )
        else:
            break

    name = input("Nhập tên học sinh: ").strip().title()

    math_score = float(input("Nhập điểm Toán: "))
    english_score = float(input("Nhập điểm Anh: "))

    student = {
        "id": student_id,
        "name": name,
        "info": (math_score, english_score)
    }

    book.append(student)

    print(
        f"Thành công: Đã thêm học sinh "
        f"{student_id} vào hệ thống!"
    )


# Cập nhật điểm
def update_scores(book):
    student_id = input(
        "Nhập mã học sinh cần cập nhật: "
    ).strip().upper()

    student = find_student(book, student_id)

    if student is None:
        print("Không tìm thấy học sinh!")
        return

    math_score = float(input("Nhập điểm Toán mới: "))
    english_score = float(input("Nhập điểm Anh mới: "))

    # Tạo tuple mới thay thế tuple cũ
    student["info"] = (math_score, english_score)

    print(
        f"Thành công: Đã cập nhật điểm "
        f"cho học sinh {student_id}!"
    )


# Xóa học sinh
def delete_student(book):
    student_id = input(
        "Nhập mã học sinh cần xóa: "
    ).strip().upper()

    student = find_student(book, student_id)

    if student is None:
        print("Không tìm thấy học sinh!")
        return

    book.remove(student)

    print(
        f"Thành công: Đã xóa hồ sơ học sinh "
        f"{student_id} khỏi hệ thống!"
    )


# Hàm chính
def main():
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===")
        print("1. Xem bảng điểm học sinh")
        print("2. Thêm hồ sơ học sinh mới")
        print("3. Cập nhật điểm số")
        print("4. Xóa hồ sơ học sinh")
        print("5. Thoát chương trình")
        print("================================")

        choice = input("Chọn chức năng (1-5): ")

        if choice == "1":
            display_grades(grade_book)

        elif choice == "2":
            add_student(grade_book)

        elif choice == "3":
            update_scores(grade_book)

        elif choice == "4":
            delete_student(grade_book)

        elif choice == "5":
            print(
                "Cảm ơn bạn đã sử dụng hệ thống. "
                "Hẹn gặp lại!"
            )
            break

        else:
            print("Lựa chọn không hợp lệ!")


main()