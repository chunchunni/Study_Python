from die import Die
import pygal

# 创建一个D6
die = Die()

# 掷骰子1000次
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 统计各个点数出现的频率
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 结果可视化处理
hist = pygal.Bar()

hist.title = "一千次随机结果"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "结果"
hist.y_title = "随机数据的频率"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')