

import pandas as pd

class Book:
    
    def __init__(self, name, count = 1, order_list = [], buy=None, sell=None):
        self.name = name
        self.count = count
        self.order_list = order_list
        self.sell= sell
        self.buy= buy
        
    def __str__(self):
        s = "\nBook on %s \n\n"%(self.name)
        if self.sell.empty:
            s+=str(self.buy) + "\n"
        elif self.buy.empty :
            s+=str(self.sell) + "\n"
        else :
            s+=str(self.sell)+ "\n" + "------------------------\n"
            s+=str(self.buy) + "\n"
        
        # for o in self.order_list:
        #     s += "         %s %s @ %s id = %s \n"%(o.order_type, o.quantity, o.price, o.idd)
        # s +="------------------------\n"
        return s
    
    
    
    def insert_buy(self, quantity, price):
        
        o = Order("BUY",quantity,price,self.count)
        
        print("--- Insert BUY %s @ %s id = %s on %s"%(quantity,price,self.count,self.name))
        
        self.count += 1
        toRemove=[]
        
        if self.order_list == [] :
            self.order_list.append(o)
            
            
        else :
            for i in range(len(self.order_list)-1,-1,-1) :
                if self.order_list[i].order_type == "SELL":
                    if o.price >= self.order_list[i].price :
                        if o.quantity > self.order_list[i].quantity :
                            o.quantity -= self.order_list[i].quantity
                            toRemove.append(i)
                            print("Execute %s at %s on %s"%(self.order_list[i].quantity, self.order_list[i].price, self.name))
                        elif o.quantity == self.order_list[i].quantity :
                            toRemove.append(i)
                            print("Execute %s at %s on %s"%(o.quantity, self.order_list[i].price, self.name))
                            break
                        else :
                            self.order_list[i].quantity -= o.quantity
                            
                            print("Execute %s at %s on %s"%(o.quantity, self.order_list[i].price, self.name))
                            break   
                    else :
                        self.order_list.append(o)
                         
                        break
            
            for i in toRemove:
                self.order_list.pop(i)
                
            #tri
            self.order_list = sorted(self.order_list, key=lambda order: order.price, reverse=True)
        
        self.sell= pd.DataFrame(data=[], columns=['Type', 'Quantity', 'Price', 'ID'])
        self.buy= pd.DataFrame(data=[], columns=['Type', 'Quantity', 'Price', 'ID'])
        
        cb, cs = 0, 0
        for x in self.order_list :
            if x.order_type == "BUY":
                self.buy.loc[cb] = [x.order_type, x.quantity, x.price, x.idd]
                cb += 1
            else :
                self.sell.loc[cs] = [x.order_type, x.quantity, x.price, x.idd]
                cs += 1
        
        self.buy = self.buy.set_index('Type')
        self.sell = self.sell.set_index('Type')
        #print
        print(self)
        
    def insert_sell(self, quantity, price):
        
        o = Order("SELL",quantity,price,self.count)
        
        print("--- Insert SELL %s @ %s id = %s on %s"%(quantity,price,self.count,self.name))
        
        self.count += 1
        toRemove=[]
        
        if self.order_list == [] :
            self.order_list.append(o)
        
        else :
            for i in range(len(self.order_list)) :
                if self.order_list[i].order_type == "BUY":
                    if o.price <= self.order_list[i].price :
                        if o.quantity > self.order_list[i].quantity :
                            o.quantity -= self.order_list[i].quantity
                            toRemove.append(i)
                            print("Execute %s at %s on %s"%(self.order_list[i].quantity, self.order_list[i].price, self.name))
                        elif o.quantity == self.order_list[i].quantity :
                            toRemove.append(i)
                            print("Execute %s at %s on %s"%(o.quantity, self.order_list[i].price, self.name))
                            break
                        else :
                            self.order_list[i].quantity -= o.quantity
                            print("Execute %s at %s on %s"%(o.quantity, self.order_list[i].price, self.name))
                            break
                        
                    else :
                        self.order_list.append(o) 
                        break
              
            for i in toRemove:
                self.order_list.pop(i)
            
            #tri
            self.order_list = sorted(self.order_list, key=lambda order: order.price, reverse=True)
        
        self.sell= pd.DataFrame(data=[], columns=['Type', 'Quantity', 'Price', 'ID'])
        self.buy= pd.DataFrame(data=[], columns=['Type', 'Quantity', 'Price', 'ID'])
        
        cb, cs = 0, 0
        for x in self.order_list :
            if x.order_type == "BUY":
                self.buy.loc[cb] = [x.order_type, x.quantity, x.price, x.idd]
                cb += 1
            else :
                self.sell.loc[cs] = [x.order_type, x.quantity, x.price, x.idd]
                cs += 1
        
        self.buy = self.buy.set_index('Type')
        self.sell = self.sell.set_index('Type')
        #print
        print(self)

        
class Order:
    
    def __init__(self, order_type, quantity, price, idd):
        self.order_type = order_type
        self.quantity = quantity
        self.price = price
        self.idd = idd
        


    