class Order:
    def __init__(self,customer,order_id):
        self.customer=customer
        self.order_id=order_id
    def deliver(self):
        print(f"{self.customer} will get his order num {self.order_id} with standard delivery")

class ExpressOrder(Order):
    def __init__(self,customer,order_id):
        super().__init__(customer,order_id)
    def deliver(self):
        print(f"{self.customer} will get his order num {self.order_id} with express delivery in one day/same day")


obj1=Order('kiran','ki125')
# obj.deliver()
obj2=Order('harish','har153')

obj3=ExpressOrder('naresh','nar123')

print(obj1.__dict__)
print(obj2.__dict__)

print(ExpressOrder.__mro__) #method of resolution order-->to check flow of inhertinace happening b/w the classes.
