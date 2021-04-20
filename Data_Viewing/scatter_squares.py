import matplotlib.pyplot as plt
# 绘制散点图

# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]
# 传入单个的元组点可以，传入值列表也可
# plt.scatter(2, 4, s=200)
# plt.scatter(x_values, y_values, s=200)
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=40)

# 修改标题、标签、字号、刻度
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

# axis指定每个坐标轴的取值范围，分别是X、Y的最大最小值
plt.axis([0,1100,0,1100000])

plt.show()