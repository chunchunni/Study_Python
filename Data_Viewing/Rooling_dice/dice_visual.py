import pygal
from die import Die

# 产生两个骰子
die_1 = Die()
die_2 = Die()

# 重复掷两个骰子一千次，并将结果计算到一起
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
# 分析结果。统计各个数据产生的频率
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# 数据可视化
hist = pygal.Bar()

hist.title = "一千次随机结果"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "结果"
hist.y_title = "随机数据的频率"

hist.add('D6+D6', frequencies)
hist.render_to_file('dice_visual.svg')