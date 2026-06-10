student_records = [
    {
        "student_id": "RA01",
        "name": "Nguyễn Văn Code",
        "current_points": 1500,
        "spent_points": 500,
        "refunded_points": 0,
        "multiplier": 1.0
    },
    {
        "student_id": "RA02",
        "name": "Trần Thị Bug",
        "current_points": 800,
        "spent_points": 1200,
        "refunded_points": 100,
        "multiplier": 1.5
    },
    {
        "student_id": "RA03",
        "name": "Lê Văn Fix",
        "current_points": 300,
        "spent_points": 0,
        "refunded_points": 0,
        "multiplier": 2.0
    }
]


# Tìm học viên theo mã
def find_student_by_id(records, student_id):
    for student in records:
        if student["student_id"] == student_id:
            return student
    return None


# Kiểm tra số nguyên dương
def input_positive_int(message):
    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Vui lòng nhập số nguyên dương!")

        except ValueError:
            print("Vui lòng nhập số nguyên dương!")


# Kiểm tra hệ số nhân
def input_multiplier():
    while True:
        try:
            multiplier = float(
                input("Nhập hệ số nhân mới (1.0 - 3.0): ")
            )

            if 1.0 <= multiplier <= 3.0:
                return multiplier

            print(
                "Hệ số nhân không hợp lệ. "
                "Chỉ chấp nhận số từ 1.0 đến 3.0"
            )

        except ValueError:
            print(
                "Hệ số nhân không hợp lệ. "
                "Chỉ chấp nhận số từ 1.0 đến 3.0"
            )


# Chức năng 1
def display_statements(records):
    print("\n--- SAO KÊ ĐIỂM SỐ ---")

    for index, student in enumerate(records, start=1):

        current = student["current_points"]

        if current < 500:
            status = "Cần tích lũy thêm"
        elif current <= 1500:
            status = "Thành viên tiềm năng"
        else:
            status = "Thành viên ưu tú"

        print(
            f"{index}. Mã: {student['student_id']} | "
            f"Tên: {student['name']} | "
            f"Hiện có: {student['current_points']} | "
            f"Đã tiêu: {student['spent_points']} | "
            f"Hoàn trả: {student['refunded_points']} | "
            f"Hệ số: x{student['multiplier']} | "
            f"Trạng thái: {status}"
        )

    print("----------------------")


# Chức năng 2
def redeem_rewards(records):
    student_id = input(
        "Nhập mã học viên đổi quà: "
    ).strip().upper()

    student = find_student_by_id(records, student_id)

    if student is None:
        print("Không tìm thấy hồ sơ học viên!")
        return

    points = input_positive_int(
        "Nhập số điểm cần tiêu: "
    )

    if points > student["current_points"]:
        print("Số dư điểm không đủ để thực hiện giao dịch!")
        return

    student["current_points"] -= points
    student["spent_points"] += points

    print(
        f">> Giao dịch thành công! "
        f"'{student['name']}' đã tiêu {points} điểm. "
        f"Số dư còn lại: {student['current_points']} điểm."
    )


# Chức năng 3
def appeal_score(records):
    student_id = input(
        "Nhập mã học viên cần phúc khảo: "
    ).strip().upper()

    student = find_student_by_id(records, student_id)

    if student is None:
        print("Không tìm thấy hồ sơ học viên!")
        return

    points = input_positive_int(
        "Nhập số điểm hoàn lại: "
    )

    if points > student["spent_points"]:
        print(
            "Không thể hoàn số điểm lớn hơn "
            "tổng điểm đã tiêu!"
        )
        return

    student["spent_points"] -= points
    student["current_points"] += points
    student["refunded_points"] += points

    print(
        f">> Hoàn điểm thành công! "
        f"'{student['name']}' được cộng lại "
        f"{points} điểm."
    )


# Chức năng 4
def activate_multiplier(records):
    student_id = input(
        "Nhập mã học viên nhận hệ số: "
    ).strip().upper()

    student = find_student_by_id(records, student_id)

    if student is None:
        print("Không tìm thấy hồ sơ học viên!")
        return

    multiplier = input_multiplier()

    student["multiplier"] = multiplier

    print(
        f">> Đã kích hoạt hệ số x{multiplier} "
        f"cho học viên '{student['name']}'."
    )


# Chức năng 5
def grade_assignment(records):
    student_id = input(
        "Nhập mã học viên vừa nộp bài: "
    ).strip().upper()

    student = find_student_by_id(records, student_id)

    if student is None:
        print("Không tìm thấy hồ sơ học viên!")
        return

    base_points = input_positive_int(
        "Nhập số điểm gốc đạt được: "
    )

    earned_points = int(
        base_points * student["multiplier"]
    )

    student["current_points"] += earned_points

    print(
        f">> Hệ số hiện tại của "
        f"'{student['name']}' là "
        f"x{student['multiplier']}."
    )

    print(
        f">> Điểm thực nhận: "
        f"{earned_points}."
    )

    print(
        f">> Đã cộng {earned_points} điểm "
        f"vào tài khoản!"
    )


# Chương trình chính
while True:
    print("\n===== HỆ THỐNG NGÂN HÀNG ĐIỂM SỐ RIKKEI ACADEMY =====")
    print("1. Hiển thị sao kê điểm số")
    print("2. Đổi điểm lấy phần thưởng")
    print("3. Phúc khảo bài thi (Hoàn điểm)")
    print("4. Kích hoạt (Hệ số nhân điểm)")
    print("5. Chấm bài (thêm điểm)")
    print("6. Thoát chương trình")
    print("=====================================================")

    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        display_statements(student_records)

    elif choice == "2":
        redeem_rewards(student_records)

    elif choice == "3":
        appeal_score(student_records)

    elif choice == "4":
        activate_multiplier(student_records)

    elif choice == "5":
        grade_assignment(student_records)

    elif choice == "6":
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break

    else:
        print("Lựa chọn không hợp lệ!")