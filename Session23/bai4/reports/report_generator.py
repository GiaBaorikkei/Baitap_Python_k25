from datetime import datetime
from colorama import Fore

from utils.score_utils import (
    calculate_average,
    classify_student
)


def display_student_scores(records):

    if not records:

        print(
            "Hệ thống chưa có dữ liệu sinh viên."
        )

        return

    print(
        "\n--- DANH SÁCH ĐIỂM SINH VIÊN ---"
    )

    for index, student in enumerate(
        records,
        1
    ):

        average = calculate_average(
            student["scores"]
        )

        rank = classify_student(
            average
        )

        print(
            f"{index}. "
            f"[{student['student_id']}] "
            f"{student['name']} | "
            f"Điểm: {student['scores']} | "
            f"ĐTB: {average:.2f} - "
            f"{rank}"
        )

    print("-"*35)


def export_learning_report(records):

    if not records:

        print(
            "Hệ thống chưa có dữ liệu sinh viên."
        )

        return

    total_students = len(records)

    passed_students = 0

    failed_students = 0


    for student in records:

        average = calculate_average(
            student["scores"]
        )

        if average >= 5:
            passed_students += 1

        else:
            failed_students += 1


    created_time = datetime.now()


    with open(
        "learning_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "===== BÁO CÁO HỌC TẬP =====\n"
        )

        file.write(
            f"Thời gian tạo: "
            f"{created_time}\n"
        )

        file.write(
            f"Tổng số sinh viên: "
            f"{total_students}\n"
        )

        file.write(
            f"Số đạt yêu cầu: "
            f"{passed_students}\n"
        )

        file.write(
            f"Số cần cải thiện: "
            f"{failed_students}\n"
        )

    print(
        "\n--- XUẤT BÁO CÁO HỌC TẬP ---"
    )

    print(
        f"Tổng số sinh viên: "
        f"{total_students}"
    )

    print(
        f"Số sinh viên đạt yêu cầu: "
        f"{passed_students}"
    )

    print(
        f"Số sinh viên cần cải thiện: "
        f"{failed_students}"
    )

    print(
        Fore.GREEN
        + ">> Đã xuất báo cáo ra file learning_report.txt"
    )