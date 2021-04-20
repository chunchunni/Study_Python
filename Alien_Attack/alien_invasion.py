import sys
import pygame

def run_game():
    # 初始化游戏
    pygame.init()
    # 实参元组（1200，800）用来指定游戏窗口的大小
    screen = pygame.display.set_mode((1200,800))
    # 创建窗口
    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():
            # 单击关闭窗口
            if event.type == pygame.QUIT:
                sys.exit()
    # 更新屏幕，隐藏旧屏幕
    pygame.display.flip()

run_game()
