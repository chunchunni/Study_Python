import matplotlib.pyplot as plt
# 根据输入绘制折线图


input_numbers = [1,2,3,4,5]
squares = [1,4,9,16,25]
# plot对输入的数值列表会默认为从x坐标0开始，为了改变这种默认行为，可以另外加入x输入列表
plt.plot(input_numbers,squares,linewidth = 5)

# 修改标题、标签、字号、刻度
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)
plt.show()