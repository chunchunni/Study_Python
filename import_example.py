def persons(age, *messages):            #创建一个persons模块
    print("Age: " + str(age))
    for message in messages:
        print(message)

def hello():
    print("Hello!")

class Cars():                           #一个模块中可以存储多个类
    def __init__(self, make, model, year):#初始化默认属性值
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_describe(self):             #描述车辆
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):            #打印里程
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometers(self, miles):  #修改属性的方法
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):#递增属性值的方法
        self.odometer_reading += miles

    def fill_gas(self):                 #加油
        print("Gas Tank is fill.")

class Battery():                        #新建电池类
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

class ElectricCars(Cars):               #继承自Cars的ElectrinCars类
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()        #将实例对象用作属性