'''                                     #一组 三个单引号  可以将多行注释
n = 0
value = 1
message = 'I say "HEllo World"'         #字符串的单引号与双引号用法一致，引号内全部是字符串内容
while n < 1:
    a = float(input("Inpute a number"))
    value = a*10
    print(value)
    n += 1
print("value = {}, n = {}".format(value, n))
print("value = {:.2f}".format(value))   #格式化输出
print(message)
print(message.title())                  #首字母大写，其余字母小写
print(message.upper())                  #所有字母大写
print(message.lower())                  #所有字母小写

space = "  s p a c e  "
print(space.rstrip())                   #删除字符串右端空白
print(space.lstrip())                   #删除字符串左端空白
print(space.strip())                    #删除字符串两端空白

a=2+3
b=2-3
c=2*3
d=2/3
e=2**3
print(a,b,c,d,e)                        #加减乘除和乘方
a=0.2+0.1                               #python中也会有精度问题
b=3*0.1
print(a,b)
'''

'''                                     #字符串操作
first_name = 'Ni'
last_name = 'Chun Chun'
name = first_name + " " + last_name     #使用加号来连接字符串
print(name)
print("Hello, " + name.title() + '!')   #使用加号来连接字符串输出
age = 23
#message = name + "year" + age           #age与name的类型不一致，在进行字符串的连接操作时需要转换类型
message = name + " year" + str(age)     #str函数将传入参数强制转换成字符串型
print(message)
print(first_name+"\t"+last_name+"\n"+message)   #制表符\t与换行符\n
'''

'''                                     #列表操作
string = ['q','w','e','r']
print(string)                           #输出包括方括号在内的所有信息
print(string[0])                        #按序访问
print(string[-1])                       #当列表不为空时，可以使用[-1]的参数来访问列表尾端元素

string[0] = 'a'
print(string[0])                        #修改列表元素
string.append('t')                      #扩展列表，在尾端添加新元素
print(string)

string.insert(0,'y')                    #插入列表，在任意指定位置插入想放入的元素
print(string)

del string[0]                           #删除列表，使用del语句删除指定位置的元素
print(string)

pop_string = string.pop(2)              #出栈列表元素，使用pop函数删除并赋值指定位置的元素，若不添加位置参数则默认出栈末尾元素
print(string)
print(pop_string)

string.remove('a')                      #删除列表中指定的值
print(string)

string = ['q','w','e','r','t','y','u','i','o','p']
print(sorted(string))                   #sorted函数，临时的将列表中的元素按字母序排序，并不改变原列表中元素的顺序
print(string)

string.reverse()                        #reverse函数，永久性的将列表反转，也就是元素头尾顺序转换
print(string)
string.reverse()

string.sort()                           #sort函数，永久性的将列表元素按字母序排序，并无法恢复原来的元素序列
print(string)

a=len(string)                           #len函数，确定列表的长度。计算长度时，计数从1开始
print(a)

strings = ['q','w','e','r','t']
for string in strings:                  #将string中的元素，挨个赋值给value然后输出。冒号“：”一定不可遗漏
    print(string)
    print("循环中可以有任意行代码")
print("循环结束")                       #使用缩进来判断代码行之间的关系,不能使用不必要的缩进，也不能不使用缩进

for value in range(1,5):                #使用range函数，生成一系列数字
    print(value)

for value in range(1,10,5):             #使用range函数，从1开始计数，步长为5，上限为10
    print(value)

numbers = list(range(1,5))              #使用list函数，将range函数生成的数字转换为一个列表
print(numbers)
numbers = []
for value in range(1,11):               #输出前十个数的平方
    numbers.append(value**2)
    print(numbers[value-1])

squares = [value**2 for value in range(1,11)]                                        
print(squares)                          #列表解析方式创建列表，所使用的效果等同于前述循环的效果

print(min(numbers))                     #专门用于处理数字列表的函数：最小、最大、求和
print(max(numbers))
print(sum(numbers))

print(numbers[1:3])                     #切片，可以访问指定位置范围内的元素
print(numbers[:3])                      #未指定起始索引，默认从开头开始提取，:3即返回前三个元素
print(numbers[4:])                      #未指定结束索引，默认终止于末尾
print(numbers[-3:])                     #负数索引返回离列表末尾相应距离的元素，-3即返回最后三个元素

copy_numbers = numbers[:]               #复制列表，同时省略开始和结束索引可以将一个列表复制给另一个新列表
print(copy_numbers)
copy_numbers.append('x')                #对复制列表的操作，不影响原列表
print(copy_numbers)
print(numbers)

double_numbers = numbers                #将变量double_numbers关联到包含在numbers中的列表，这两个变量都指向同一个列表
print(double_numbers)
double_numbers.append('Y')
print(double_numbers)
print(numbers)                          #对double_numbers末端添加的新元素，改变了原列表
'''

'''                                     #元组操作
numbers = (20,50)                       #定义拥有两个元素的元组
print(numbers[0])
#numbers[0] = 30                        #报错，因为元组中的元素值不可以修改
print(numbers)
numbers = (30,50)                       #元组的元素值不可以修改，但是可以给元组变量重新赋值
print(numbers)
'''

