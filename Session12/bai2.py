saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán hoặc xóa sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    if choice == "1":
        if len(saving_accounts) == 0:
            print("Danh sách sổ tiết kiệm hiện đang trống")
        else:
            print("\nDanh sách sổ tiết kiệm:")
            for i, account in enumerate(saving_accounts, start=1):
                print(
                    f"{i}. Mã sổ: {account['account_id']} | "
                    f"Khách hàng: {account['customer_name']} | "
                    f"Số tiền gửi: {account['balance']} | "
                    f"Kỳ hạn: {account['term_months']} tháng | "
                    f"Lãi suất: {account['interest_rate']}%/năm | "
                    f"Trạng thái: {account['status']}"
                )

    elif choice == "2":
        account_id = input("Nhập mã sổ tiết kiệm: ").strip().upper()

        existed = False

        for account in saving_accounts:
            if account["account_id"] == account_id:
                existed = True
                break

        if existed:
            print("Mã sổ tiết kiệm đã tồn tại!")

        else:
            customer_name = input("Nhập tên khách hàng: ").strip().title()

            if customer_name == "":
                print("Tên khách hàng không được để trống")

            else:
                balance = input("Nhập số tiền gửi: ").strip()
                term_months = input("Nhập kỳ hạn gửi theo tháng: ").strip()

                if (
                    not balance.isdigit()
                    or not term_months.isdigit()
                    or int(balance) <= 0
                    or int(term_months) <= 0
                ):
                    print("Số tiền gửi hoặc kỳ hạn không hợp lệ")

                else:
                    interest_rate = input("Nhập lãi suất năm: ").strip()

                    if (
                        not interest_rate.replace(".", "", 1).isdigit()
                        or float(interest_rate) <= 0
                    ):
                        print("Lãi suất không hợp lệ!")

                    else:
                        saving_accounts.append({
                            "account_id": account_id,
                            "customer_name": customer_name,
                            "balance": int(balance),
                            "term_months": int(term_months),
                            "interest_rate": float(interest_rate),
                            "status": "active"
                        })

                        print("Mở sổ tiết kiệm thành công!")

    elif choice == "3":
        account_id = input(
            "Nhập mã sổ tiết kiệm cần cập nhật: "
        ).strip().upper()

        found = False

        for account in saving_accounts:
            if account["account_id"] == account_id:
                found = True

                if account["status"] == "closed":
                    print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
                    break

                customer_name = input(
                    "Nhập tên khách hàng mới: "
                ).strip()

                if customer_name == "":
                    print("Tên khách hàng không được để trống")
                    break

                balance = input(
                    "Nhập số tiền gửi mới: "
                ).strip()

                term_months = input(
                    "Nhập kỳ hạn mới theo tháng: "
                ).strip()

                if (
                    not balance.isdigit()
                    or not term_months.isdigit()
                    or int(balance) <= 0
                    or int(term_months) <= 0
                ):
                    print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                    break

                interest_rate = input(
                    "Nhập lãi suất năm mới: "
                ).strip()

                if (
                    not interest_rate.replace(".", "", 1).isdigit()
                    or float(interest_rate) <= 0
                ):
                    print("Lãi suất không hợp lệ!")
                    break

                account["customer_name"] = customer_name
                account["balance"] = int(balance)
                account["term_months"] = int(term_months)
                account["interest_rate"] = float(interest_rate)

                print("Cập nhật thành công!")
                break

        if not found:
            print("Không tìm thấy mã sổ tiết kiệm!")

    elif choice == "4":
        account_id = input(
            "Nhập mã sổ tiết kiệm cần tất toán/xóa: "
        ).strip().upper()

        found = False

        for account in saving_accounts:
            if account["account_id"] == account_id:
                account["status"] = "closed"
                found = True
                print("Tất toán sổ thành công!")
                break

        if not found:
            print("Không tìm thấy mã sổ tiết kiệm")

    elif choice == "5":
        account_id = input(
            "Nhập mã sổ tiết kiệm cần tính lãi: "
        ).strip().upper()

        found = False

        for account in saving_accounts:
            if account["account_id"] == account_id:
                found = True

                if account["status"] == "closed":
                    print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                    break

                interest = (
                    account["balance"]
                    * account["interest_rate"]
                    / 100
                    * account["term_months"]
                    / 12
                )

                total = account["balance"] + interest

                print(f"Tiền lãi dự kiến: {interest:,.0f}")
                print(f"Tổng tiền nhận khi đến hạn: {total:,.0f}")
                break

        if not found:
            print("Không tìm thấy mã sổ tiết kiệm")

    elif choice == "6":
        account_id = input(
            "Nhập mã sổ tiết kiệm cần kiểm tra: "
        ).strip().upper()

        found = False

        for account in saving_accounts:
            if account["account_id"] == account_id:
                found = True

                if account["status"] == "closed":
                    print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                    break

                actual_months = input(
                    "Nhập số tháng thực gửi: "
                ).strip()

                if (
                    not actual_months.isdigit()
                    or int(actual_months) <= 0
                ):
                    print("Số tháng thực gửi không hợp lệ!")
                    break

                actual_months = int(actual_months)

                if actual_months < account["term_months"]:
                    rate = 0.5
                    print("Khách hàng rút trước hạn")
                else:
                    rate = account["interest_rate"]
                    print("Khách hàng đủ điều kiện hưởng lãi đúng hạn")

                interest = (
                    account["balance"]
                    * rate
                    / 100
                    * actual_months
                    / 12
                )

                total = account["balance"] + interest

                print(f"Lãi suất áp dụng: {rate}%")
                print(f"Tiền lãi thực nhận: {interest:,.0f}")
                print(f"Tổng tiền thực nhận: {total:,.0f}")
                break

        if not found:
            print("Không tìm thấy mã sổ tiết kiệm")

    elif choice == "7":
        print("Thoát chương trình!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại")