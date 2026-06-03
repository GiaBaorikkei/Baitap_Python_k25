branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = 2

for i in range(1, branch_count+1):
    print(f"Chi nhánh {i}")
    for j in range(1, 3):
        student_count = int(input(f"Nhập số lượng học viên đi học của lớp {j}: "))
        if student_count >= 20:
            print(f"Chi nhánh {i} - Lớp {j}: Lớp học ổn định")
        elif 0 < student_count < 20:
            print(f"Chi nhánh {i} - Lớp {j}: Lớp cần được nhắc nhở theo dõi")
        else:
            print(f"Chi nhánh {i} - Lớp {j}: Lớp vắng toàn bộ, bỏ qua đánh giá trạng thái")