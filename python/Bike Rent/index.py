class bikeshop:
    print("NOTE :--- 100 Rs. per every hour for every bike Rent")
    def __init__(self,stock):
     self.stock=stock
    def displaybike(self):
        print("total bikes",self.stock)
    def rentforbike(self,q):
       
        if q<=0:
            print("enter the positive value or grater than zero")
        elif q>self.stock:
            print("enter the value (less than stock)")
        else:
            self.stock=self.stock-q
            print("total prices per hour ",q*100)
            print("total remender bikes ",self.stock)

while True:
    obj=bikeshop(100)
    uc=int(input('''
        1. display stock 
        2. Rent a bike 
        3. Exit                   
    '''))     
    if uc==1:
        obj.displaybike()
    elif uc==2:
        n=int(input("enter the Time for rent :---"))
        obj.rentforbike(n)
    else:
        break               

