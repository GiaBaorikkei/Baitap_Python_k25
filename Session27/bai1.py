from abc import ABC, abstractmethod

# ==========================================
# 1. MIXIN CLASS
# ==========================================
class DigitalPremiumMixin:
    """
    Mixin Class: Lớp bổ trợ cung cấp tính năng độc lập, không phụ thuộc vào BaseAccount.
    Dùng để đa kế thừa, tăng cường tính năng mà không phá vỡ cấu trúc phân cấp chính.
    """
    def cashback_reward(self, amount):
        if amount > 5000000:
            return amount * 0.01
        return 0


# ==========================================
# 2. ABSTRACT BASE CLASS
# ==========================================
class BaseAccount(ABC):
    """
    Abstract Base Class: Bộ khung chuẩn cho mọi tài khoản.
    Bẫy 1: Kế thừa từ ABC ngăn chặn việc khởi tạo trực tiếp đối tượng từ lớp này (ném TypeError).
    """
    bank_name = "Vietcombank"

    def __init__(self, account_number, account_name):
        self.account_number = account_number
        # Tự động chuẩn hóa tên (In hoa, xóa khoảng trắng thừa)
        self.account_name = " ".join(account_name.strip().upper().split())
        self.__balance = 0  # Private attribute: Đóng gói nghiêm ngặt, chống can thiệp trực tiếp

    # @property: Biến một method thành một thuộc tính read-only. 
    # Giúp truy xuất self.balance an toàn mà không cần viết hàm get_balance().
    @property
    def balance(self):
        return self.__balance

    # Phương thức bảo vệ (Protected) để các Subclass có thể cập nhật số dư hợp lệ
    def _update_balance(self, amount):
        self.__balance += amount

    # @abstractmethod: Ép buộc tất cả các lớp con (Subclass) phải ghi đè và triển khai logic cho hàm này.
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    # Operator Overloading: Nạp chồng toán tử cộng (+)
    def __add__(self, other):
        # Bẫy 3: Kiểm tra kiểu dữ liệu khi Overloading
        if not isinstance(other, BaseAccount):
            return NotImplemented
        return self.balance + other.balance

    # Operator Overloading: Nạp chồng toán tử so sánh nhỏ hơn (<)
    def __lt__(self, other):
        if not isinstance(other, BaseAccount):
            return NotImplemented
        return self.balance < other.balance

    # @staticmethod: Hàm tĩnh không phụ thuộc vào instance (self) hay class (cls).
    # Dùng cho các tác vụ tiện ích chung, gọi thông qua TênLớp.tên_hàm().
    @staticmethod
    def validate_account_number(account_number):
        return len(account_number) == 10 and account_number.isdigit()

    # @classmethod: Hàm thao tác trực tiếp với Class (cls) thay vì Instance (self).
    # Có thể thay đổi thuộc tính cấp độ Class (bank_name) và áp dụng cho toàn bộ hệ thống.
    @classmethod
    def update_bank_name(cls, new_name):
        cls.bank_name = new_name


