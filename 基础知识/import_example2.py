from import_example import Cars         #从一个模块中导入另一个模块

class Battery():                        #新建电池类
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

class ElectricCars(Cars):               #继承自Cars的ElectrinCars类
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()        #将实例对象用作属性