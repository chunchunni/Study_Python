def persons(age, *messages):            #创建一个persons模块
    print("Age: " + str(age))
    for message in messages:
        print(message)

def hello():
    print("Hello!")