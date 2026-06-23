from tabulate import tabulate

def display_records(attendance_book):
    if not attendance_book:
        print("Không có dữ liệu.")
        return

    table = []

    for emp in attendance_book:
        clock_in, clock_out = emp["times"]

        if clock_out is None:
            clock_out = "[Đang làm việc]"

        table.append([
            emp["id"],
            emp["name"],
            clock_in,
            clock_out
        ])

    print("\n--- BẢNG CHẤM CÔNG ---")
    print(tabulate(table, headers=["Mã NV", "Tên", "Giờ Vào", "Giờ Ra"]))
    print("-" * 40)