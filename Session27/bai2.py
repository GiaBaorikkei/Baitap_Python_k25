from abc import ABC, abstractmethod

# ==========================================
# 1. ABSTRACT BASE CLASS
# ==========================================
class BaseProduct(ABC):
    """
    Lớp trừu tượng định nghĩa bộ khung chuẩn cho mọi loại hàng hóa trong kho.
    Bẫy 1: Kế thừa từ ABC ngăn chặn việc khởi tạo trực tiếp đối tượng từ lớp này (ném TypeError).
    """
    warehouse_name = "Amazon Logistics"
    base_storage_fee = 5000

    def __init__(self, product_code, product_name):
        self.product_code = product_code
        # Chuẩn hóa tên sản phẩm (In hoa, xóa khoảng trắng thừa)
        self.product_name = " ".join(product_name.strip().upper().split())
        self.__stock_quantity = 0  # Private Attribute: Đóng gói số lượng tồn kho

    # @property: Tạo getter an toàn cho thuộc tính private, ngăn việc gán giá trị bừa bãi
    @property
    def stock_quantity(self):
        return self.__stock_quantity

    def _update_stock(self, quantity):
        """Hàm nội bộ (Protected) để các lớp con cập nhật tồn kho an toàn."""
        self.__stock_quantity += quantity

    # @abstractmethod: Ép buộc tất cả các lớp con phải ghi đè các hàm này
    @abstractmethod
    def import_stock(self, quantity):
        pass

    @abstractmethod
    def export_stock(self, quantity):
        pass

    # Operator Overloading: Nạp chồng toán tử cộng (+)
    def __add__(self, other):
        # Bẫy 3: Kiểm tra kiểu dữ liệu khi Overloading
        if not isinstance(other, BaseProduct):
            return NotImplemented
        return self.stock_quantity + other.stock_quantity

    # Operator Overloading: Nạp chồng toán tử so sánh nhỏ hơn (<)
    def __lt__(self, other):
        if not isinstance(other, BaseProduct):
            return NotImplemented
        return self.stock_quantity < other.stock_quantity

    # @staticmethod: Hàm tĩnh không cần truy cập instance (self) hay class (cls)
    @staticmethod
    def validate_product_code(product_code):
        # Bắt đầu bằng chữ và có đúng 10 ký tự
        return len(product_code) == 10 and product_code[0].isalpha()

    # @classmethod: Hàm thao tác trực tiếp với Class, áp dụng cho toàn hệ thống
    @classmethod
    def update_warehouse_name(cls, new_name):
        cls.warehouse_name = new_name


# ==========================================
# 2. SUBCLASSES (KẾ THỪA)
# ==========================================
class ColdStorageProduct(BaseProduct):
    def __init__(self, product_code, product_name, required_temperature):
        super().__init__(product_code, product_name)
        self.required_temperature = required_temperature

    def import_stock(self, quantity):
        if quantity > 0:
            self._update_stock(quantity)

    def export_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Số lượng xuất phải lớn hơn 0.")
        
        # Đặc thù: Chịu 5% phí hao hụt bảo quản phụ trội
        loss = quantity * 0.05
        total_deduction = quantity + loss
        
        if self.stock_quantity >= total_deduction:
            self._update_stock(-total_deduction)
            return quantity, loss
        else:
            raise ValueError("Số lượng tồn kho không đủ để xuất và chịu hao hụt.")

    def apply_cooling_cost(self):
        # Giả định: Mỗi đơn vị tính phí 3,000 VND
        return self.stock_quantity * 3000


class HazardousProduct(BaseProduct):
    def __init__(self, product_code, product_name, max_safety_limit):
        super().__init__(product_code, product_name)
        self.max_safety_limit = max_safety_limit

    def import_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Số lượng nhập phải lớn hơn 0.")
        
        # Bẫy 2: Kiểm tra hạn mức lưu trữ an toàn tối đa
        if self.stock_quantity + quantity > self.max_safety_limit:
            raise ValueError(f"Giao dịch thất bại! Số lượng nhập vào khiến tồn kho vượt quá hạn mức an toàn cho phép (Tối đa: {self.max_safety_limit}).")
        
        self._update_stock(quantity)

    def export_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Số lượng xuất phải lớn hơn 0.")
        
        if self.stock_quantity >= quantity:
            self._update_stock(-quantity)
            return quantity, 0
        else:
            raise ValueError("Số lượng tồn kho không đủ.")


