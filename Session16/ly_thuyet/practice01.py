# .split() tách chuỗi thành mảng (mặc định là khoảng trắng)

my_information = "My nam is Bao, and i am a student in PTIT"
my_information_list = my_information.split(" ", 3)
print(my_information_list)

# <Phần tử nối>.join<mảng của mình>
my_array = ['My', 'nam', 'is', 'Bao,', 'and', 'i', 'am', 'a', 'student', 'in', 'PTIT']
my_string = "-".join(my_array)
print(my_string)

# replace(old, new, count)
"""
count có thể truyền vô số giá trị
"""
language_string = ("Hello Python", "Hello Java", "Hello C++")
print(language_string.replace("Hello", "Goodbye", 7))