class Product:
    def __init__(self, product_id, name, price, quantity_sold, discount):
        self.id = product_id
        self.name = name
        self.price = price
        self.quantity_sold = quantity_sold
        self.discount = discount
        self.total_revenue = 0
        self.revenue_type = ""
        
        self.calculate_revenue()
        self.classify_revenue()
        
    def calculate_revenue(self):
        revenue = (self.price * self.quantity_sold) - self.discount
        self.total_revenue = revenue
    
    def classify_revenue(self):
        if self.total_revenue < 5000000:
            self.revenue_type = "Thấp"
        elif self.total_revenue < 20000000:
            self.revenue_type = "Trung Bình"
        elif self.total_revenue < 50000000:
            self.revenue_type = "Khá"
        else:
            self.revenue_type = "Cao"
            
    def update_info(self, price, quantity_sold, discount):
        self.price = price
        self.quantity_sold = quantity_sold
        self.discount = discount
        self.calculate_revenue()
        self.classify_revenue()