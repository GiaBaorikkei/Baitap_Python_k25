from data.students import student_records

import reports.report_generator as rp

from utils.random_utils import (
    generate_assignment_code
)

import utils.string_utils as su


def main():

    while True:

        print(
"""
===== HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY =====
1. Xem danh sách sinh viên và điểm trung bình
2. Chuẩn hóa tên sinh viên
3. Sinh mã bài tập ngẫu nhiên
4. Xuất báo cáo học tập
5. Thoát chương trình
====================================================
"""
)

        try:

            choice = int(
                input(
                    "Chọn chức năng (1-5): "
                )
            )

            if choice == 1:

                rp.display_student_scores(
                    student_records
                )


            elif choice == 2:

                su.normalize_student_names(
                    student_records
                )


            elif choice == 3:

                print(
                    "\n--- SINH MÃ BÀI TẬP ---"
                )

                print(
                    "Mã bài tập của bạn là:",
                    generate_assignment_code()
                )


            elif choice == 4:

                rp.export_learning_report(
                    student_records
                )


            elif choice == 5:

                print(
                    "Cảm ơn bạn đã sử dụng hệ thống!"
                )

                break


            else:

                print(
                    "Chức năng không hợp lệ. "
                    "Vui lòng chọn từ 1 đến 5."
                )

        except ValueError:

            print(
                "Chức năng không hợp lệ. "
                "Vui lòng chọn từ 1 đến 5."
            )


main()