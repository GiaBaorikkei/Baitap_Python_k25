import math


def show_flight_schedule(flight_list):

    print("\n----- DANH SÁCH CHUYẾN BAY & HẬU CẦN -----")

    for index, flight in enumerate(flight_list,1):

        reserve_water = math.ceil(
            flight["passengers"]/10
        )

        print(
            f"{index}. "
            f"Mã: {flight['flight_id']} | "
            f"Khởi hành: {flight['depart_time']} | "
            f"Số khách: {flight['passengers']} | "
            f"Dự phòng: {reserve_water} thùng nước"
        )