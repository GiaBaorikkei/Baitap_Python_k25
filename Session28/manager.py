from product import Product
from utils import get_number_input, get_string_input

class ProductManager:
    def __init__(self):
        self.products = []
    
    def find_product_by_id(self, product_id):
        for i in self.products:
            if i.id == product_id:
                return i
        return None
        
    def add_product(self):
        print("Thêm sản phẩm mới.")
        while True:
            product_id = get_string_input("Nhập mã sản phẩm: ")
            if self.find_product_by_id(product_id):
                print("Mã sản phẩm đã tồn tại.")
            else:
                break
        name = get_string_input("Nhập tên sản phẩm: ")
        price = get_number_input("Nhập giá sản phẩm: ", min_val=0)
        quantity = get_number_input("Nhập số lượng đã bán: ", int, max_val=10000, min_val=0)
        discount = get_number_input("Nhập giảm giá: ", min_val=0)
        
        new_product = Product(product_id, name, price, quantity, discount)
        self.products.append(new_product)
        print("Đã thêm sản phẩm thành công.")

    def show_all(self):
        print("--- DANH SÁCH SẢN PHẨM ---")
        if not self.products:
            print("Danh sách sản phẩm đang rỗng")
            return
        print(f"{'Mã SP':<10} | {'Tên SP':<10} | {'Giá bán':<10} | {'SL đã bán':<10} | {'Giảm giá':<10} | {'Tổng DT':<10} | {'Loại DT'}")
        for i in self.products:
            print(f"{i.id:<10} | {i.name:<10} | {i.price:<10} | {i.quantity_sold:<10} | {i.discount:<10} | {i.total_revenue} | {i.revenue_type}")
            
    def update_product(self):
        print("--- Cập nhật sản phẩm ---")
        product_id = get_string_input("Nhập mã sản phẩm cần cập nhật: ")
        product = self.find_product_by_id(product_id)
        if not product:
            print("Không tìm thấy sản phẩm cần cập nhật.")
            return
        price = get_number_input("Nhập giá bán mới: ", min_val=0)
        quantity = get_number_input("Nhập số lượng bán mới: ", int, max_val=10000, min_val=0)
        discount = get_number_input("Nhập giảm giá mới: ", min_val=0)
        
        product.update_info(price, quantity, discount)
        print("Cập nhật sản phẩm thành công.")
        
    def delete_product(self):
        print("--- Xoá sản phẩm ---")
        product_id = get_string_input("Nhập mã sản phẩm cần xoá: ")
        product = self.find_product_by_id(product_id)
        if not product:
            print("Không tìm thấy sản phẩm cần xoá.")
            return
        confirm = get_string_input(f"Bạn có chắc chắn muốn xoá sản phẩm {product.name} không? )y/n: ")
        if confirm.lower() == "y":
            self.products.remove(product)
            print("Xoá sản phẩm thành công.")
        elif confirm.lower() == "n":
            print("Đã huỷ thao tác xoá.")
        else:
            print("Lựa chọn không hợp lệ.")

    def search_product(self):
        print("\n--- TÌM KIẾM SẢN PHẨM ---")
        keyword = get_string_input("Nhập tên sản phẩm cần tìm kiếm: ").lower()
        
        results = []
        
        for i in self.products:
            if keyword in i.name.lower():
                results.append(i)
                
        if len(results) == 0:
            print("Không tìm thấy sản phẩm phù hợp!")
            return 
            
        print(f"{'Mã SP':<10} | {'Tên sản phẩm':<25} | {'Giá bán':<15} | {'SL bán':<10} | {'Giảm giá':<15} | {'Tổng DT':<15} | {'Loại DT':<10}")
        print("-" * 115)
        
        for i in results:
            print(f"{i.id:<10} | {i.name:<25} | {i.price:<15,.0f} | {i.quantity_sold:<10} | {i.discount:<15,.0f} | {i.total_revenue:<15,.0f} | {i.revenue_type:<10}")
        print("-" * 115)
        