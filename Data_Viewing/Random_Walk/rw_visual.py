import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建一个RandomWalk实例，并绘制所有点
while True:
    # Make a random walk.
    rw = RandomWalk(50)
    rw.fill_walk()

    point_numbers = range(rw.num_points)
    
    # 调整屏幕大小
    plt.figure(figsize=(10,6))

    plt.scatter(0, 0, c = 'green', edgecolors= 'none', s = 10) # 让（0，0）很大
    
    plt.plot(rw.x_values, rw.y_values, linewidth = 1)

    """
    # 去除默认的黑色轮廓，为各个先后顺序不同的点着色
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,edgecolors='none', s=15)  
    """
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break