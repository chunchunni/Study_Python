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

squares = [value**2 for value in range(1,11)]   #列表解析方式创建列表，所使用的效果等同于前述循环的效果
print(squares)

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

                                        #元组操作
numbers = (20,50)                       #定义拥有两个元素的元组
print(numbers[0])
#numbers[0] = 30                        #报错，因为元组中的元素值不可以修改
print(numbers)
numbers = (30,50)                       #元组的元素值不可以修改，但是可以给元组变量重新赋值
print(numbers)