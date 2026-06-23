import os


def create_folder():

    print(
        "\n----- KHỞI TẠO "
        "THƯ MỤC HỆ THỐNG -----"
    )

    folder_name = "aviation_logs"

    if not os.path.exists(
            folder_name
    ):

        print(
            "[SYSTEM] "
            "Thư mục chưa tồn tại."
        )

        os.mkdir(
            folder_name
        )

        print(
            "[SYSTEM] "
            "Tạo thư mục thành công!"
        )

    else:

        print(
            "Thư mục đã tồn tại, "
            "bỏ qua bước khởi tạo"
        )