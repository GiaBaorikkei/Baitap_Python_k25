a = 79
for i in range(1,6):
    print("Lượt đoán", i)
    b = int(input("Nhập số dự đoán: "))
    if b < a:
        print("Gợi ý: Số của bạn nhỏ hơn số may mắn")
    elif b > a:
        print("Gợi ý: Số của bạn lớn hơn số may mắn")
    else:
        print("Chúc mừng! Bạn đã đoán chính xác số may mắn!")
        break
print("-- TRÒ CHƠI KẾT THÚC --")
        
    