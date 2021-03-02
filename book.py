#Book contient des order, qui contiennent  type de l'ordre, quantite, prix, id

class Book:
    
    def __init__(self, name, order_list = []):
        self.name = name
        self.order_list = order_list
        
    def insert_buy(quantity, price):
        return 0
        
    def insert_sell(quantity, price):
        return 0
        
class Order:
    
    def __init__(self, order_type, quantity, price, idd):
        self.order_type = order_type
        self.quantity = quantity
        self.price = price
        self.idd = 0
        
    