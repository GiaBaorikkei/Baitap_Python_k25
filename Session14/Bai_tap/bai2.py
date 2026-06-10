# Biến toàn cục lưu tổng điểm hiện tại của khách hàng
total_points = 100

# Hàm cộng điểm thưởng
def add_reward_points(points_earned):
    global total_points
    # Cố gắng lấy tổng điểm cũ cộng thêm điểm mới
    total_points = total_points + points_earned
    print("Đã cộng thêm", points_earned, "điểm.")
    return total_points
# Khách mua hàng được thưởng 50 điểm
add_reward_points(50)

# In ra kết quả
print("Tổng điểm hiện tại của khách hàng:", total_points)