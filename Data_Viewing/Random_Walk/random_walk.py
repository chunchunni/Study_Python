from random import choice

class RandomWalk():
    # 生成随机漫步数据的类

    def __init__(self, num_points = 5000) -> None:
        # 初始化随机漫步属性
        self.num_points = num_points

        # 起始地址（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        # 计算随机点
    
        # 不断漫步至指定个数的点
        while len(self.x_values) < self.num_points:
        
            # 决定前进方向和沿这个方向的距离
            # 方向：向右 1 向左 -1
            x_direction = choice([-1,1])
            # 距离：前进步长 0~4
            x_distance = choice([0, 1, 2, 3, 4])
            # 怎么走：方向*距离
            x_step = x_direction * x_distance
        
            y_direction = choice([-1,1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
        
            # 不能原地行走
            if x_step == 0 and y_step == 0:
                continue
        
            # 计算下一个点的坐标值
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
        
            self.x_values.append(x)
            self.y_values.append(y)
