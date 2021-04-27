import matplotlib.pyplot as plt
# 使用scatter函数绘制散点图

# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]
# 传入单个的元组点可以，传入值列表也可
# plt.scatter(2, 4, s=200)
# plt.scatter(x_values, y_values, s=200)
# 绘图时，默认是蓝色点和黑色轮廓，edgecolor设置为None可以删除轮廓的颜色
# 修改点的颜色可以传入参数c 例如c = (0,0,0.8)表示淡蓝色
# c = y_values, cmap = plt.cm.Blues
# pyplot模块内置了一系列颜色，从起始颜色渐变到结束颜色，可以用于突出数据变化规律。
# 将参数c设置为一个y值列表，参数cmpa告诉pyplot使用哪个颜色映射。其中y值小的为浅蓝色，大的为深蓝色
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Reds, edgecolor = 'None', s = 40)

# 修改标题、标签、字号、刻度
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

# axis指定每个坐标轴的取值范围，分别是X、Y的最大最小值
plt.axis([0,1100,0,1100000])

# 展示图片
plt.show()
# 自动保存图表
plt.savefig("squares_plot.png", bbox_inches = 'tight')