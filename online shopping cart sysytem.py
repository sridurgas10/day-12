class Product:
    def __init__(self):
        self.items={}
   
     
    def addproduct(self,product_name,quantity,unit_price):
        if product_name in self.items:
            self.items[product_name]['quantity']=+quantity
            self.items[product_name]['totalprice']=quantity*unit_price
        else:
            self.items[product_name]={
                'quantity':quantity,
                'unit_price':unit_price ,
                'total_price':quantity*unit_price
            }
        return f"{product_name}  added/updated successfully.{self.items}"
     

    def remproduct(self,product_name,quantity) :   
        if product_name in self.items:
          if self.items[product_name]['quantity'] > quantity:
             self.items[product_name]['quantity']-=quantity
             self.items[product_name]['total_price'] = self.items[product_name]['quantity'] * self.items[product_name]['unit_price']
             return f"{quantity} {product_name} removed successfully{self.items}"

          elif self.items[product_name]['quantity']==quantity:
                del self.items[product_name]
                return f"{product_name} removed successfully {self.items}"
               
               
          else:
                 
                return f"{product_name} {'qunatity'} is not enough to delete"    
            
        else:
            return f" the product is not in {self.items}"    
          
product1=Product()
print("added successsfully",product1.addproduct("laptop",5,90000) )
print("added successsfully",product1.addproduct("moouse",5,10000) )
print(product1.remproduct("laptop",1))
print(product1.remproduct("laptop",5))
print(product1.remproduct("charger",1))



class Cart(Product):

    def __init__(self):
        super().__init__()
        

    def caltotal(self,discount_percentage):
        for product_name,details in self.items.items():
            total_price=details.get('total_price')
            print("tatoal_price",total_price)
      
            discount_value=total_price * (1 - discount_percentage / 100)
            print("discount_value",discount_value)
            total_amount=total_price  - discount_value
            
        return total_amount

cart1 = Cart()
cart1.addproduct("phone", 2, 30000)
print("after discount the price of the product is" ,cart1.caltotal(50))
cart1.addproduct("headphones", 1, 5000)
print("after discount the price of the product is" ,cart1.caltotal(20))


