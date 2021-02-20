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