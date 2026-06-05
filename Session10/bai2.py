playlist = []

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ DANH SÁCH PHÁT NHẠC =====")
    print("1. Thêm bài hát vào danh sách phát")
    print("2. Xem danh sách phát")
    print("3. Xóa bài hát khỏi danh sách")
    print("4. Sắp xếp và Trích xuất danh sách")
    print("5. Thoát chương trình")

    choice = input("Chọn chức năng: ")

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
        continue

    choice = int(choice)

    if choice == 1:
        print("\n1. Thêm vào cuối danh sách")
        print("2. Chèn vào vị trí bất kỳ")

        sub = input("Lựa chọn: ")

        if not sub.isdigit():
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
            continue

        sub = int(sub)

        song = input("Nhập tên bài hát: ")

        if sub == 1:
            playlist.append(song)
            print("Thêm bài hát thành công!")
            print("Số lượng bài hát hiện tại:", len(playlist))

        elif sub == 2:
            index = input("Nhập vị trí muốn chèn: ")

            if not index.isdigit():
                print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
                continue

            index = int(index)

            if index < 1 or index > len(playlist) + 1:
                print("Vị trí không hợp lệ.")
            else:
                playlist.insert(index - 1, song)
                print("Thêm bài hát thành công!")
                print("Số lượng bài hát hiện tại:", len(playlist))

        else:
            print("Lựa chọn không hợp lệ.")

    elif choice == 2:
        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
        else:
            print("\n===== DANH SÁCH PHÁT =====")
            for i in range(len(playlist)):
                print(i + 1, ".", playlist[i])

    elif choice == 3:
        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
            continue

        print("\n1. Xóa theo tên bài hát")
        print("2. Xóa theo số thứ tự")

        sub = input("Lựa chọn: ")

        if not sub.isdigit():
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
            continue

        sub = int(sub)

        if sub == 1:
            song = input("Nhập tên bài hát cần xóa: ")

            if song in playlist:
                playlist.remove(song)
                print("Đã xóa bài hát", song, "khỏi danh sách")
            else:
                print("Không tìm thấy bài hát trong danh sách phát.")

        elif sub == 2:
            index = input("Nhập số thứ tự bài hát cần xóa: ")

            if not index.isdigit():
                print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
                continue

            index = int(index)

            if index < 1 or index > len(playlist):
                print("Vị trí không hợp lệ.")
            else:
                song = playlist.pop(index - 1)
                print("Đã xóa bài hát", song, "khỏi danh sách")

    elif choice == 4:
        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
            continue

        print("\n1. Sắp xếp theo bảng chữ cái")
        print("2. Hiển thị 3 bài hát đầu tiên")

        sub = input("Lựa chọn: ")

        if not sub.isdigit():
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
            continue

        sub = int(sub)

        if sub == 1:
            playlist.sort()

            print("\nDanh sách sau khi sắp xếp:")
            for i in range(len(playlist)):
                print(i + 1, ".", playlist[i])

        elif sub == 2:
            print("\n3 bài hát đầu tiên:")
            for song in playlist[:3]:
                print(song)

    elif choice == 5:
        print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
        break

    else:
        print("Lựa chọn không hợp lệ.")