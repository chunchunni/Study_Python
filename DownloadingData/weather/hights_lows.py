import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'DownloadingData/weather/data/sitka_weather_2018.csv'
with open(filename) as f:

    # 创建一个阅读器相关联的对象，reader处理文件中以逗号分隔的数据，并将数据以元素形式存在列表中
    reader = csv.reader(f)
    # 函数next返回文件的下一行
    header_row = next(reader)
    
    lows, highs = [], []
    # 用于提取日期
    datas = []
    for row in reader:
        # 将日期转化为datatime对象
        #print(row[2])
        current_data = datetime.strptime(row[2], "%Y-%m-%d")
        datas.append(current_data)
        highs.append(int(row[-2]))
        lows.append(int(row[-1]))
    
    # print(highs)


fig = plt.figure(dpi= 128, figsize=(10,6))
plt.plot(datas, highs, c = 'red')
plt.plot(datas, lows, c = 'blue')
# 填充两条折线之间的空白，alpha表示透明度[0,1]
plt.fill_between(datas, highs, lows, facecolor = 'blue', alpha= 0.5)


plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
# 绘制斜的日期标签，并避免重叠
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
