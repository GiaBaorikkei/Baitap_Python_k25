import re

username = ""
title = ""
description = ""
hashtags = []

while True:
    print("\n===== MENU =====")
    print("1. Nhập dữ liệu và xem báo cáo thống kê")
    print("2. Chuẩn hóa tên tài khoản TikTok")
    print("3. Kiểm tra hashtag hợp lệ")
    print("4. Tìm kiếm và thay thế từ khóa")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn: ")

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue

    choice = int(choice)

    if choice < 1 or choice > 5:
        print("Lựa chọn không hợp lệ")
        continue
    if choice == 1:
        username = input("Nhập tên tài khoản: ").strip()

        if username == "":
            print("Tên tài khoản không được rỗng")
            continue

        title = input("Nhập tiêu đề video: ").strip()

        description = input("Nhập mô tả video: ").strip()

        if description == "":
            print("Mô tả video không được rỗng")
            continue

        hashtag_input = input("Nhập hashtag (cách nhau bởi dấu phẩy): ")

        hashtags = hashtag_input.split(",")

        for i in range(len(hashtags)):
            hashtags[i] = hashtags[i].strip()

        print("\n===== BÁO CÁO =====")
        print("Tên tài khoản:", username)
        print("Tiêu đề:", title.title())
        print("Mô tả:", description)

        print("Độ dài mô tả:", len(description))
        print("Số lượng từ:", len(description.split()))

        print("Danh sách hashtag:", hashtags)
        print("Số lượng hashtag:", len(hashtags))

        print("Mô tả chữ thường:")
        print(description.lower())

        print("Mô tả chữ hoa:")
        print(description.upper())

    elif choice == 2:

        if username == "":
            print("Chưa có dữ liệu tài khoản")
            continue

        tk_moi = username.lower().strip()

        if not tk_moi.startswith("@"):
            tk_moi = "@" + tk_moi

        print("Tên tài khoản ban đầu:", username)
        print("Tên tài khoản chuẩn hóa:", tk_moi)

    elif choice == 3:

        hashtag = input("Nhập hashtag cần kiểm tra: ").strip()

        if hashtag == "":
            print("Hashtag không được rỗng")

        elif not hashtag.startswith("#"):
            print("Hashtag phải bắt đầu bằng ký tự #")

        elif len(hashtag) < 2:
            print("Hashtag phải có ít nhất 2 ký tự")

        elif " " in hashtag:
            print("Hashtag không được chứa khoảng trắng")

        elif re.fullmatch(r"#[A-Za-z0-9_]+", hashtag) is None:
            print("Hashtag chỉ được chứa chữ cái, số hoặc dấu gạch dưới")

        else:
            print("Hashtag hợp lệ")
            hashtags.append(hashtag)

    elif choice == 4:

        if description == "":
            print("Chưa có mô tả video")
            continue

        tu_tim = input("Nhập từ khóa cần tìm: ")
        tu_moi = input("Nhập từ khóa thay thế: ")

        so_lan = description.count(tu_tim)

        if so_lan == 0:
            print("Không tìm thấy từ khóa")

        else:
            mo_ta_moi = description.replace(tu_tim, tu_moi)

            print("Mô tả sau khi thay thế:")
            print(mo_ta_moi)

            print("Số lần xuất hiện:", so_lan)

    elif choice == 5:
        print("Thoát chương trình")
        break