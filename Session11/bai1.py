# Thông tin sản phẩm ban đầu
product_info = ("SP001", "Áo polo nam", "Size L", 299000)

# Lấy mã sản phẩm
product_code = product_info[0]

# Lấy tên sản phẩm
product_name = product_info[1]

# Đếm số lượng thông tin sản phẩm
product_length = len(product_info)

# Cập nhật giá bán
temp = list(product_info)
temp[3] = 279000
product_info = tuple(temp)

print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", product_info)