students_list = [
    {
        "id": "SV001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "physics_score": 7.0,
        "chemistry_score": 9.0,
        "average_score": 8.17,
        "level": "Giỏi"
    },
    {
        "id": "SV002",
        "name": "Trần Thị B",
        "math_score": 7.5,
        "physics_score": 7.0,
        "chemistry_score": 8.0,
        "average_score": 7.50,
        "level": "Khá"
    },
    {
        "id": "SV003",
        "name": "Lê Văn C",
        "math_score": 6.0,
        "physics_score": 5.5,
        "chemistry_score": 7.0,
        "average_score": 6.17,
        "level": "Trung Bình"
    },
    {
        "id": "SV004",
        "name": "Phạm Thị D",
        "math_score": 9.0,
        "physics_score": 9.5,
        "chemistry_score": 8.5,
        "average_score": 9.00,
        "level": "Giỏi"
    },
    {
        "id": "SV005",
        "name": "Hoàng Văn E",
        "math_score": 4.0,
        "physics_score": 5.0,
        "chemistry_score": 4.5,
        "average_score": 4.50,
        "level": "Yếu"
    }
]

def validate_score(a):
    while True:
        score = input(f"Nhập điểm {a}: ")

        if score.replace(".", "", 1).isdigit():
            score = float(score)

            if 0 <= score <= 10:
                return score

        print("Điểm phải từ 0 đến 10!")

def add_student():
    while True:
        student_id = input("Nhập mã sinh viên: ").strip().upper()

        if student_id == "":
            print("Mã sinh viên không được để trống!")
            continue

        is_exist = False
        for student in students_list:
            if student["id"] == student_id:
                is_exist = True
                break

        if is_exist:
            print("Mã sinh viên đã tồn tại!")
            continue

        break

    while True:
        name = input("Nhập tên sinh viên: ").strip().title()

        if name == "":
            print("Tên sinh viên không được để trống!")
        else:
            break

    math = validate_score("Toán")
    physics = validate_score("Lý")
    chemistry = validate_score("Hoá")

    average_score = (math + physics + chemistry) / 3

    level = ranking_student(average_score)

    student = {
        "id": student_id,
        "name": name,
        "math_score": math,
        "physics_score": physics,
        "chemistry_score": chemistry,
        "average_score": average_score,
        "level": level
    }

    students_list.append(student)

    print("Thêm học sinh thành công!")
        
def update_score():
    student_id = input("Nhập mã sinh viên cần sửa: ").strip().upper()

    for student in students_list:
        if student["id"] == student_id:

            math = validate_score("Toán")
            physics = validate_score("Lý")
            chemistry = validate_score("Hóa")

            average_score = (math + physics + chemistry) / 3
            level = ranking_student(average_score)

            student["math_score"] = math
            student["physics_score"] = physics
            student["chemistry_score"] = chemistry
            student["average_score"] = average_score
            student["level"] = level

            print("Cập nhật điểm thành công!")
            return

    print("Mã sinh viên không tồn tại.")

def ranking_student(average_score):
    if average_score < 5:
        return "Yếu"
    elif average_score < 7:
        return "Trung Bình"
    elif average_score < 8:
        return "Khá"
    else:
        return "Giỏi"
    
def search_student():
    student_id = input("Nhập mã sinh viên cần tìm kiếm: ").strip().upper()
    
    for i in students_list:
        if i["id"] == student_id:
            print(f"{'Mã SV':<10} | {'Họ tên':<20} | {'Toán':<10} | {'Lý':<10} | {'Hoá':<10} | {'TB':<10} | {'Xếp loại'}")
            print(f"{i['id']:<10} | {i['name']:<20} | {i['math_score']:<10} | {i['physics_score']:<10} | {i['chemistry_score']:<10} | {i['average_score']:<10} | {i['level']}")


def delete_student():
    student_id = input("Nhập mã sinh viên cần xoá: ").strip().upper()

    for student in students_list:
        if student["id"] == student_id:

            confirm = input("Bạn có chắc muốn xóa? (Y/N): ").strip().upper()

            if confirm == "Y":
                students_list.remove(student)
                print("Xóa sinh viên thành công!")
            else:
                print("Đã hủy thao tác xóa.")

            return

    print("Mã sinh viên không tồn tại.")
    
def statistics_by_level():
    gioi = 0
    kha = 0
    trung_binh = 0
    yeu = 0
    
    for i in students_list:
        if i["level"] == "Giỏi":
            gioi += 1
        elif i["level"] == "Khá":
            kha += 1
        elif i["level"] == "Trung Bình":
            trung_binh += 1
        else:
            yeu += 1
    print("--- KẾT QUẢ THỐNG KÊ ---")
    print(f"Số học sinh Giỏi: {gioi}")
    print(f"Số học sinh Khá: {kha}")
    print(f"Số học sinh Trung Bình: {trung_binh}")
    print(f"Số học sinh Yếu: {yeu}")

def display_student():
    print(f"{'Mã SV':<10} | {'Họ tên':<20} | {'Toán':<10} | {'Lý':<10} | {'Hoá':<10} | {'TB':<10} | {'Xếp loại'}")
    for i in students_list:
        print(f"{i['id']:<10} | {i['name']:<20} | {i['math_score']:<10} | {i['physics_score']:<10} | {i['chemistry_score']:<10} | {i['average_score']:<10} | {i['level']}")

def main():
    while True:
        print("----- QUẢN LÍ SINH VIÊN -----")
        print("1. Hiển thị danh sách sinh viên.")
        print("2. Tiếp nhận sinh viên.")
        print("3. Cập nhật kết quả học tập.")
        print("4. Xoá sinh viên.")
        print("5. Tìm kiếm sinh viên.")
        print("6. Thống kê điểm TB.")
        print("7. Phân loại học lực.")
        print("8. Thoát chương trình.")
        print("--------------------------------")
        
        choice = input("Mời bạn nhập lựa chọn (1-8): ")
        
        if choice == "1":
            display_student()
        elif choice == "2":
            add_student()
        elif choice == "3":
            update_score()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            statistics_by_level()
        elif choice == "8":
            print("Đã thoát chương trình.")
            break
        else: 
            print("Lựa chọn không hợp lệ.")
main()