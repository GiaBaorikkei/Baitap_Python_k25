shop = ""
ten_san_pham = ""
mo_ta = ""
danh_muc = ""
tu_khoa = []

while True:
    print("\n===== MENU =====")
    print("1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê")
    print("2. Chuẩn hóa tên Shop")
    print("3. Kiểm tra mã giảm giá hợp lệ")
    print("4. Tìm kiếm và thay thế từ khóa trong mô tả sản phẩm")
    print("5. Thoát chương trình")

    lua_chon = input("Nhập lựa chọn: ")

    if not lua_chon <= 0:
        print("Lựa chọn không hợp lệ")
        continue

    lua_chon = int(lua_chon)

    if lua_chon < 1 or lua_chon > 5:
        print("Lựa chọn không hợp lệ")
        continue

    if lua_chon == 1:

        shop = input("Nhập tên shop: ").strip()

        if shop == "":
            print("Tên shop không được bỏ trống")
            continue

        ten_san_pham = input("Nhập tên sản phẩm: ").strip()

        mo_ta = input("Nhập mô tả sản phẩm: ").strip()

        if mo_ta == "":
            print("Mô tả sản phẩm không được rỗng")
            continue

        danh_muc = input("Nhập danh mục sản phẩm: ").strip().lower()

        ds_tu_khoa = input(
            "Nhập danh sách từ khóa (cách nhau bởi dấu phẩy): "
        )

        tu_khoa = ds_tu_khoa.split(",")

        for i in range(len(tu_khoa)):
            tu_khoa[i] = tu_khoa[i].strip()

        print("\n===== BÁO CÁO THỐNG KÊ =====")

        print("Tên shop:", shop)

        print("Tên sản phẩm:", ten_san_pham.title())

        print("Mô tả sản phẩm:", mo_ta)

        print("Độ dài mô tả sản phẩm:", len(mo_ta))

        print("Danh mục sản phẩm:", danh_muc)

        print("Danh sách từ khóa:", tu_khoa)

        print("Số lượng từ khóa:", len(tu_khoa))

        print("Mô tả chữ thường:")
        print(mo_ta.lower())

        print("Mô tả chữ hoa:")
        print(mo_ta.upper())

    elif lua_chon == 2:

        if shop == "":
            print("Chưa có dữ liệu shop")
            continue

        shop_moi = shop.strip().lower()

        shop_moi = shop_moi.replace(" ", "-")

        if not shop_moi.startswith("shop-"):
            shop_moi = "shop-" + shop_moi

        print("Tên shop ban đầu:", shop)
        print("Tên shop chuẩn hóa:", shop_moi)

    elif lua_chon == 3:

        ma = input("Nhập mã giảm giá: ")

        if ma == "":
            print("Mã giảm giá không được rỗng")

        elif " " in ma:
            print("Mã giảm giá không được chứa khoảng trắng")

        elif len(ma) < 6 or len(ma) > 12:
            print("Mã giảm giá phải có độ dài từ 6 đến 12 ký tự")

        elif ma != ma.upper():
            print("Mã giảm giá phải được viết hoa toàn bộ")

        elif not ma.startswith("SALE"):
            print("Mã giảm giá phải bắt đầu bằng SALE")

        elif not ma.isalnum():
            print("Mã giảm giá chỉ được chứa chữ cái và chữ số")

        else:
            print("Mã giảm giá hợp lệ")

    elif lua_chon == 4:

        if mo_ta == "":
            print("Chưa có mô tả sản phẩm")
            continue

        tu_tim = input("Nhập từ khóa cần tìm: ")
        tu_thay = input("Nhập từ khóa thay thế: ")

        so_lan = mo_ta.count(tu_tim)

        if so_lan == 0:
            print("Không tìm thấy từ khóa")

        else:
            mo_ta_moi = mo_ta.replace(tu_tim, tu_thay)

            print("Số lần xuất hiện của từ khóa:", so_lan)

            print("Mô tả sau khi thay thế:")
            print(mo_ta_moi)

    elif lua_chon == 5:
        print("Thoát chương trình")
        break