class HybridPremiumProduct(ColdStorageProduct, HazardousProduct):
    """
    Multiple Inheritance: Đa kế thừa.
    MRO: HybridPremiumProduct -> ColdStorageProduct -> HazardousProduct -> BaseProduct -> ABC
    """
    def __init__(self, product_code, product_name, required_temperature, max_safety_limit):
        # Khởi tạo Base để đồng bộ thuộc tính
        BaseProduct.__init__(self, product_code, product_name)
        self.required_temperature = required_temperature
        self.max_safety_limit = max_safety_limit

    def import_stock(self, quantity):
        # Tích hợp cơ chế chặn giới hạn an toàn của HazardousProduct
        HazardousProduct.import_stock(self, quantity)

    def export_stock(self, quantity):
        # Tích hợp cơ chế hao hụt của ColdStorageProduct
        return ColdStorageProduct.export_stock(self, quantity)


# ==========================================
# 3. DUCK TYPING (ĐỐI TÁC VẬN CHUYỂN)
# ==========================================
class FedExCarrier:
    def ship_package(self, product, quantity):
        drawn, _ = product.export_stock(quantity)
        return f"[Hệ thống FedEx]: Đang tiếp nhận mã sản phẩm {product.product_code}...\nXác thực đối tác bằng Duck Typing thành công!\nĐơn vị vận chuyển đã tiếp nhận đơn hàng số lượng: {drawn} đơn vị."

class DHLCarrier:
    def ship_package(self, product, quantity):
        drawn, _ = product.export_stock(quantity)
        return f"[Hệ thống DHL]: Xác thực kiện hàng {product.product_code}...\nXác thực đối tác bằng Duck Typing thành công!\nĐơn vị vận chuyển đã tiếp nhận đơn hàng số lượng: {drawn} đơn vị."

class InvalidCarrier:
    # Lớp giả lập bẫy lỗi Duck Typing (Không có hàm ship_package)
    def pack(self):
        pass

def dispatch_to_carrier(carrier_agent, product, quantity):
    """
    Duck Typing: Hàm không kiểm tra kiểu của carrier_agent,
    miễn là nó có phương thức `ship_package` thì có thể gọi.
    """
    try:
        # Bẫy 4: Sai lệch phương thức trong Duck Typing
        return carrier_agent.ship_package(product, quantity)
    except AttributeError:
        raise AttributeError("Đơn vị vận chuyển không hợp lệ hoặc chưa ký kết hợp đồng kỹ thuật.")


