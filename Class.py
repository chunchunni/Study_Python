'''
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

    def get_descriptve(self):           #描述车辆
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):            #打印里程
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometers(self, mile):
        self.odometer_reading = mile

my_car = Cars("audi", "A4", 2016)
print(my_car.get_descriptve())
my_car.read_odometer()                  #打印默认属性值

my_car.odometer_reading = 2020          #直接修改属性值
my_car.read_odometer()

my_car.update_odometers(2009)           #通过方法修改属性值
my_car.read_odometer()
