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

'''                                     #函数返回
def name(first,last):
    full_name = first + " " + last
    return full_name.title()            #使用return语句将值返回到调用函数的代码行
message = name('jimi', 'mike')
print(message)

def name(first,last,middle=''):         #使用默认值让实参变成可选的，默认值不加空格
    if middle:
        full_name = first + " " + middle + ' ' +last
    else:
        full_name = first + ' ' + last
    return full_name.title()
message = name('jimi', 'mike')          #缺省中间值
print(message)
message = name("marry","lara","michal") #不缺中间值
print(message)

def persons(first, last):               #返回字典
    person = {'first_name':first,'last_name':last}
    return person
message = persons('jim','kerry')
print(message)

while True:                             #搭配循环来循环调用函数，输入参数
    print("Enter 'q' to quit at any time")
    first = input("Please input first name:\n")
    if first == 'q':
        break
    last = input("Please input last name:\n")
    if last == 'q':
        break
    full_name = name(first,last)
    print("Hello " + full_name.title())
'''

'''                                     #传递列表
def greet(names):                       #把函数定义为名字列表，并将其存储在形参names中，向函数传递列表来提高处理列表的效率
    for name in names:
        print("Hello " + name.title() + "!")
users_names = ['mike','jim','kerry']
greet(users_names)

def design(undesigned, completed):      #在函数中修改列表
    while undesigned:
        current = undesigned.pop()
        print("Current designing: " + current)
        completed.append(current)
def show(completed):                    #在函数中对列表所做的任何修改都是永久的
    print("These are completed:")
    for current in completed:
        print(current)
undesigned = ['qwe','asd','zxc','rty','dfg']
completed = []
design(undesigned,completed)
show(completed)

undesigned = ['jim','cou','eric','mike']#禁止函数修改列表
completed = []
design(undesigned[:],completed)         #使用切片表示法[:]，创建列表的副本，此时传递传递进函数的是副本而不是原件
print(undesigned)                       #函数所作的任何修改也只影响副本，不影响原件
print(completed)
'''

'''                                     #传递任意数量实参
def names(*message):                    #形参*message创建一个名为message的空元组，并将接收到的所有值都封装到这个元组中
    print(message)
names('jack')
names('mike','jim','jerry')

def names(age = 0 ,*message):           #要接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后
    print(age)
    print(message)
names(16, 'jack')
names(18, 'mike', "jim")

def persons(first, last, **user_info):  #能够接受任意数量的键-值对。形参**user_info创建一个空字典用于存储任意键值对
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for key, vaule in user_info.items():
        profile[key] = vaule
    return profile
user_profile = persons('pence', 'merry', location = 'WuHan', field = 'CS')
print(user_profile)
'''

'''
import import_example                   #导入创建的模块（.py文件）， import关键字打开了import_example.py文件，并将其中所有的函数复制到了本程序中
import_example.persons(18, 'Mike', 'jim')#调用被导入模块中的函数，模块名.函数名
'''

'''
from import_example import persons      #导入模块中的指定函数
persons(18, 'Mike', 'jim')              #直接使用该函数
from import_example import persons, hello #也可以导入多个指定函数
hello()

from import_example import persons as name #使用as给函数指定别名
name(19, "nike")

import import_example as ie             #使用as给模块指定别名
ie.hello()

from import_example import *            #使用星号*运算符可导入模块中的所有函数
'''