# ==========================================
# 3. SUBCLASSES
# ==========================================
class SavingsAccount(BaseAccount):
    def __init__(self, account_number, account_name, interest_rate):
        super().__init__(account_number, account_name)  # Gọi constructor của lớp cha
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self._update_balance(amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Số tiền rút phải lớn hơn 0.")
        
        penalty = amount * 0.02
        total_deduction = amount + penalty
        
        if self.balance >= total_deduction:
            self._update_balance(-total_deduction)
            return amount, penalty
        else:
            raise ValueError("Số dư không đủ để rút và trả phí phạt.")

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        if interest > 0:
            self._update_balance(interest)
        return interest


class CreditAccount(BaseAccount):
    def __init__(self, account_number, account_name, credit_limit):
        super().__init__(account_number, account_name)
        self.credit_limit = credit_limit

    def deposit(self, amount):
        if amount > 0:
            self._update_balance(amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Số tiền rút phải lớn hơn 0.")
        
        # Bẫy 2: Kiểm tra vượt quá hạn mức tín dụng âm
        if self.balance - amount < -self.credit_limit:
            raise ValueError("Vượt quá hạn mức thấu chi cho phép.")
        
        self._update_balance(-amount)
        return amount


class HybridAccount(SavingsAccount, DigitalPremiumMixin):
    """
    Multiple Inheritance: Đa kế thừa.
    MRO (Method Resolution Order): HybridAccount -> SavingsAccount -> BaseAccount -> ABC -> DigitalPremiumMixin -> object
    """
    def deposit(self, amount):
        if amount <= 0:
            return
        
        # Gọi hàm deposit của lớp cha (SavingsAccount)
        super().deposit(amount)
        
        # Kích hoạt tính năng hoàn tiền từ Mixin
        cashback = self.cashback_reward(amount)
        if cashback > 0:
            self._update_balance(cashback)
            return cashback
        return 0


# ==========================================
# 4. PAYMENT GATEWAYS (DUCK TYPING)
# ==========================================
class VNPayGateway:
    def execute_pay(self, account, amount):
        account.withdraw(amount)
        return f"[Hệ thống VNPay]: Đang kết nối tới tài khoản {account.account_number}...\nXác thực thanh toán bằng Duck Typing thành công!"

class ViettelMoneyGateway:
    def execute_pay(self, account, amount):
        account.withdraw(amount)
        return f"[Hệ thống Viettel Money]: Xử lý giao dịch cho {account.account_number}...\nXác thực thanh toán bằng Duck Typing thành công!"

class InvalidGateway:
    # Lớp giả lập lỗi Duck Typing (Không có hàm execute_pay)
    def process(self):
        pass

def process_payment(payment_gateway, account, amount):
    """
    Cơ chế Duck Typing: Không quan tâm đối tượng thuộc Class nào, 
    chỉ cần đối tượng đó có phương thức `execute_pay(account, amount)` là có thể thực thi.
    """
    try:
        # Bẫy 4: Sai lệch phương thức trong Duck Typing
        return payment_gateway.execute_pay(account, amount)
    except AttributeError:
        raise AttributeError("Cổng thanh toán không hợp lệ hoặc chưa được tích hợp.")


# ==========================================
# 5. CLI MENU SYSTEM (NGHIỆP VỤ)
# ==========================================
def main():
    accounts = []
    current_account = None

    while True:
        print("\n===== VIETCOMBANK DIGIBANK PRO SIMULATOR =====")
        print("1. Mở tài khoản mới")
        print("2. Xem thông tin & Kiểm tra thứ tự kế thừa (MRO)")
        print("3. Giao dịch Nạp / Rút tiền & Tính điểm thưởng")
        print("4. Tích lũy / Áp dụng lãi suất định kỳ")
        print("5. Kiểm tra tính năng gộp tài khoản & So sánh")
        print("6. Thanh toán hóa đơn qua Cổng trung gian")
        print("7. Thoát chương trình")
        print("==============================================")
        
        choice = input("Chọn chức năng (1-7): ")

        if choice == '1':
            print("\n--- CHỌN LOẠI TÀI KHOẢN ---")
            print("1. Savings Account (Tài khoản Tiết kiệm)")
            print("2. Credit Account (Tài khoản Tín dụng)")
            print("3. Hybrid Account (Tài khoản Đa năng)")
            type_choice = input("Chọn loại tài khoản (1-3): ")
            
            acc_number = input("Nhập số tài khoản 10 chữ số: ")
            if not BaseAccount.validate_account_number(acc_number):
                print("Số tài khoản không hợp lệ! Phải gồm đúng 10 chữ số.")
                continue
                
            acc_name = input("Nhập tên chủ tài khoản: ")
            
            try:
                if type_choice == '1':
                    rate = float(input("Nhập lãi suất năm (ví dụ 0.05): "))
                    new_acc = SavingsAccount(acc_number, acc_name, rate)
                    print(f"\nMở tài khoản Tiết kiệm thành công!\nChủ tài khoản: {new_acc.account_name}")
                elif type_choice == '2':
                    limit = float(input("Nhập hạn mức tín dụng: "))
                    new_acc = CreditAccount(acc_number, acc_name, limit)
                    print(f"\nMở tài khoản Tín dụng thành công!\nChủ tài khoản: {new_acc.account_name}")
                elif type_choice == '3':
                    rate = float(input("Nhập lãi suất năm (ví dụ 0.05): "))
                    new_acc = HybridAccount(acc_number, acc_name, rate)
                    print(f"\nMở tài khoản Đa năng thành công!\nChủ tài khoản: {new_acc.account_name}")
                else:
                    print("Loại tài khoản không hợp lệ.")
                    continue
                
                accounts.append(new_acc)
                current_account = new_acc
            except ValueError:
                print("Dữ liệu nhập vào không hợp lệ (cần là số).")

        elif choice == '2':
            if not current_account:
                print("Hệ thống chưa có thông tin tài khoản. Vui lòng mở tài khoản ở Chức năng 1 trước.")
                continue
            
            print("\n--- THÔNG TIN TÀI KHOẢN HIỆN TẠI ---")
            print(f"Loại tài khoản: {current_account.__class__.__name__}")
            print(f"Ngân hàng: {current_account.bank_name}")
            print(f"Số tài khoản: {current_account.account_number}")
            print(f"Chủ tài khoản: {current_account.account_name}")
            print(f"Số dư: {current_account.balance:,.0f} VND")
            
            if hasattr(current_account, 'interest_rate'):
                print(f"Lãi suất: {current_account.interest_rate * 100}% / năm")
            if hasattr(current_account, 'credit_limit'):
                print(f"Hạn mức tín dụng: {current_account.credit_limit:,.0f} VND")
                
            print("\n[Cấu trúc MRO]:", [cls.__name__ for cls in current_account.__class__.mro()])

        elif choice == '3':
            if not current_account:
                print("Vui lòng mở tài khoản trước.")
                continue
                
            print("\n--- GIAO DỊCH NẠP / RÚT TIỀN ---")
            print("1. Nạp tiền")
            print("2. Rút tiền")
            action = input("Chọn giao dịch (1-2): ")
            
            try:
                amount = float(input("Nhập số tiền: "))
                if action == '1':
                    # Đa hình: Hành vi deposit tự thay đổi tùy loại tài khoản
                    result = current_account.deposit(amount)
                    print("\nNạp tiền thành công!")
                    if isinstance(current_account, HybridAccount) and result and result > 0:
                        print(f"[Ưu đãi Premium]: Bạn được hoàn tiền 1% ({result:,.0f} VND) vào tài khoản!")
                    print(f"Số dư mới: {current_account.balance:,.0f} VND")
                    
                elif action == '2':
                    # Đa hình: Hành vi withdraw xử lý logic khác nhau
                    if isinstance(current_account, SavingsAccount) and not isinstance(current_account, HybridAccount):
                        drawn, penalty = current_account.withdraw(amount)
                        print("\nRút tiền thành công!")
                        print(f"Số tiền rút: {drawn:,.0f} VND")
                        print(f"Phí phạt rút trước hạn (2%): {penalty:,.0f} VND")
                    elif isinstance(current_account, CreditAccount):
                        drawn = current_account.withdraw(amount)
                        print("\nRút tiền thành công! (Sử dụng hạn mức thấu chi)")
                        print(f"Số tiền rút: {drawn:,.0f} VND")
                    else:
                        drawn, penalty = current_account.withdraw(amount)
                        print("\nRút tiền thành công!")
                        
                    print(f"Số dư hiện tại: {current_account.balance:,.0f} VND")
            except ValueError as e:
                print(f"Lỗi giao dịch: {e}")

        elif choice == '4':
            if not current_account:
                print("Vui lòng mở tài khoản trước.")
                continue
            
            if hasattr(current_account, 'apply_interest'):
                print("\n--- TÍNH LÃI ĐỊNH KỲ ---")
                print(f"Số dư trước tính lãi: {current_account.balance:,.0f} VND")
                interest = current_account.apply_interest()
                print(f"Lãi suất năm: {current_account.interest_rate * 100}%")
                print(f"Tiền lãi nhận được: +{interest:,.0f} VND")
                print(f"Số dư mới sau khi cộng lãi: {current_account.balance:,.0f} VND")
            else:
                print("Tài khoản này không hỗ trợ tính năng sinh lãi định kỳ.")

        elif choice == '5':
            if not current_account or len(accounts) < 2:
                print("Hệ thống cần ít nhất 2 tài khoản để thực hiện chức năng này.")
                continue
                
            print("\n--- ĐỒNG BỘ & SO SÁNH TÀI KHOẢN (OPERATOR OVERLOADING) ---")
            print(f"Tài khoản hiện tại (A): {current_account.account_name} (Số dư: {current_account.balance:,.0f} VND)")
            
            print("Danh sách tài khoản đối ứng (B):")
            for idx, acc in enumerate(accounts):
                if acc != current_account:
                    print(f"{idx}. {acc.account_number} ({acc.account_name} - Số dư: {acc.balance:,.0f} VND)")
                    
            try:
                target_idx = int(input("Chọn số thứ tự tài khoản đối ứng: "))
                target_acc = accounts[target_idx]
                
                # Gọi __lt__
                compare_str = "NHỎ HƠN" if current_account < target_acc else "LỚN HƠN HOẶC BẰNG"
                print(f"\n[Kết quả So sánh (__lt__)]: Số dư tài khoản A {compare_str} số dư tài khoản B.")
                
                # Gọi __add__
                total_balance = current_account + target_acc
                print(f"[Kết quả Tổng hợp (__add__)]: Tổng số tiền sở hữu của cả 2 tài khoản là: {total_balance:,.0f} VND.")
            except (ValueError, IndexError):
                print("Lựa chọn không hợp lệ.")

        elif choice == '6':
            if not current_account:
                print("Vui lòng mở tài khoản trước.")
                continue
                
            print("\n--- THANH TOÁN HÓA ĐƠN QUA CỔNG TRUNG GIAN ---")
            print("1. Thanh toán qua VNPay")
            print("2. Thanh toán qua Viettel Money")
            print("3. Test Bẫy Duck Typing (Cổng lỗi)")
            gw_choice = input("Chọn cổng thanh toán (1-3): ")
            
            try:
                amount = float(input("Nhập số tiền hóa đơn: "))
                
                if gw_choice == '1':
                    gateway = VNPayGateway()
                elif gw_choice == '2':
                    gateway = ViettelMoneyGateway()
                elif gw_choice == '3':
                    gateway = InvalidGateway()
                else:
                    print("Lựa chọn không hợp lệ.")
                    continue
                
                # Xử lý thanh toán độc lập bằng Duck Typing
                msg = process_payment(gateway, current_account, amount)
                print(f"\n{msg}")
                print(f"Tài khoản đã thanh toán hóa đơn giá trị: {amount:,.0f} VND.")
                print(f"Số dư mới: {current_account.balance:,.0f} VND.")
                
            except AttributeError as e:
                print(f"\n[Lỗi Hệ Thống]: {e}")
            except ValueError as e:
                print(f"\n[Từ chối giao dịch]: {e}")

        elif choice == '7':
            print("Cảm ơn đã trải nghiệm hệ thống Vietcombank Digibank Pro Simulator!")
            break
        else:
            print("Chức năng không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()