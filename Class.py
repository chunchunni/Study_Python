'''                                     #类
class Dog():
    """
    定义一个Dog类
    类中的函数称为方法。_init_()是一个特殊的方法，每当使用Dog类创建实例时，Python都会自动运行它
    self、name、age三个形参。其中self形参必不可少，且必须位于其他形参前。
    当调用_init_方法时，将自动传入实参self。每个与类关联的方法调用都自动传递实参self，
    self是一个指向实例（创建的对象）的引用，让实例能访问类中的属性和方法
    当需要创建实例时，只需要给最后两个形参name、age提供值
    """                                
    def __init__(self, name, age):      #并未设置return，但是会自动返回一个小狗实例
        self.name = name                #以self为前缀的变量可供类中所有的方法使用
        self.age = age
        
    def sit(self):
        print(self.name.title() + " is now sitting")
    
    def roll(self):
        print(self.name.title() + " is now rolling")

my_dog = Dog("Mike", 6)                 #根据类创建实例。默认调用_init_方法来创建一个小狗实例，并设置name和age的属性值
my_dog.sit()                            #调用方法
my_dog.roll()
print("My dog's name is " + my_dog.name.title())#使用“.”来访问与实例相关的属性name。
'''

class Cars():
    def __init__(self, make, model, year):#初始化方法
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0       #设置默认属性值

    def get_describe(self):             #描述车辆
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):            #打印里程
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometers(self, miles):  #修改属性的方法
        self.odometer_reading = miles

    def increment_odometer(self, miles):#递增属性值的方法
        self.odometer_reading += miles

    def fill_gas(self):                 #加油
        print("Gas Tank is fill.")

my_car = Cars("audi", "A4", 2016)
print(my_car.get_describe())
my_car.read_odometer()                  #打印默认属性值

my_car.odometer_reading = 2020          #直接修改属性值
my_car.read_odometer()

my_car.update_odometers(2009)           #通过方法修改属性值
my_car.read_odometer()

my_car.increment_odometer(100)          #通过方法增加属性值
my_car.read_odometer()

"""
继承：子类可以继承父类所有的属性和方法，同时可以定义自己的属性和方法

class ElectricCars(Cars):               #继承自Cars的ElectrinCars类
    def __init__(self, make, model, year):
    #初始化父类属性
        super().__init__(make, model, year)
    #super是一个特殊函数，用于将子类和父类关联起来。让Python调用Cars的方法__init__()，让ElectrinCars实例包含父类的所有属性
        self.battery_size = 70          #新建子类的属性
    
    def describe_battery(self):         #新建子类的方法
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def fill_gas(self):                 #重写继承自父类的方法
        print("This car has no gas_tank.")

my_ElCars = ElectricCars('tesla', "Model's", 2016)
print(my_ElCars.get_describe())         #子类中直接继承了所有父类的方法
my_ElCars.describe_battery()            #调用子类新创建的方法

my_car.fill_gas()                       #加油方法
my_ElCars.fill_gas()                    #重写加油方法
"""

class Battery():                        #新建电池类
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

class ElectricCars(Cars):               #继承自Cars的ElectrinCars类
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()        #将实例对象用作属性
    
my_ElCars = ElectricCars('tesla', "Model's", 2016)
print(my_ElCars.get_describe())
my_ElCars.battery.describe_battery()    #在实例my_ElCars中找到属性battery，再在该属性中找到battery实例可以调用的方法