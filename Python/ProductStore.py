class Product:
    count = 0
    def __init__(self, pname, price):
        self.pname = pname
        self.price = price
        Product.count += 1
    
    def get_info(self):
        print(f"Product = {self.pname}, Price = {self.price}")
    
    @classmethod
    def get_count(cls):
        print(f"Total products in store = {cls.count}")
        
    @staticmethod
    def calc_discount(price, discount):
        print(f"Discounted Price = {price - (price * discount / 100)}")
        

p1 = Product("Phone", 10000)
p2 = Product("Laptop", 90000)
p3 = Product("Watch", 1200)

p1.get_info()
p2.get_info()
p3.get_info()

Product.get_count()

p1.calc_discount(p2.price, 15)

