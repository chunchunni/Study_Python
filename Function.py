'''                                     #函数                                      
def greet_us():                         #使用关键字def定义一个函数，指出函数名，以冒号":"结尾
    print("Hello World!")
greet_us()

def greet_us(name):                     #传递参数给函数。name是形参，是函数完成工作所需的一项信息
    print("Hello " + name.title())
greet_us("Mike")                        #"Mike"是实参，是调用时传递的信息
'''

'''                                     #传递实参
def describe_pet(type, name):           #1、位置实参。根据实参的顺序将其关联到函数形参。
    print("I have a " + type)
    print("My " + type +"' name is " + name.title())
describe_pet('dog','jerry')             #实参的位置也很重要，不然顺序混乱则结果混乱

def describe_pet(type, name):           #2、关键字实参。传递给函数的名称-值对。
    print("I have a " + type)
    print("My " + type +"' name is " + name.title())
describe_pet(name= 'marry', type = 'cat') #实参的顺序无关紧要

def describe_pet(name, type = 'dog'):   #3、默认值。调用函数没有提供实参时，则使用形参的默认值。
    print("I have a " + type)
    print("My " + type +"' name is " + name.title())
describe_pet(name= 'tom', type = 'fish')
describe_pet("pop")                     #当默认值和未默认形参并存时，剩下的形参就被视为位置形参，
                                        #当只传入一个实参时会被指定给这一个位置实参
describe_pet(name='jack')               #可混合使用上述几种方式
'''