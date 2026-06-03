tuoi = int(input("Nhập tuổi của bệnh nhân: "))
huyet_ap = int(input("Nhập huyết áp của bệnh nhân (mmHg): "))
duong_huyet = int(input("Nhập đường huyết của bệnh nhân (mg/dL): "))

if tuoi < 75 and 90 <= huyet_ap <= 120 and duong_huyet < 150:
    print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT.")
else:
    print("TỪ CHỐI PHẪU THUẬT.")