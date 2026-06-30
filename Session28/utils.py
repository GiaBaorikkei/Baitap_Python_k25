def get_string_input(title, allow=False):
    while True:
        value = input(title).strip()
        if not allow and not value:
            print("Dữ liệu không được để trống vui lòng nhập lại.")
            continue
        return value

def get_number_input(title, num_type=float, max_val=None, min_val=None):
    while True:
        try:
            value_str = input(title).strip()
            if not value_str:
                print("Lỗi: Dữ liệu không được để trống!")
                continue
            
            value = num_type(value_str)
            
            if min_val is not None and value < min_val:
                print(f"Lỗi: Giá trị phải lớn hơn hoặc bằng {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Lỗi: Giá trị phải bé hơn hoặc bằng {max_val}")
                continue
                
            return value
            
        except ValueError:
            if num_type == int:
                type_name = "số nguyên"
            else:
                type_name = "số thực"
            print(f"Lỗi: Nhập không đúng định dạng {type_name}!")