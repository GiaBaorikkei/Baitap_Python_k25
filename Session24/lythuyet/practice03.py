# Static Method
"""
Chỉ sử dụng khi chỉ cần thực hiện hành vi mà không cần liên quan đến thuộc tính
"""

class MathOperator:
    # def __init__(self):
    #   pass
    
    @staticmethod
    def add_function(x,y):
        print(x + y)
        
phep_tinh = MathOperator()
