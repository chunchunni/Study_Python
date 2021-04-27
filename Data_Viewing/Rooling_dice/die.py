from random import randint

class Die():
    # 一个表示骰子的类
    def __init__(self, num_sides=6):
        """默认有六个面"""
        self.num_sides = num_sides
        
    def roll(self):
        """"返回一个位于1和骰子面数之间的随机值"""
        return randint(1, self.num_sides)