from datetime import datetime

def to_time(t):
    return datetime.strptime(t, "%H:%M")


def evaluate_flex_time(attendance_book):
    for emp in attendance_book:
        emp_id = emp["id"]
        time_in, time_out = emp["times"]

        if time_out is None:
            continue

        in_t = to_time(time_in)
        out_t = to_time(time_out)

        # Vi phạm đi muộn
        if in_t > to_time("10:00"):
            print(f"{emp_id} - Vi phạm: Đến muộn quá 90 phút.")
            continue

        worked_hours = (out_t - in_t).seconds / 3600

        if worked_hours < 9:
            print(f"{emp_id} - Vi phạm: Về sớm, chưa đủ 9 tiếng.")
        else:
            print(f"{emp_id} - Hợp lệ: Hoàn thành ca làm việc.")