# ==========================================
# 4. HỆ THỐNG MENU CLI (NGHIỆP VỤ)
# ==========================================
def main():
    products = []
    current_product = None

    while True:
        print("\n===== AMAZON INVENTORY SIMULATOR PRO =====")
        print("1. Đăng ký mã hàng hóa mới (Chọn loại sản phẩm)")
        print("2. Xem thông tin & Kiểm tra thứ tự kế thừa (MRO)")
        print("3. Giao dịch Nhập / Xuất kho (Đa hình)")
        print("4. Kiểm tra điều kiện bảo quản / Tính chi phí phụ trội")
        print("5. Kiểm tra tính năng gộp lô hàng & So sánh tồn kho (Overloading)")
        print("6. Điều phối vận chuyển qua Đối tác thứ ba (Duck Typing)")
        print("7. Thoát chương trình")
        print("==========================================")
        
        choice = input("Chọn chức năng (1-7): ")

        if choice == '1':
            print("\n--- CHỌN LOẠI SẢN PHẨM KHỞI TẠO ---")
            print("1. Cold Storage Product (Hàng Đông Lạnh)")
            print("2. Hazardous Product (Hàng Nguy Hiểm)")
            print("3. Hybrid Premium Product (Hàng Lai Cao Cấp)")
            type_choice = input("Chọn loại sản phẩm (1-3): ")
            
            p_code = input("Nhập mã sản phẩm 10 ký tự: ")
            if not BaseProduct.validate_product_code(p_code):
                print("Mã sản phẩm không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng chữ.")
                continue
                
            p_name = input("Nhập tên sản phẩm: ")
            
            try:
                if type_choice == '1':
                    temp = float(input("Nhập nhiệt độ bảo quản yêu cầu (độ C): "))
                    new_prod = ColdStorageProduct(p_code, p_name, temp)
                    print(f"\nĐăng ký sản phẩm Đông Lạnh thành công!\nTên sản phẩm: {new_prod.product_name}")
                elif type_choice == '2':
                    limit = int(input("Nhập hạn mức lưu trữ tối đa an toàn: "))
                    new_prod = HazardousProduct(p_code, p_name, limit)
                    print(f"\nĐăng ký sản phẩm Nguy Hiểm thành công!\nTên sản phẩm: {new_prod.product_name}")
                elif type_choice == '3':
                    temp = float(input("Nhập nhiệt độ bảo quản yêu cầu (độ C): "))
                    limit = int(input("Nhập hạn mức lưu trữ tối đa an toàn: "))
                    new_prod = HybridPremiumProduct(p_code, p_name, temp, limit)
                    print(f"\nĐăng ký sản phẩm Lai Cao Cấp thành công!\nTên sản phẩm: {new_prod.product_name}")
                else:
                    print("Loại sản phẩm không hợp lệ.")
                    continue
                
                products.append(new_prod)
                current_product = new_prod
            except ValueError:
                print("Dữ liệu nhập vào không hợp lệ (cần là số).")

        elif choice == '2':
            if not current_product:
                print("Hệ thống chưa có thông tin sản phẩm. Vui lòng đăng ký ở Chức năng 1 trước.")
                continue
            
            print("\n--- THÔNG TIN SẢN PHẨM HIỆN TẠI ---")
            print(f"Loại sản phẩm: {current_product.__class__.__name__}")
            print(f"Chuỗi kho: {current_product.warehouse_name}")
            print(f"Mã sản phẩm: {current_product.product_code}")
            print(f"Tên sản phẩm: {current_product.product_name}")
            print(f"Số lượng tồn kho: {current_product.stock_quantity:,.0f} đơn vị")
            
            if hasattr(current_product, 'required_temperature'):
                print(f"Nhiệt độ yêu cầu: {current_product.required_temperature} độ C")
            if hasattr(current_product, 'max_safety_limit'):
                print(f"Hạn mức an toàn tối đa: {current_product.max_safety_limit:,.0f} đơn vị")
                
            print("\n[Cấu trúc MRO]:", [cls.__name__ for cls in current_product.__class__.mro()])

        elif choice == '3':
            if not current_product:
                print("Vui lòng đăng ký sản phẩm trước.")
                continue
                
            print("\n--- GIAO DỊCH NHẬP / XUẤT KHO ---")
            print("1. Nhập kho")
            print("2. Xuất kho")
            action = input("Chọn giao dịch (1-2): ")
            
            try:
                qty = float(input("Nhập số lượng: "))
                if action == '1':
                    current_product.import_stock(qty)
                    print("\nNhập kho thành công!")
                    print(f"Tồn kho mới: {current_product.stock_quantity:,.0f} đơn vị")
                elif action == '2':
                    drawn, loss = current_product.export_stock(qty)
                    print("\nXuất kho thành công!")
                    print(f"Số lượng yêu cầu: {drawn:,.0f} đơn vị")
                    if loss > 0:
                        print(f"Số lượng hao hụt bảo quản (5%): {loss} đơn vị")
                        print(f"Tổng số lượng khấu trừ trong kho: {drawn + loss} đơn vị")
                    print(f"Tồn kho hiện tại: {current_product.stock_quantity:,.0f} đơn vị")
            except ValueError as e:
                print(f"\n{e}")

        elif choice == '4':
            if not current_product:
                print("Vui lòng đăng ký sản phẩm trước.")
                continue
            
            if hasattr(current_product, 'apply_cooling_cost'):
                print("\n--- TÍNH PHÍ BẢO QUẢN ĐÔNG LẠNH ---")
                print(f"Số lượng tồn kho hiện tại: {current_product.stock_quantity:,.0f} đơn vị")
                print(f"Nhiệt độ yêu cầu: {current_product.required_temperature} độ C")
                cost = current_product.apply_cooling_cost()
                print(f"Chi phí làm lạnh phát sinh trong ngày: +{cost:,.0f} VND")
            else:
                print("Sản phẩm này không hỗ trợ tính năng làm lạnh phụ trội.")

        elif choice == '5':
            if not current_product or len(products) < 2:
                print("Hệ thống cần ít nhất 2 sản phẩm để thực hiện chức năng này.")
                continue
                
            print("\n--- ĐỒNG BỘ & SO SÁNH TỒN KHO (OPERATOR OVERLOADING) ---")
            print(f"Sản phẩm hiện tại (A): {current_product.product_name} (Tồn kho: {current_product.stock_quantity:,.0f} đơn vị)")
            
            print("Danh sách sản phẩm đối ứng (B):")
            for idx, p in enumerate(products):
                if p != current_product:
                    print(f"{idx}. {p.product_code} ({p.product_name} - Tồn kho: {p.stock_quantity:,.0f} đơn vị)")
                    
            try:
                target_idx = int(input("Chọn số thứ tự sản phẩm đối ứng: "))
                target_p = products[target_idx]
                
                # Gọi Overloading (__lt__)
                compare_str = "ÍT HƠN" if current_product < target_p else "NHIỀU HƠN HOẶC BẰNG"
                print(f"\n[Kết quả So sánh (__lt__)]: Tồn kho sản phẩm A {compare_str} tồn kho sản phẩm B.")
                
                # Gọi Overloading (__add__)
                total_qty = current_product + target_p
                print(f"[Kết quả Tổng hợp (__add__)]: Tổng số lượng tồn kho của cả 2 mã sản phẩm là: {total_qty:,.0f} đơn vị.")
            except (ValueError, IndexError):
                print("Lựa chọn không hợp lệ.")

        elif choice == '6':
            if not current_product:
                print("Vui lòng đăng ký sản phẩm trước.")
                continue
                
            print("\n--- ĐIỀU PHỐI ĐƠN VỊ VẬN CHUYỂN NGOÀI ---")
            print("1. Vận chuyển qua đối tác FedEx")
            print("2. Vận chuyển qua đối tác DHL")
            print("3. Test Bẫy Duck Typing (Cổng lỗi)")
            gw_choice = input("Chọn đối tác vận chuyển (1-3): ")
            
            try:
                qty = float(input("Nhập số lượng hàng hóa bàn giao: "))
                
                if gw_choice == '1':
                    carrier = FedExCarrier()
                elif gw_choice == '2':
                    carrier = DHLCarrier()
                elif gw_choice == '3':
                    carrier = InvalidCarrier()
                else:
                    print("Lựa chọn không hợp lệ.")
                    continue
                
                # Gọi hàm xử lý Duck Typing
                msg = dispatch_to_carrier(carrier, current_product, qty)
                print(f"\n{msg}")
                print(f"Số lượng tồn kho cập nhật: {current_product.stock_quantity:,.0f} đơn vị.")
                
            except AttributeError as e:
                print(f"\n[Lỗi Hệ Thống]: {e}")
            except ValueError as e:
                print(f"\n[Từ chối giao dịch]: {e}")

        elif choice == '7':
            print("Cảm ơn đã sử dụng hệ thống Amazon Inventory Simulator Pro!")
            break
        else:
            print("Chức năng không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()