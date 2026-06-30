import sys
from manager import ProductManager
from utils import get_string_input

def show_menu():
    print("=== MENU ===")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật sản phẩm")
    print("4. Xóa sản phẩm")
    print("5. Tìm kiếm sản phẩm")
    print("6. Thoát")

def main():
    manager = ProductManager()
    
    while True:
        show_menu()
        choice = get_string_input("Nhập lựa chọn của bạn: ")
        
        if choice == '1':
            manager.show_all()
        elif choice == '2':
            manager.add_product()
        elif choice == '3':
            manager.update_product()
        elif choice == '4':
            manager.delete_product()
        elif choice == '5':
            manager.search_product()
        elif choice == '6':
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý sản phẩm!")
            sys.exit(0)
        else:
            print("Lựa chọn không hợp lệ! Vui lòng nhập từ 1 đến 6.")

if __name__ == "__main__":
    main()
                
            
            
        
        
        
        