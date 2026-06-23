from datetime import datetime
from datetime import timedelta


def calculate_eta(
        flight_id,
        flight_list
):

    print(
        "\n----- TÍNH TOÁN "
        "THỜI GIAN HẠ CÁNH (ETA) -----"
    )

    search_id = input(
        "Nhập mã chuyến bay cần tính: "
    ).strip().upper()

    for flight in flight_list:

        if flight["flight_id"] == search_id:

            departure = datetime.strptime(
                flight["depart_time"],
                "%Y-%m-%d %H:%M:%S"
            )

            eta = departure + timedelta(
                minutes=flight["duration_min"]
            )

            print(
                f"-> Chuyến bay "
                f"{search_id} "
                f"cất cánh lúc: "
                f"{flight['depart_time']}"
            )

            print(
                f"-> Thời gian "
                f"hạ cánh dự kiến (ETA): "
                f"{eta}"
            )

            return

    print(
        "Không tìm thấy chuyến bay"
    )