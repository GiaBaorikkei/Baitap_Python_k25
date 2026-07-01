from abc import ABC, abstractmethod

class BaseVehicle(ABC):
    def __init__(self, plate):
        self.plate = plate
        self.__odometer = 0
        
    @property
    def odometer(self):
        return self.__odometer
    @abstractmethod
    def calculate_efficiency(self):
        pass
    
    def drive(self, distance):
        if distance > 0:
            self.__odometer += distance
        else:
            print("Số km phải lớn hơn 0")
    
    def __it__(self, other):
        return self.odometer < other.odometer
    
    @staticmethod
    def validate_license_plate(plate):
        return len(plate) == 9 and plate.startswith("29")
    
class AutonomousFeature:
    def calculate_efficiency(self):
        return 95.0
    
class ElectricBus(BaseVehicle):
    def calculate_efficiency(self):
        efficiency = 100 - (self.odometer * 0.005)

        if efficiency < 50:
            return 50.0

        return efficiency

class RoboBus(ElectricBus, AutonomousFeature):
    def calculate_efficiency(self):
        electric = ElectricBus.calculate_efficiency(self)
        auto = AutonomousFeature.calculate_efficiency(self)

        return (electric + auto) / 2
    
current_vehicle = None

while True:

    print("\n====== SMART TRANSIT MENU ======")
    print("1. Khởi tạo & Đăng ký xe lai RoboBus mới")
    print("2. Giả lập vận hành & Kiểm tra hiệu suất")
    print("0. Thoát")

    choice = input("Chọn chức năng: ")

    if choice == "1":

        print("\n--- KHỞI TẠO XE LAI ROBOBUS ---")

        while True:
            plate = input("Nhập biển số xe (9 ký tự, bắt đầu bằng 29): ")

            if BaseVehicle.validate_license_plate(plate):
                current_vehicle = RoboBus(plate)

                print("\n[Thành công]: Khởi tạo phương tiện RoboBus thành công!")

                print("[MRO Architecture]: ", end="")
                print(
                    " -> ".join(cls.__name__ for cls in RoboBus.__mro__)
                )

                break
            else:
                print("Biển số không hợp lệ! Nhập lại.")

    elif choice == "2":

        if current_vehicle is None:
            print("Chưa có RoboBus nào được tạo!")
            continue

        print("\n--- GIẢ LẬP VẬN HÀNH PHƯƠNG TIỆN ---")

        try:

            distance = float(
                input("Nhập số km di chuyển mới phát sinh: ")
            )

            current_vehicle.drive(distance)

            print("\n[Thành công]: Cập nhật lộ trình xe chạy thành công.")

            print(
                f"Tổng quãng đường tích lũy (Odometer): {current_vehicle.odometer:.1f} km"
            )

            print(
                f"Hiệu suất tiêu thụ năng lượng tích hợp: {current_vehicle.calculate_efficiency():.1f}%"
            )

        except ValueError as e:
            print("Lỗi:", e)

    elif choice == "0":
        print("Tạm biệt!")
        break

    else:
        print("Lựa chọn không hợp lệ.")
        
