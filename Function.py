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

def name(first,last,middle=''):         #使用默认值让实参变成可选的
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