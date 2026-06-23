from datetime import datetime

def find_employee(book, emp_id):
    for i, emp in enumerate(book):
        if emp["id"] == emp_id:
            return i
    return -1


def clock_in(attendance_book):
    while True:
        emp_id = input("Nhập mã nhân viên: ").strip().upper()

        exists = False
        for emp in attendance_book:
            if emp["id"].upper() == emp_id:
                exists = True
                break

        if exists:
            print("Mã nhân viên đã tồn tại! Vui lòng nhập lại.")
            continue

        name = input("Nhập tên nhân viên: ").strip().title()
        time_in = input("Nhập giờ vào (HH:MM): ").strip()

        attendance_book.append({
            "id": emp_id,
            "name": name,
            "times": (time_in, None)
        })

        print(f"Thành công: Đã ghi nhận {emp_id} chấm công vào lúc {time_in}!")
        break


def clock_out(attendance_book):
    while True:
        emp_id = input("Nhập mã nhân viên: ")
        time_out = input("Nhập giờ ra (HH:MM): ")

        idx = find_employee(attendance_book, emp_id)

        if idx == -1:
            print("Không tìm thấy nhân viên!")
            return

        emp = attendance_book[idx]
        time_in = emp["times"][0]

        emp["times"] = (time_in, time_out)

        print(f"Đã cập nhật giờ ra cho {emp_id} lúc {time_out}")