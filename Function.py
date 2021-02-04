'''                                     #函数                                      
def greet_us():                         #使用关键字def定义一个函数，指出函数名，以冒号":"结尾
    print("Hello World!")
greet_us()

def greet_us(name):                     #传递参数给函数。name是形参，是函数完成工作所需的一项信息
    print("Hello " + name.title())
greet_us("Mike")                        #"Mike"是实参，是调用时传递的信息
'''

                                        #传递实参
def describe_pet(type, name):           #1、位置实参。根据实参的顺序将其关联到函数形参。
    print("I have a " + type)
    print("My " + type +"' name is " + name.title())
describe_pet('dog','jerry')             #实参的位置也很重要，不然顺序混乱则结果混乱