so_hang = int(input("Nhập số hàng: "))
so_ghe = int(input("Nhập số ghế: "))

for i in range(1, so_hang+1):
    if so_hang > 10 or so_hang <= 0:
        print("Dữ liệu không hợp lệ!")
        break
    else:
        for j in range(1, so_ghe+1):
            if so_ghe > 10 or so_ghe <= 0:
                print("Dữ liệu không hợp lệ!")
                break
            else:
                print("*", end="")
        print()
            