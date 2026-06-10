"""
Biến global:
    + Được khai báo ngoài funcion 
    + Bên trong funcion có thể sử dụng biến global (khai báo: global name_global)
Biến local được khai báo bên trong funcion (gọi là tham số)
"""
status = False

def get_information_of_student_1(name, age, school):
    global status
    print(name)
    print(age)
    print(school)
    print(status)
    
    status = True
    
    # print(f"(1) --- {name} | {age} | {school}")
    return status
new_status = get_information_of_student_1("Bảo", 20, "PTIT")
print(new_status)