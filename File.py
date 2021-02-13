with open('file_example.txt') as file_objiect:
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