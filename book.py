#Book contient des order, qui contiennent  type de l'ordre, quantite, prix, id

class Book:
    
    def __init__(self, nom, order_list = []):
        self.nom = nom
        self.order_list = order_list
        
class Order:
    
    def __init__(self, nom, order_list = []):
        self.nom = nom
        self.order_list = order_list