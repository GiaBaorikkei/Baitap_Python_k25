list_staff = []
count_id = 100

while True:
    print("=== QUẢN LÍ NHÂN SỰ ===")
    print("1. Thêm nhân viên mới.")
    print("2. Danh sách nhân viên.")
    print("3. Xoá nhân viên khỏi hệ thống.")
    print("4. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn: ")
    
    if choice == "1":
        while True:
            name = input("Nhập tên nhân viên: ").strip().title()
            if name != "":
                break
            print("Tên không được để trống.")
        while True:
            salary = float(input("Nhập lương nhân viên: "))
            if salary != "" or salary > 0:
                break
            print("Lương nhân viên không hợp lệ.")
        count_id += 1
            
        list_staff.append({
            "id": count_id,
            "name": name,
            "salary": salary
        })
        print(f"Đã thêm nhân viên {count_id} thành công!")
    elif choice == "2":
        if len(list_staff) == 0:
            print("Danh sách nhân viên đang trống")
        else:
            print(f"{'ID':<5} | {'TÊN NHÂN VIÊN':<20} | {'MỨC LƯƠNG'}")
            for i in list_staff:
                print(f"{i['id']:<5} | {i['name']:<20} | {i['salary']}")
    elif choice == "3":
        del_id = int(input("Nhập ID nhân viên cần xoá: "))
        is_exit = False
        for i in list_staff:
            if del_id == i["id"]:
                list_staff.remove(i)
                print("Xoá thành công!")
                is_exit = True
                break
            if is_exit == False:
                print("Không tìm thấy nhân viên cần xoá!")
                break
    elif choice == "4":
        print("Đã thoát chương trình!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
                
                
        
        