'''                                     #条件判断语句
a = 4
if a == 3:                              #if条件语句的使用,判断是否相等时，区分大小写
    print("a = ",a)
else:
    print("不相等")
if a != 3:
    print("a不等于3")
if a < 5 and a > 3:                     #and检测多个条件
    print("And测试,正确")
if a > 1 or a > 10:                     #or检测多个条件
    print("Or测试，正确")

age = 16
if age < 14:                            #if-elif-else结构
    print("免票")
elif age < 18:
    print("半票")
elif age > 60:
    print("老年人优惠")
else:
    print("全票")

numbers = [1,2,3,4]
if a in numbers:                        #in 判断值是否在列表中
    print("a在numbers中")
b = 5
if b not in numbers:                    #not in 判断值是否不包括在列表中
    print("b不在numbers中")

flag1 = True                            #布尔表达式，用于设置标志
flag2 = False
if flag1:
    print("True")
if ~flag2:                              #~ 取反
    print("False")
'''

'''                                     #字典
lara = {'age':15,'sex':'man'}           #字典是一系列的键-值对，通过使用键来访问对应的值，                                       
print(lara)                             #值可以是任意数据类型、列表、字典
print(lara['sex'])
lara['high'] = 170                      #添加键值对
lara['major'] = 'CS'
print(lara)
lara['age'] = 16                        #修改键值对
print(lara)
del lara["major"]                       #使用del删除指定字典名和要删除的键
print(lara)

languages = {                           #由类似对象组成的字典
    'mike':'c',
    'jack':'java',
    'marry':'python',
    'edward':'ruby',
    'phil':'python',
    }
print("Marry's favorite language is " + #较长语句的分行输出
    languages['marry'].title()+
    ".")
                                        #遍历                                        
for name, language in languages.items():#遍历字典中所有键值对
    print("Name:" + name)               #方法item返回一个键值对列表，需要依次将键-值对存储到两个变量中
    print("Language:" + language + "\n")#遍历字典时，键值对的返回顺序与存储顺序可能不同

for name in languages.keys():           #遍历字典中所有的键
    print(name.title())                 #方法keys仅提取所有的键，返回一个列表包含字典中所有的键
for name in languages:                  #遍历字典时，默认遍历所有的键
    print(name.title()) 
print("\n")
for name in sorted(languages.keys()):   #按序遍历字典中所有的键
    print(name.title())

for language in languages.values():     #遍历字典中所有的键,不考虑重复
    print(language.title())
print("\n")
for language in set(languages.values()):#set方法，找出列表中不重复的元素并创建一个集合
    print(language.title())

                                        #嵌套
lara = {'age':15,'sex':'man'}
mike = {'age':16,'sex':'woman'}
jack = {'age':17,'sex':'man'}
persons = [lara, mike, jack]            #字典列表
for person in persons:
    print(person)

pizza = {                               #在字典中存储列表
    'crust':['thick'],
    'toppings':['mushrooms','cheese'],
}
for topping in pizza['toppings']:
    print(topping)
for key, values in pizza.items():       #使用变量来存储列表，再使用循环输出列表
    print("Value:"+ key)
    for value in values:
        print(value)

persons = {                             #在字典中存储字典
    'lara':{
        'age':15,
        'sex':'man',
        },

    'mike':{
        'age':16,
        'sex':'woman',
        },
    }
for name, info in persons.items():      #使用变量来存储字典，再访问对应的键来对应的值打印输出
    print("Name: " + name.title())
    print("Age: " + str(info['age']) +"\tSex: " + info['sex'].title())
'''

'''                                     #输入与循环
message = input('input something and i will return to you:\n')
                                        #input函数可以暂停程序，等待用户进行输入，并将输入存储到一个变量中
                                        #input()接受一个参数，即向用户显示的提示或者说明
print(message)
introduce = 'can you tell us your name?'#创建多行字符串
introduce += '\nwhat\'s your first name?'
name = input(introduce)
print("Hello," + name +'!')

number = input('input a number\n')
number = int(number)                    #input函数的输出值为字符串类型，可以使用int()函数将其转换为整数型
print(number)
number = number % 3                     #求模运算符
print(number)

count = 0
while count <=5:                        #使用while循环
    print(count)
    count += 1

introduce = "Input 'quit' to quit the program"
introduce += "\nPlease input something:\n"
message = ""
while message != "quit":                #由用户选择退出时机
    message = input(introduce)
    print(message)

flag = True
while flag:                             #使用标志来选择退出时机
    message = input(introduce)
    if message == "quit":
        flag = False
    else:
        print(message)

while True:                             #使用break来立即退出循环，不再运行循环中余下的代码
    message = input(introduce)
    if message == "quit":
        break
    else:
        print(message)

count = 0
while count < 5:                        #使用continue退出当前循环，不再执行此次循环中的余下代码。返回到while循环开头
    count += 1
    if count % 2 == 0:
        continue
    print(count)

unconfirmed_users = ['alice','mike','marry']
confirmed_users = []
while unconfirmed_users:                #在列表之间移动元素
    user = unconfirmed_users.pop()      #pop取尾
    print("Verifying user:" + user)
    confirmed_users.append(user)        #添加到尾端
for user in confirmed_users:
    print("Confirmed user:" + user)

pets = ['dog', 'cat', 'dog', 'fish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:                    #使用in方法来判断元素是否存在于列表中，再通过循环判断来删除每一个该元素
    pets.remove('cat')
print(pets)

responses = {}
flag = True
while flag:                             #使用用户输出来填充字典
    name = input("What's your name:\n")
    response = input("Whinc mountain would you like to climb:\n")
    responses[name] = response          #分别输出字典的键和值

    repeat = input("If you like to continue?(yse/no)")
    if repeat == 'no':                  #存储键值对
        flag = False

print("---Poll Results---")
for name, response in responses.items():#输出键值对
    print(name + " woule like to climb " + response)
'''