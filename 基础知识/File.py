"""                                     #读取文件
with open('file_example.txt') as file_objiect:
                                        #将表示文件及其内容的对象存储到了变量file_object中
    '''
    要以任何方式使用文件，必须先打开文件。open()函数接收一个参数：打开文件名。
    Python在当前执行文件所在目录中查找指定文件。即在File.py所在目录中查找file_example.txt文件。

    关键字with 会在不需要访问文件后将其关闭。
    '''
    contents = file_objiect.read()      #read()方法读取文件全部内容。并将其作为字符串存储在变量contents中。read在文件末尾会返回一个空字符串
    print(contents)                     #打印输出会多一个空行，即末尾的空字符串
    print(contents.rstrip())            #rstrip()方法删除字符串末尾空白

with open('file_work/file_workExample.txt') as file_object:
    '''
    使用相对路径来打开当前运行文件夹下中的其他文件夹的文件。
    '''
    contents = file_object.read()
    print(contents)

filename = 'file_example.txt'
with open(filename) as fb:
    for line in fb:                     #逐行读取文件内容，每行末尾自动添加换行符
        print(line)
        #print(line.rstrip())           #去除换行符，和原文件直接读取一致

with open(filename) as fb:
    lines = fb.readlines()              #每次读取一行并将其存储在一个列表中，再将列表存储在变量lines中
for line in lines:                      #打印列表
    print(line.rstrip())

pai = ''                                #使用文件中的内容
for line in lines:
    pai += line.strip()                 #去除空格和换行
print(pai)
print(len(pai))

filename = 'pi_million_digits.txt'

with open(filename) as fb:              #包含一百万位的大型文件
    lines = fb.readlines()
pai = ''
for line in lines:
    pai += line.strip()
print(pai[:52] + "...")                 #输出小数点后50位
print(len(pai))

birthday = input("Enter birthday, in form mmddyy:")
if birthday in pai:                     #测试生日是否在pai中
    print("Your birthday is in the pai")
else:
    print("Your birthday isn't in pai")
"""

"""                                     #写入文件
filename = 'writing_Example.txt'
with open(filename, 'w') as fb:
    '''
    调用open函数时提供了两个实参，一个是打开文件名，另一个是指定模式
    读取模式'r'，写入模式'w'，附加模式'a'，读取和写入模式'r+'

    若写入文件不存在，则自动创建它。若省略模式实参，则默认参数为只读模式

    当以写入模式'w'打开文件时需要注意，若指定的文件已经存在，则Python会在返回对象前将文件清空

    Python只能将字符串写入文本文件。对于数值数据，必须先使用str函数将其转换为字符串格式
    '''
    fb.write("I love Python.")

with open(filename, 'w') as fb:
    fb.write("I don't love Python.")    #之前写入的I love Python被清空

with open(filename, 'a') as fb:
    fb.write("\nI love C.")             #附加模式下，不会清空原文件中的数据

while True:                             #循环输入，不断添加行到文件中，且每条记录独占一行
    print("Input end to eqit!")
    guest = input("Please enter your name:")
    if guest == 'end':
        break
    else:
        print("Hello! " + guest)
        with open("guest.txt",'a') as fb:
            fb.write(guest+'\n')
"""

"""                                     #异常处理
'''
    每当发生让Python无法处理的错误时，就会创建一个异常对象。如果处理了异常，程序会继续运行；未对异常处理，程序将停止运行。
    异常是使用try-except代码块进行处理的
'''
try:                                    #将可能引发错误的代码放在try-except代码块中
    print(5/0)
except ZeroDivisionError:               #除0错误
    print("Can't divide by 0!")         #try-except后的代码将继续运行

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst Number:")
    if first_number == 'q':
        break
    second_number = input("\nSecond Number:")
    try:
        answer = int(first_number)/int(second_number)#字符串型需要转换为整数型才能进行除法
    except ZeroDivisionError:
        print("Can't divide by 0!")
    else:
        print(answer)

try:
    with open('example.txt') as fb:
        contents = fb.read()
except FileNotFoundError:               #文件不存在异常
    print("Sorry, the file example.txt " + "doesn't exist.")

try:
    with open('example.txt') as fb:
        contents = fb.read()
except FileNotFoundError:               #文件不存在异常
    pass                                #pass语句让Python什么都不做

filename = 'alice.txt'
try:
    with open(filename,'rb') as fb:     #rb的意思是以二进制方式读打开文件
        contents = fb.read()
except FileNotFoundError:
    print("Sorry, the file Alice.txt dosen't exist")
else:
    words = contents.split()            #spilt方法根据一个字符串创建一个单词列表
    len_words = len(words)
    print("The file " + "has about " + str(len_words) +" words.")
"""

                                        #存储数据
import json                             #导入json模块
'''
    使用json模块来存储数据。json模块可以将简单的数据结构存储在文件中，并在文件再次运行时加载该文件中的数据，
    同时还可以使用json在Python程序之间分享数据。
    json.dump()接受两个实参，要存储的数据以及可用于存储数据的文件对象
'''
numbers = [2,3,5,7,11,13]
with open("numbers.json",'w') as fb:
    json.dump(numbers,fb)

with open('numbers.json') as fb:
    numbers = json.load(fb)             #使用json.load()加载存储在numbers.load中的信息，并将其存储在变量numbers中
print(numbers)

'''
    保持和读取用户生成的数据
    对于用户生成的数据，使用json保存可以避免程序停止时，运行用户的信息丢失。
'''
username = input("What's your name?")
filename = 'username.json'
with open(filename,'w') as fb:
    json.dump(username,fb)              #写入数据
    print("We will remember your name " + username + "!")

with open(filename) as fb:
    username = json.load(fb)            #读取数据
    print("Welcome back " + username + "!")


from import_example import *
get_new_username()
greet_user()                            #调用函数访问json中的数据来访问用户
